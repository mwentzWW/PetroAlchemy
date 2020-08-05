# This Python file uses the following encoding: utf-8
import datetime
import json
import os
import sys
import webbrowser
from pathlib import Path

import matplotlib as mpl
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QFile, QObject, Signal, Slot
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import (
    QApplication,
    QComboBox,
    QFileDialog,
    QMainWindow,
    QMessageBox,
)

import eia_data.commodity_prices as prices
import petrolpy_equations.petrolpy_equations as petrolpy
from model.cashflow import create_cashflow as model_create_cashflow
from model.create_decline_curve import (
    create_decline_curve as model_create_decline_curve,
)
from model.custom_models import ListModel, TableModel
from model.import_data import import_data as model_import_data
from model.mpl_canvas_widget import DynamicMplCanvas
from model.plot_decline_curve import plot_decline_curve as model_plot_decline_curve
from model.plot_production import plot_production as model_plot_production
from model.set_production_widgets import (
    set_production_widgets as model_set_production_widgets,
)
from ui_mainwindow import Ui_main_window

mpl.use("Qt5Agg")

VERSION = "0.3.0-beta"


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        # Application variables

        self.model = ListModel()
        self.well_dataframes_dict = {}

        self.decline_curves_dict = {}
        self.model_oil_curves = ListModel()
        self.model_gas_curves = ListModel()

        # Cashflow models

        self.model_cashflow_monthly = TableModel()
        self.model_cashflow_annual = TableModel()
        self.model_cashflow_summary = TableModel()

        # Production Plot setup

        self.widget_production_plot = DynamicMplCanvas(self.ui.widgetProductionPlot)
        toolbar = NavigationToolbar2QT(
            self.widget_production_plot, self.ui.widgetProductionPlot
        )

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.widget_production_plot)

        self.ui.widgetProductionPlot.setLayout(layout)

        self.ui.comboBoxPhase.addItems(["Oil", "Gas"])
        self.ui.comboBoxUnits.addItems(["BOPM/MCFPM", "BOPD/MCFPD"])

    def help_tutorial(self):
        """Open tutorial from Read the Docs"""

        webbrowser.open(
            "https://petroalchemy.readthedocs.io/en/latest/alpha_tutorial.html"
        )

    def help_documentation(self):
        """Open Read the Docs home page"""

        webbrowser.open("https://petroalchemy.readthedocs.io/en/latest/")

    def help_website(self):
        """Open Github Pages website"""

        webbrowser.open("https://mwentzww.github.io/PetroAlchemy/")

    def help_bug(self):
        """Open github bug report"""

        webbrowser.open(
            "https://github.com/mwentzWW/PetroAlchemy/issues/new?assignees=mwentzWW&labels=bug&template=bug_report.md&title="
        )

    def help_feature(self):
        """Open github feature request"""

        webbrowser.open(
            "https://github.com/mwentzWW/PetroAlchemy/issues/new?assignees=mwentzWW&labels=enhancement&template=feature_request.md&title="
        )

    def help_open_bugs_features(self):
        """Open current bugs and features on github"""

        webbrowser.open("https://github.com/mwentzWW/PetroAlchemy/issues")

    def help_contact(self):
        """Open linkedin page"""

        webbrowser.open("https://www.linkedin.com/in/mwentzww/")

    def about_version(self):
        """Message with current version info"""

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"💻 Version installed: {VERSION}")
        msg.setWindowTitle("Current Version")
        msg.exec_()

    def about_take_survey(self):
        """Open survey"""

        webbrowser.open("https://www.surveymonkey.com/r/F22RYZ5")

    def about_donate(self):
        """Open paypal link"""

        webbrowser.open("https://paypal.me/MichaelWentz")

    def import_data(self):
        model_import_data(self)

        self.ui.comboBoxWellSelect.setModel(self.model)
        self.ui.wellListView.setModel(self.model)

    @Slot(str)
    def well_selected(self, well_name):
        """Well selected in comboBoxWellSelect changed, and triggers production plot to redraw"""

        self.widget_production_plot.plot_production(self, well_name, init=True)
        self.ui.widgetProductionPlot.update()
        self.widget_production_plot.update()

    @Slot(str)
    def units_changed(self, units):
        """Well units selected (BOPM/MCFPM or BOPD/MCFPD) and label needs to refresh"""

        self.widget_production_plot.axes.set_ylabel(units)
        self.widget_production_plot.draw()
        self.ui.widgetProductionPlot.update()
        self.widget_production_plot.update()

    @Slot(str)
    def phase_changed(self, phase):
        """Updates widgets based on phase selected"""

        well_name = self.ui.comboBoxWellSelect.currentText()

        model_set_production_widgets(self, well_name, phase=phase)

    def create_decline_curve(self):
        """Calls create_decline_curve from model/"""

        model_create_decline_curve(self)

        # Production Plot comboboxes

        self.ui.comboBoxOilDeclineCurves.setModel(self.model_oil_curves)
        self.ui.comboBoxGasDeclineCurves.setModel(self.model_gas_curves)

        # Cashflow comboboxes

        self.ui.comboBoxOilDeclineCurve.setModel(self.model_oil_curves)
        self.ui.comboBoxGasDeclineCurve.setModel(self.model_gas_curves)

        self.model_oil_curves.layoutChanged.emit()
        self.model_gas_curves.layoutChanged.emit()

    def reset_plot(self):
        """Resets plot with production"""

        well_name = self.ui.comboBoxWellSelect.currentText()

        self.widget_production_plot.plot_production(self, well_name)

    def plot_decline_curves(self):
        """Plots the selected curves on the plot"""

        # Checks whether to use oil, gas, or both curves

        use_oil = self.ui.checkBoxUseOil.isChecked()
        use_gas = self.ui.checkBoxUseGas.isChecked()

        oil_curve = self.ui.comboBoxOilDeclineCurves.currentText()
        gas_curve = self.ui.comboBoxGasDeclineCurves.currentText()

        if use_oil and use_gas:

            model_plot_decline_curve(self, oil_curve, reset=False)
            model_plot_decline_curve(self, gas_curve, reset=False)

        elif use_oil:

            model_plot_decline_curve(self, oil_curve, reset=False)

        elif use_gas:

            model_plot_decline_curve(self, gas_curve, reset=False)

        else:

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Use the two checkboxes to use the decline curves 👀")
            msg.setWindowTitle("No Decline Curves Used")
            msg.exec_()

    def delete_decline_curves(self):
        """Deletes the selected curves on the plot"""

        # Checks whether to use oil, gas, or both curves

        use_oil = self.ui.checkBoxUseOil.isChecked()
        use_gas = self.ui.checkBoxUseGas.isChecked()

        oil_curve = self.ui.comboBoxOilDeclineCurves.currentText()
        gas_curve = self.ui.comboBoxGasDeclineCurves.currentText()

        if use_oil and use_gas:

            self.model_oil_curves.delete(oil_curve)
            del self.decline_curves_dict[oil_curve]

            self.model_gas_curves.delete(gas_curve)
            del self.decline_curves_dict[oil_curve]

        elif use_oil:

            self.model_oil_curves.delete(oil_curve)
            del self.decline_curves_dict[oil_curve]

        elif use_gas:

            self.model_gas_curves.delete(gas_curve)
            del self.decline_curves_dict[oil_curve]

        else:

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Use the two checkboxes to use the decline curves 👀")
            msg.setWindowTitle("No Decline Curves Used")
            msg.exec_()

    def create_cashflow(self):
        """Creates cashflow from setup page inputs"""

        model_create_cashflow(self)

        self.ui.tableViewCashflow.setModel(self.model_cashflow_monthly)
        self.ui.tableViewSummaryValues.setModel(self.model_cashflow_summary)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
