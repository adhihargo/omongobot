import PySide2
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QAbstractItemModel

from app_lib.character_table_model import CharacterTableModel
from app_lib.constants import KEY_NAME
from app_lib.struct.character_table import CharacterTable

DEFAULT_ROW_HEIGHT = 25


class CharacterTableView(QtWidgets.QTableView):
    def __init__(self, parent=None):
        super(CharacterTableView, self).__init__(parent=parent)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().setDefaultSectionSize(DEFAULT_ROW_HEIGHT)
        self.verticalHeader().setMinimumSectionSize(DEFAULT_ROW_HEIGHT)

        table_model = CharacterTableModel()
        self.setModel(table_model)

    @property
    def characterList(self):
        model: CharacterTableModel = self.model()
        return model.itemList

    @characterList.setter
    def characterList(self, value):
        model: CharacterTableModel = self.model()
        model.itemList = value

    @property
    def characterTable(self):
        """

        :return: Character list as dict(name, args)
        """
        model: CharacterTableModel = self.model()
        character_table = CharacterTable(model.itemList)
        return character_table

    def currentChanged(self, current: PySide2.QtCore.QModelIndex, previous: PySide2.QtCore.QModelIndex):
        row_count = self.model().rowCount()
        last_row = row_count - 1
        current_row = current.row()
        if current_row == last_row:
            # if cursor is at the last row, having character name filled, create another row as placeholder for user to
            # create new character.
            current_item: dict = current.internalPointer()
            if current_item.get(KEY_NAME):
                self.model().insertRow(row_count, current.parent())

        previous_row = previous.row()
        # this is for cases requiring row deletion to prevent too many empty rows, therefore limit against deleting
        # single empty row
        if row_count > 1 and current_row != previous_row:
            last = self.model().index(last_row, 0)
            last_item: dict = last.internalPointer()
            if not last_item.get(KEY_NAME) and current_row < last_row - 1:
                # if last row is empty, and we're leaving next-to-last row (so as not to delete when still needed
                self.model().removeRow(last_row, last.parent())
            elif previous_row > 0 and current_row != last_row and not previous.internalPointer().get(KEY_NAME):
                # if leaving an empty row (deleting a row's character name), delete
                self.model().removeRow(previous_row, previous.parent())

    def clear(self):
        model: CharacterTableModel = self.model()
        model.clear()
