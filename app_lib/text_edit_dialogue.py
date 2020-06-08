import re
from collections import namedtuple

from PySide2 import QtCore, QtGui, QtWidgets

from app_lib.constants import KEY_ARGS, KEY_NAME

DocumentFragmentDescriptor = namedtuple("DocumentFragmentDescriptor", ["initial_char_info", "block", "block_end"])
LineDescriptor = namedtuple("LineDescriptor", ["char_info", "extra_args", "block_linenum", "line_start"])

DEFAULT_CHAR_NAME = "CHAR"
CHAR_LINE_REGEX = re.compile(r"(?P<{}>[A-Za-z0-9_\s]+)\s*(<(?P<{}>[\S\s]*)>)?:\s*".format(KEY_NAME, KEY_ARGS))
EXEC_KEY_SEQUENCE = QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Enter)


class TextEditDialogue(QtWidgets.QTextEdit):
    readIter = QtCore.Signal(DocumentFragmentDescriptor)

    def __init__(self, parent=None):
        super(TextEditDialogue, self).__init__(parent=parent)
        self.__char_table__ = {}

    def setCharacterTable(self, char_table: list):
        self.__char_table__ = char_table

    @QtCore.Slot()
    def requestReadLine(self):
        cursor = self.textCursor()
        if cursor.hasSelection():
            pos_start = cursor.selectionStart()
            pos_end = cursor.selectionEnd()

            cursor.setPosition(pos_start)
            block = cursor.block()
            cursor.setPosition(pos_end)
            block_end = cursor.block().next()
        else:
            block = cursor.block()
            block_end = block.next()

        initial_char_info = self.getInitialLine(block)
        self.readIter.emit(DocumentFragmentDescriptor(initial_char_info, block, block_end))

    def getInitialLine(self, block):
        """
        For any text block in any position within a document, find a character assigned to the text block.

        :param block: Text block
        :return: Character info, dialogue
        """
        document = self.document()
        initial_char_info = None
        while block != document.begin():
            block = block.previous()

            ld = self.getLineDescriptor(block)
            if ld.char_info:
                initial_char_info = ld.char_info
                break

        return initial_char_info

    def getLineDescriptor(self, block):
        char_info = None
        extra_args = None
        block_linenum = block.firstLineNumber()
        line_start = 0

        block_text = block.text().strip()
        match = CHAR_LINE_REGEX.search(block_text)
        if match:
            b = match.groupdict()
            char_name = b.get(KEY_NAME)
            char_info = self.__char_table__.get(char_name)
            extra_args = b.get(KEY_ARGS)
            if char_info:
                line_start = match.end()

        return LineDescriptor(char_info, extra_args, block_linenum, line_start)

    def iterDocument(self):
        """
        Iterate whole document
        """
        document = self.document()
        block = document.begin()
        block_end = document.end()
        yield from self.iterBlocks(block, block_end)

    def iterBlocks(self, block, block_end, initial_char_info=None):
        """
        Iterate a document, from BLOCK until before BLOCK_END. Can optionally supply INITIAL_CHAR_INFO for initial lines
        having no character info.

        :param block: Start block
        :param block_end: End block to limit iteration
        :param initial_char_info: Character info for first lines having none.
        """
        # char_info = {KEY_NAME: DEFAULT_CHAR_NAME}
        char_info = initial_char_info or {}
        while block != block_end:
            ld = self.getLineDescriptor(block)
            if ld.char_info:
                char_info = ld.char_info

            block_text = block.text()[ld.line_start:]
            if block_text != "":
                yield char_info, block_text
            block = block.next()
