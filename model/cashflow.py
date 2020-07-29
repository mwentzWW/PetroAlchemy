import numpy as np
import pandas as pd

from petrolpy_equations import petrolpy_equations as petrolpy
from model.custom_models import TableModel


def create_cashflow(self):
    """Get all cashflow inputs and create cashflow dataframe"""

    # get gross oil and gas curves

    oil_decline_curve = self.ui.comboBoxOilDeclineCurve.currentText()
    gas_decline_curve = self.ui.comboBoxGasDeclineCurve.currentText()

    df_oil = self.decline_curves_dict.get(oil_decline_curve)
    df_gas = self.decline_curves_dict.get(gas_decline_curve)

    delta_time_yrs = df_oil.delta_time_yrs.tolist()

    shape = df_oil.shape

    if df_oil is None:

        oil_curve = np.zeros(shape)

    else:

        oil_curve = df_oil[oil_decline_curve]

    if df_gas is None:

        gas_curve = np.zeros(shape)

    else:

        gas_curve = df_gas[gas_decline_curve]

    months = np.arange(1, 601)

    cashflow_start_date = self.ui.dateEditCashflowStart.date().toPython()

    time = pd.date_range(cashflow_start_date, periods=600, freq="M")

    data = zip(months, oil_curve, gas_curve, delta_time_yrs)

    df_cashflow = pd.DataFrame(
        data, columns=["Month", "Gross Oil", "Gross Gas", "delta_time_yrs"], index=time
    )

    # create net volumes

    net_interest = float(self.ui.doubleSpinBoxNetRevenueInterest.value()) / 100

    df_cashflow["Net Oil"] = df_cashflow["Gross Oil"] * net_interest
    df_cashflow["Net Gas"] = df_cashflow["Gross Gas"] * net_interest

    # display oil and gas prices

    spot_oil_price = float(self.ui.doubleSpinBoxOilPrice.value())
    spot_gas_price = float(self.ui.doubleSpinBoxGasPrice.value())

    oil_diff = float(self.ui.doubleSpinBoxOilDiff.value())
    gas_diff = float(self.ui.doubleSpinBoxGasDiff.value())

    net_oil_price = spot_oil_price - oil_diff
    net_gas_price = spot_gas_price - gas_diff

    df_cashflow["Spot Oil Price ($/BBL)"] = spot_oil_price
    df_cashflow["Spot Gas Price ($/MCF)"] = spot_gas_price

    df_cashflow["Net Oil Price ($/BBL)"] = net_oil_price
    df_cashflow["Net Gas Price ($/MCF)"] = net_gas_price

    # Revenues

    df_cashflow["Net Oil Revenue (M$)"] = (
        df_cashflow["Net Oil"] * df_cashflow["Net Oil Price ($/BBL)"] / 1000
    )
    df_cashflow["Net Gas Revenue (M$)"] = (
        df_cashflow["Net Gas"] * df_cashflow["Net Gas Price ($/MCF)"] / 1000
    )
    df_cashflow["Net Operating Revenue (M$)"] = (
        df_cashflow["Net Oil Revenue (M$)"] + df_cashflow["Net Gas Revenue (M$)"]
    )

    # Taxes, OPEX, and CAPEX

    sev_tax_rate = float(self.ui.spinBoxSeveranceTax.value()) / 100
    opex = float(self.ui.spinBoxOPEX.value())
    capex = float(self.ui.doubleSpinBoxCAPEX.value())

    df_cashflow["Severance Taxes (M$)"] = (
        df_cashflow["Net Operating Revenue (M$)"] * sev_tax_rate
    )
    df_cashflow["OPEX (M$)"] = opex / 1000
    df_cashflow["CAPEX (M$)"] = capex * 1000
    df_cashflow["CAPEX (M$)"][1:] = 0

    # Net Revenue and Cumulative Net Revenue

    df_cashflow["Net Revenue (M$)"] = (
        df_cashflow["Net Operating Revenue (M$)"]
        - df_cashflow["Severance Taxes (M$)"]
        - df_cashflow["OPEX (M$)"]
        - df_cashflow["CAPEX (M$)"]
    )
    df_cashflow["Cumulative Net Revenue (M$)"] = df_cashflow[
        "Net Revenue (M$)"
    ].cumsum()

    # Discounted values

    ann_disc_rate = float(self.ui.spinBoxDiscountRate.value()) / 100

    monthly_disc_rate = petrolpy.ann_to_monthly_disc_rate(ann_disc_rate)

    df_cashflow["Discounted Net Revenue (M$)"] = df_cashflow["Net Revenue (M$)"] * (
        1 / ((1 + monthly_disc_rate) ** (df_cashflow["Month"] - 1))
    )
    df_cashflow["Cumulative Discounted Net Revenue (M$)"] = df_cashflow[
        "Discounted Net Revenue (M$)"
    ].cumsum()

    npv_rate = df_cashflow["Discounted Net Revenue (M$)"].sum()

    # drop months column, 1 is for columns

    df_cashflow.drop("Month", 1, inplace=True)

    # Store current cashflow dataframe to Mainwindow class, group by month in case decline curve is daily data

    df_cashflow_monthly = df_cashflow.groupby(pd.Grouper(freq="M")).sum().reset_index()
    df_cashflow_monthly["index"] = df_cashflow_monthly["index"].dt.strftime("%m-%d-%Y")
    df_cashflow_monthly.set_index("index", inplace=True)

    df_cashflow_annual = df_cashflow.groupby(pd.Grouper(freq="Y")).sum().reset_index()
    df_cashflow_annual["index"] = df_cashflow_annual["index"].dt.strftime("%m-%d-%Y")
    df_cashflow_annual.set_index("index", inplace=True)

    self.model_cashflow_monthly = TableModel(df_cashflow_monthly)
    self.model_cashflow_monthly.layoutChanged.emit()
    self.model_cashflow_annual = TableModel(df_cashflow_annual)
    self.model_cashflow_annual.layoutChanged.emit()

    # Annual Net Revenue


#     ann_net_revenue = (
#         df_cashflow_annual["Net Revenue (M$)"]
#     )

#     # Summary Values

#     # Economic Life cutoff

#     try:
#         econ_life_years = round(
#             float(
#                 (df_cashflow_monthly[df_cashflow_monthly["Net Revenue (M$)"] > 0].index[-1] + 1)
#                 / 12
#             ),
#             1,
#         )
#     except IndexError:
#         # Error ocurrs when Net Revenue is never positive
#         econ_life_years = 0

#     # IRR, ROI, DROI as %

#     irr_annual = petrolpy.irr(df_cashflow_monthly["Net Revenue (M$)"], monthly=True)

#     roi = df_cashflow_monthly["Net Revenue (M$)"].sum() / (capex * 1000)
#     dcf_roi = npv_rate / (capex * 1000)

#     # NPV8, NPV10, NPV15, NPV20, NPV25, NPV30

#     rates = [8, 10, 15, 20, 25, 30]
#     npv_data = []
#     npv_values = []

#     for rate in rates:

#         monthly_disc_rate = petrolpy.ann_to_monthly_disc_rate(rate / 100)

#         df_cashflow_monthly[f"NPV{rate} (M$)"] = df_cashflow_monthly["Net Revenue (M$)"] * (
#             1 / ((1 + monthly_disc_rate) ** (df_cashflow_monthly["Month"] - 1))
#         )
#         npv_sum = df_cashflow_monthly[f"NPV{rate} (M$)"].sum()
#         npv_data.append((f"NPV{rate}", f"{npv_sum:,.0f} M$"))
#         npv_values.append(npv_sum)

#     # Payout

#     try:
#         payout_years = round(
#             float(
#                 (
#                     df_cashflow_monthly[
#                         df_cashflow_monthly["Cumulative Net Revenue (M$)"] > 0
#                     ].index[0]
#                     + 1
#                 )
#                 / 12
#             ),
#             1,
#         )

#     except IndexError:
#         # Error ocurrs when Cumulative Net Revenue is never positive
#         payout_years = "Infinite"

#     # 1 year EUR,  5 (60 months) year EUR, 50 (600 months) year EUR

#     oil_eur_1 = int(df_cashflow_annual["Gross Oil"][0].sum() / 1_000)
#     oil_eur_5 = int(df_cashflow_annual["Gross Oil"][:4].sum() / 1_000)
#     oil_eur_50 = int(df_cashflow_annual["Gross Oil"][:49].sum() / 1_000)

#     gas_eur_1 = round(df_cashflow_annual["Gross Gas"][0].sum() / 1_000_000, 1)
#     gas_eur_5 = round(df_cashflow_annual["Gross Gas"][:4].sum() / 1_000_000, 1)
#     gas_eur_50 = round(df_cashflow_annual["Gross Gas"][:49].sum()/ 1_000_000, 1)

#     eur_data = (
#         ("1 Year EUR", f"{oil_eur_1:,} MBO & {gas_eur_1} BCF"),
#         ("5 Year EUR", f"{oil_eur_5:,} MBO & {gas_eur_5} BCF"),
#         ("50 Year EUR", f"{oil_eur_50:,} MBO & {gas_eur_50} BCF"),
#     )

#     # Summary data to display

#     summary_data = (
#         ("Economic Life", f"{econ_life_years} Years"),
#         ("NPV of Selected Rate", f"{npv_rate:,.0f} M$"),
#         ("Internal Rate of Return", f"{irr_annual:.0%}"),
#         ("Payout", f"{payout_years} Years"),
#         ("Return on Investment", f"{roi:.0%}"),
#         ("Discounted Return on Investment", f"{dcf_roi:.0%}"),
#     )

#     self.treeview_summary.delete(*self.treeview_summary.get_children())
#     for index, row in enumerate(summary_data):

#         self.treeview_summary.insert("", index, index, values=row)

#     # Discount rate values to display

#     self.treeview_discount.delete(*self.treeview_discount.get_children())
#     for index, row in enumerate(npv_data):

#         self.treeview_discount.insert("", index, index, values=row)

#     # EUR values to display

#     self.treeview_eur.delete(*self.treeview_eur.get_children())
#     for index, row in enumerate(eur_data):

#         self.treeview_eur.insert("", index, index, values=row)

#     # Summary df to save to excel

#     data_dict = {
#         "Economic Life (Years)": econ_life_years,
#         "NPV of Selected Rate (M$)": npv_rate,
#         "Internal Rate of Return": irr_annual,
#         "Payout (Years)": payout_years,
#         "Return on Investment": roi,
#         "Discounted Return on Investment": dcf_roi,
#         "NPV8 (M$)": npv_values[0],
#         "NPV10 (M$)": npv_values[1],
#         "NPV15 (M$)": npv_values[2],
#         "NPV20 (M$)": npv_values[3],
#         "NPV25 (M$)": npv_values[4],
#         "NPV30 (M$)": npv_values[5],
#     }

#     self.df_summary_output = pd.DataFrame(data_dict, index=["Values"])

#     # Output cashflow to text

#     self.controller.children["!frame"].children[
#         "!cashflowoutputpage"
#     ].cashflow_to_text(df=df_cashflow)

# def save_cashflow(self):
#     """Save cashflow and summary output to excel"""

#     save_as = tk.filedialog.asksaveasfilename(
#         filetypes=[("Excel files", ".xlsx .xls")], defaultextension=".xlsx"
#     )

#     with pd.ExcelWriter(save_as, engine="xlsxwriter") as writer:

#         self.df_summary_output.to_excel(
#             writer, sheet_name="PetroBase Summary Output", index=False
#         )
#         self.df_cashflow.to_excel(
#             writer, sheet_name="PetroBase Cashflow", index=False
#         )
