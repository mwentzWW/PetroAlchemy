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

    months = pd.date_range(curve_start_date, periods=600, freq="M")

    # create days date range because months sets inital date to end of month

    delta_time_yrs = [(date - months[0]).days / 365 for date in months]

    df_curve = pd.DataFrame(
        zip(months, delta_time_yrs), columns=["months", "delta_time_yrs"]
    )

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

    qt_curve_name = QtGui.QStandardItem(curve_name)

    if curve_phase == "Oil":
        parent.model_oil_curves.appendRow(qt_curve_name)
    else:
        parent.model_gas_curves.appendRow(qt_curve_name)

    model_plot_decline_curve(parent, curve_name=curve_name)
