from PySide2 import QtWidgets


class TemplateLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super(TemplateLineEdit, self).__init__(parent=parent)

    def displayText(self) -> str:
        display_text = super().text() + ".wav"
        print(display_text)
        return display_text
