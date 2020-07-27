from PySide2 import QtCore
from PySide2.QtWidgets import QMessageBox
from PySide2.QtCore import Qt


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

