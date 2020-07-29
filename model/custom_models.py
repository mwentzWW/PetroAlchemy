import datetime

from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMessageBox


class ListModel(QtCore.QAbstractListModel):
    def __init__(self, *args, list=None, **kwargs):
        super(ListModel, self).__init__(*args, **kwargs)
        self.list = list or []

    def data(self, index, role):
        if role == Qt.DisplayRole:

            try:
                text = self.list[index.row()]
                return text
            except IndexError:
                pass

    def rowCount(self, index):
        return len(self.list)

    def add(self, text: str):
        """Append text to model list"""

        text = str(text).strip()

        if text:
            if text not in self.list:

                self.list.append(text)
                self.layoutChanged.emit()

    def delete(self, text: str):
        """Remove text by name from model list"""

        text = str(text).strip()

        if text in self.list:

            self.list.remove(text)
            self.layoutChanged.emit()


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data=None):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:

            value = self._data.iloc[index.row(), index.column()]

            if isinstance(value, datetime.datetime):

                return value.strftime("%m-%d-%Y")

            if isinstance(value, float):

                return f"{value:,.2f}"

            if isinstance(value, int):

                return f"{value:,}"

        if role == Qt.TextAlignmentRole:

            return Qt.AlignCenter

    def rowCount(self, index):

        return self._data.shape[0]

    def columnCount(self, index):

        return self._data.shape[1]

    def headerData(self, section, orientation, role):

        if role == Qt.DisplayRole:

            if orientation == Qt.Horizontal:

                return str(self._data.columns[section])

            if orientation == Qt.Vertical:

                return str(self._data.index[section])
