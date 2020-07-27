import datetime

import pandas as pd
from PySide2 import QtGui
from PySide2.QtWidgets import QMessageBox

import petrolpy_equations.petrolpy_equations as petrolpy
from model.plot_decline_curve import plot_decline_curve as model_plot_decline_curve


def create_decline_curve(parent, curve_name=None):
    """Creates decline curve from widget curve inputs"""

    if curve_name is None:
        curve_name = parent.ui.lineEditDeclineCurveName.text()

    if curve_name == "":
        QMessageBox.warning(
            parent, "Error", "You need to enter a name for the decline curve 👀"
        )
        parent.ui.lineEditDeclineCurveName.setFocus()
        return

    curve_start_date = parent.ui.dateEditCurveStart.date().toPython()

    # Calculated time for 50 years

    unit_time = parent.ui.comboBoxUnits.currentText()

    if unit_time == "BOPM/MCFPM":
        unit_time_factor = 1
        freq = "M"
    else:
        unit_time_factor = 12
        freq = "D"

    time = pd.date_range(curve_start_date, periods=600 * unit_time_factor, freq=freq)

    # Gets delta time by taking the date (day) - initial date (day) and divide by 365

    delta_time_yrs = [(date - time[0]).days / 365 for date in time]

    df_curve = pd.DataFrame(delta_time_yrs, columns=["delta_time_yrs"], index=time)

    di_secant = float(parent.ui.doubleSpinBoxDi.value() / 100)
    b_factor = float(parent.ui.doubleSpinBoxBFactor.value())
    min_decline = float(parent.ui.doubleSpinBoxMinDecline.value() / 100)
    qi = int(parent.ui.spinBoxRate.value())

    curve_phase = parent.ui.comboBoxPhase.currentText()

    nominal_di = petrolpy.convert_secant_di_to_nominal(di_secant, b_factor)

    df_curve[curve_name] = petrolpy.arps_decline_rate_q(
        qi, b_factor, nominal_di, delta_time_yrs, min_decline
    )

    if curve_name in parent.decline_curves_dict:
        del parent.decline_curves_dict[curve_name]

    parent.decline_curves_dict[curve_name] = df_curve

    if curve_phase == "Oil":
        parent.list_oil_curves.append(curve_name)
    else:
        parent.list_gas_curves.append(curve_name)

    model_plot_decline_curve(parent, curve_name=curve_name)
