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
from model.import_data import import_data as model_import_data
from model.plot_decline_curve import plot_decline_curve as model_plot_decline_curve
from model.plot_production import plot_production as model_plot_production


class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=14, height=12, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(
            self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        FigureCanvas.updateGeometry(self)

        plt.style.use("bmh")


class DynamicMplCanvas(MyMplCanvas):
    """A canvas that updates on the comboBoxWellSelect signal"""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def plot_decline_curve(self, parent):
        model_plot_decline_curve(self, parent)

    def plot_production(self, parent, well_name, init=False):
        model_plot_production(self, parent, well_name, init)
