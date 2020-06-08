import os
import subprocess
import sys

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QApplication, QFileDialog

from app_lib.constants import KEY_ESPEAK_ARGS, KEY_ESPEAK_PATH, KEY_OUTPUT_PATH
from app_lib.forms.ui_dialog_preferences import Ui_DialogPreferences


class DialogPreferences(QtWidgets.QDialog):
    def __init__(self, settings: QtCore.QSettings = None, parent=None):
        super(DialogPreferences, self).__init__(parent=parent)
        self.ui = Ui_DialogPreferences()
        self.ui.setupUi(self)

        self.settings = settings
        if isinstance(self.settings, QtCore.QSettings):
            self.binary_path = self.settings.value(KEY_ESPEAK_PATH, defaultValue="")
            self.binary_args = self.settings.value(KEY_ESPEAK_ARGS, defaultValue="")
            self.output_path = self.settings.value(KEY_OUTPUT_PATH, defaultValue="")

    @QtCore.Slot()
    def on_btnEspeakPathBrowse_clicked(self):
        old_binary_path = self.binary_path
        old_dir = os.path.dirname(old_binary_path)
        binary_path, _ = QFileDialog.getOpenFileName(parent=self, caption="Espeak Executable Path", dir=old_dir,
                                                     filter="Executable (*.exe)")
        if os.path.isfile(binary_path):
            self.ui.lneEspeakPath.setText(binary_path)

    @QtCore.Slot()
    def on_btnEspeakTest_clicked(self):
        binary_path = self.binary_path
        if os.path.isfile(binary_path):
            subprocess.call([binary_path, self.binary_args, "Test"])

    @QtCore.Slot()
    def on_btnSave_clicked(self):
        if isinstance(self.settings, QtCore.QSettings):
            self.settings.setValue(KEY_ESPEAK_PATH, self.binary_path)
            self.settings.setValue(KEY_ESPEAK_ARGS, self.binary_args)
            self.settings.setValue(KEY_OUTPUT_PATH, self.output_path)
        self.accept()

    @QtCore.Slot()
    def on_btnDefaultOutputPathBrowse_clicked(self):
        old_output_path = self.output_path
        output_path = QtWidgets.QFileDialog.getExistingDirectory(parent=self, dir=old_output_path)
        if output_path:
            self.output_path = output_path

    @property
    def output_path(self):
        return self.ui.lneDefaultOutputPath.text()

    @output_path.setter
    def output_path(self, value):
        self.ui.lneDefaultOutputPath.setText(value)

    @property
    def binary_args(self):
        return self.ui.lneEspeakArgs.text()

    @binary_args.setter
    def binary_args(self, value):
        self.ui.lneEspeakArgs.setText(value)

    @property
    def binary_path(self):
        return self.ui.lneEspeakPath.text()

    @binary_path.setter
    def binary_path(self, value):
        self.ui.lneEspeakPath.setText(value)


if __name__ == '__main__':
    app = QApplication([])

    settings = QtCore.QSettings(r"..\test.ini", QtCore.QSettings.IniFormat)

    dialog = DialogPreferences(settings=settings)
    dialog.show()

    sys.exit(app.exec_())
