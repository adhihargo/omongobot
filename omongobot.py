import logging
import os
import sys

from PySide2 import QtCore, QtWidgets

from app_lib.constants import CONFIG_FILE_NAME
from app_lib.main_window import MainWindow


def run():
    if os.getenv("DEBUG"):
        logging.basicConfig(level=logging.DEBUG)

    app = QtWidgets.QApplication([])

    script_dir = os.path.dirname(__file__)
    settings = QtCore.QSettings(os.path.join(script_dir, CONFIG_FILE_NAME), QtCore.QSettings.IniFormat)

    window = MainWindow(settings)
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
