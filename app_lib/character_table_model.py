import typing

import PySide2
from PySide2 import QtCore

from app_lib.constants import KEY_ARGS, KEY_FIELD, KEY_NAME

HORIZONTAL_HEADER_LIST = ({KEY_NAME: "Char. Name", KEY_FIELD: KEY_NAME},
                          {KEY_NAME: "Args", KEY_FIELD: KEY_ARGS})


class CharacterTableModel(QtCore.QAbstractItemModel):
    __character_list__ = [{KEY_NAME: ""}]
    __root_index__ = QtCore.QModelIndex()

    def __init__(self, parent=None):
        super(CharacterTableModel, self).__init__(parent=parent)

    @property
    def itemList(self):
        return self.__character_list__

    @itemList.setter
    def itemList(self, item_list: list):
        old_row_count = len(self.__character_list__)

        new_row_count = len(item_list)
        self.beginInsertRows(self.__root_index__, old_row_count, old_row_count + new_row_count - 1)
        self.__character_list__.extend(item_list)
        self.endInsertRows()

        self.beginRemoveRows(self.__root_index__, 0, old_row_count - 1)
        for i in range(0, old_row_count):
            self.__character_list__.pop(0)
        self.endRemoveRows()

        row_count = self.rowCount()

    def parent(self, index: QtCore.QModelIndex) -> PySide2.QtCore.QObject:
        return self.__root_index__

    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int:
        character_count = len(self.__character_list__)
        return character_count

    def columnCount(self, parent: QtCore.QModelIndex = ...) -> int:
        return len(HORIZONTAL_HEADER_LIST)

    def index(self, row: int, column: int, parent: QtCore.QModelIndex = ...) -> QtCore.QModelIndex:
        if row > self.rowCount() or column > self.columnCount():
            return QtCore.QModelIndex()

        item_info = self.__character_list__[row]
        return self.createIndex(row, column, item_info)

    def headerData(self, section: int, orientation: PySide2.QtCore.Qt.Orientation, role: int = ...) -> typing.Any:
        if section > self.columnCount():
            return super().headerData(section, orientation, role)
        if orientation == QtCore.Qt.Orientation.Horizontal:
            if role == QtCore.Qt.DisplayRole:
                column_info = HORIZONTAL_HEADER_LIST[section]
                return column_info[KEY_NAME]

    def data(self, index: PySide2.QtCore.QModelIndex, role: int = ...) -> typing.Any:
        if not index.isValid():
            return

        item_row, item_column = index.row(), index.column()
        if item_row > self.rowCount() or item_column > self.columnCount():
            return

        if role in [QtCore.Qt.DisplayRole, QtCore.Qt.EditRole]:
            item_info = self.__character_list__[item_row]
            column_info = HORIZONTAL_HEADER_LIST[item_column]
            field = column_info[KEY_FIELD]
            return item_info.get(field)

        return None

    def setData(self, index: PySide2.QtCore.QModelIndex, value: typing.Any, role: int = ...) -> bool:
        """

        :param index: Index of item to modify
        :param value: New value of item indexed
        :param role: In what role the new value is to be assigned as
        :return: Success
        """
        value: str = value.strip()
        item_info: dict = index.internalPointer()
        column_info = HORIZONTAL_HEADER_LIST[index.column()]
        field = column_info[KEY_FIELD]
        item_info[field] = value

        return True

    def insertRow(self, row: int, parent: PySide2.QtCore.QModelIndex = ...) -> bool:
        """

        :param row: Row position to insert to
        :param parent: Parent index of row to insert to
        :return: Success
        """
        self.beginInsertRows(parent, row, row)
        self.__character_list__.insert(row, {})
        self.endInsertRows()

        return True

    def removeRow(self, row: int, parent: PySide2.QtCore.QModelIndex = ...) -> bool:
        """

        :param row: Row position to remove from
        :param parent: Parent index of row to remove from
        :return: Success
        """
        self.beginRemoveRows(parent, row, row)
        self.__character_list__.pop(row)
        self.endRemoveRows()

        return True

    def flags(self, index: PySide2.QtCore.QModelIndex) -> PySide2.QtCore.Qt.ItemFlags:
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

    def clear(self):
        self.itemList = [{KEY_NAME: ""}]
