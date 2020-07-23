import os
from pathlib import Path

import pandas as pd
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QFile, QObject, Signal, Slot
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow, QMessageBox


def import_data(self):

    dialog = QFileDialog(self)
    dialog.setFileMode(QFileDialog.ExistingFiles)

    # filter files to excel and csv, not working yet
    # dialog.setNameFilter(QObject.tr("Excel/CSV (*.xls *.xlss *.csv)"))

    dialog.setDirectory(os.getcwd())
    dialog.setViewMode(QFileDialog.Detail)

    if dialog.exec_():
        filenames = dialog.selectedFiles()

    wells_total = 0

    for fname in filenames:
        file_type = Path(fname).suffix

        if file_type == (".xlsx" or ".xls"):
            df = pd.read_excel(fname, parse_dates=True)

        elif file_type == (".csv"):
            df = pd.read_csv(fname, parse_dates=["Date"])

        df.columns = map(str.lower, df.columns)

        # csv doesn't always parse dates correctly

        df.date = [time.date() for time in df.date]

        well_names = df["well name"].unique().tolist()

        num_wells = len(well_names)

        wells_total = wells_total + num_wells

        for well_name in well_names:

            well_name = str(well_name)

            # checks if the exact well name is already in the model

            matches = self.model.findItems(well_name, QtCore.Qt.MatchExactly)

            if not matches:

                well_item = QtGui.QStandardItem(well_name)
                self.model.appendRow(well_item)

                dict_well_name = well_name.replace(" ", "_")
                self.well_dataframes_dict[dict_well_name] = df.loc[
                    df["well name"] == well_name
                ].reset_index()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"{well_name} already exists, check the file and try again")
                msg.setWindowTitle("Import Failed")
                msg.exec_()

    if wells_total > 1:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"{wells_total} wells have been added 🚀")
        msg.setWindowTitle("Import Finished")
        msg.exec_()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(f"{well_name} has been added 🚀")
        msg.setWindowTitle("Import Finished")
        msg.exec_()
