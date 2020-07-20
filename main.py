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
from model.create_decline_curve import (
    create_decline_curve as model_create_decline_curve,
)
from model.import_data import import_data as model_import_data
from model.plot_decline_curve import plot_decline_curve as model_plot_decline_curve
from model.plot_production import plot_production as model_plot_production
from model.plot_widgets import DynamicMplCanvas
from ui_mainwindow import Ui_main_window

mpl.use("Qt5Agg")

VERSION = "0.3.0-beta"


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        # Application variables

        self.model = QtGui.QStandardItemModel()
        self.well_dataframes_dict = {}

        self.decline_curves_dict = {}
        self.model_oil_curves = QtGui.QStandardItemModel()
        self.model_gas_curves = QtGui.QStandardItemModel()

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

    def about_version(self):
        "Message with current version info"

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"💻 Version installed: {VERSION}")
        msg.setWindowTitle("Current Version")
        msg.exec_()

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
        "Open current bugs and features on github"

        webbrowser.open("https://github.com/mwentzWW/PetroAlchemy/issues")

    def help_contact(self):
        "Open linkedin page"

        webbrowser.open("https://www.linkedin.com/in/mwentzww/")

    def help_take_survey(self):
        "Open survey"

        webbrowser.open("https://www.surveymonkey.com/r/F22RYZ5")

    def import_data(self):
        model_import_data(self)

        self.ui.comboBoxWellSelect.setModel(self.model)
        self.ui.wellListView.setModel(self.model)

    @Slot(str)
    def well_selected(self, well_name):
        """Well selected in comboBoxWellSelect changed, and triggers production plot to redraw"""

        self.widget_production_plot.plot_production(self, well_name)
        self.ui.widgetProductionPlot.update()
        self.widget_production_plot.update()

    def create_decline_curve(self):
        """Calls create_decline_curve from model/"""

        model_create_decline_curve(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
