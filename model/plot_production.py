import datetime

import matplotlib.dates as mdates
from matplotlib import pyplot as plt
from matplotlib.ticker import StrMethodFormatter


def plot_production(self, parent, well_name, init=False):
    """Plot production for current well selected"""

    dict_well_name = str(well_name).replace(" ", "_")

    df_selected = parent.well_dataframes_dict.get(dict_well_name)

    if init:
        # set line edit decline curve name

        parent.ui.lineEditDeclineCurveName.setText(f"{well_name} Oil Decline Curve")

        # Set dateEditCurveStart as first date of dataframe

        parent.ui.dateEditCurveStart.setDate(df_selected["date"][0])

        # set plot widgets with oil early max

        parent.ui.spinBoxRate.setValue(int(df_selected.oil[:6].max()))
        max_id = df_selected.oil[:6].idxmax()

        if len(df_selected.index) > 11:
            di_estimate_float = (
                df_selected["oil"][max_id] - df_selected["oil"][max_id + 12]
            ) / df_selected["oil"][max_id]

            time_scale = (
                df_selected["date"][max_id + 12] - df_selected["date"][max_id]
            ).days

            if time_scale == 365:
                di_estimate_pct = round(di_estimate_float * 100, 2)
                parent.ui.doubleSpinBoxDi.setValue(di_estimate_pct)
        else:
            parent.ui.doubleSpinBoxDi.setValue(75)

    # Plot chart

    self.axes.clear()

    self.axes.plot(
        df_selected["date"], df_selected["oil"], "g", label="Oil", linewidth=2
    )
    self.axes.plot(
        df_selected["date"], df_selected["gas"], "r", label="Gas", linewidth=2
    )

    self.axes.set_yscale("log")
    self.axes.yaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))
    self.axes.yaxis.set_minor_formatter(StrMethodFormatter("{x:,.0f}"))
    self.axes.tick_params(axis="y", which="major", labelsize=8)
    self.axes.tick_params(axis="y", which="minor", labelsize=6)
    self.axes.tick_params(axis="x", which="both", labelsize=8)

    years = mdates.YearLocator()  # every year
    months = mdates.MonthLocator()  # every month
    days = mdates.DayLocator()
    x_format = mdates.DateFormatter("%m/%d/%Y")

    year_range = df_selected["date"].max().year - df_selected["date"].min().year

    if year_range < 2:
        self.axes.xaxis.set_major_locator(months)
        self.axes.xaxis.set_major_formatter(x_format)

    else:
        self.axes.xaxis.set_major_locator(years)
        self.axes.xaxis.set_major_formatter(x_format)
        self.axes.xaxis.set_minor_locator(months)

    datemin = datetime.date(df_selected["date"].min().year, 1, 1)
    datemax = datetime.date(df_selected["date"].max().year + 1, 1, 1)
    self.axes.set_xlim(datemin, datemax)
    self.axes.set_ylim(ymin=10)

    for label in self.axes.xaxis.get_ticklabels():
        label.set_rotation(45)

    self.axes.grid(
        which="major", axis="x", color="grey", linestyle="--", linewidth=1, alpha=0.5,
    )
    self.axes.grid(
        which="both", axis="y", color="grey", linestyle="--", linewidth=1, alpha=0.5,
    )

    self.axes.legend(
        bbox_to_anchor=(0, 1.02, 1, 0.102), loc="best", ncol=2, borderaxespad=0
    )
    self.axes.set_title(f"{well_name}", fontsize=16)

    self.axes.set_ylabel(parent.ui.comboBoxUnits.currentText())

    self.draw()
