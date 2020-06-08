import enum
import itertools
import logging
import os

from PySide2 import QtCore, QtWidgets

from app_lib.constants import APP_NAME, APP_VERSION, FILE_FILTER, KEY_ARGS, KEY_ESPEAK_ARGS, KEY_ESPEAK_PATH, \
    KEY_NAME, KEY_OUTPUT_PATH
from app_lib.dialog_preferences import DialogPreferences
from app_lib.dialog_record import DialogRecord
from app_lib.espeakng import ESpeakNG
from app_lib.struct.document_descriptor import DocumentDescriptor
from app_lib.struct.document_io import DocumentIO
from app_lib.forms.ui_main_window import Ui_MainWindow
from app_lib.runnable import Runnable
from app_lib.character_table_model import CharacterTableModel
from app_lib.text_edit_dialogue import DEFAULT_CHAR_NAME, DocumentFragmentDescriptor

PLAYBACK_TIMER_INTERVAL = 500


class DocumentMode(enum.Enum):
    DOC_READ = 1
    DOC_WRITE = 2
    DOC_MODIFY = 3


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, settings: QtCore.QSettings = None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = settings

        self.logger = logging.getLogger(self.__class__.__name__)
        self.thread_pool = QtCore.QThreadPool()
        self.thread_pool.setMaxThreadCount(1)
        self.runnable = None

        self.ui.actReadLine.triggered.connect(self.ui.txeDialogue.requestReadLine)
        self.ui.actReadAll.triggered.connect(self.on_txeDialogue_readDocument)

        self.ui.txeDialogue.setFocus()
        self.ui.txeDialogue.setCharacterTable(self.ui.tbvCharacters.characterTable)
        self.setPlaybackEnabled(True)
        self.playback_timer = QtCore.QTimer(self)
        self.playback_timer.timeout.connect(self.on_playback_timeout)

        self.document_io = DocumentIO()
        self.document = DocumentDescriptor("")
        self.setCurrentDocument()

    def setCurrentDocument(self, mode: DocumentMode = DocumentMode.DOC_READ):
        window_title = "{} {}".format(APP_NAME, APP_VERSION)
        is_read_mode = mode == DocumentMode.DOC_READ

        if is_read_mode:
            self.ui.txeDialogue.clear()
            self.ui.tbvCharacters.clear()

        document_path = self.document.document_path
        if document_path:
            file_name = os.path.basename(document_path)
            window_title += " - {}".format(file_name)

        self.setWindowTitle(window_title)

    def readDocument(self, document: DocumentDescriptor):
        qt_document = self.ui.txeDialogue.document()
        self.document_io.read(document)
        qt_document.setPlainText(self.document.document_body)
        self.ui.tbvCharacters.characterList = self.document.character_list
        self.logger.debug("Read from {} succeeded".format(document.document_path))

    def writeDocument(self, document: DocumentDescriptor):
        qt_document = self.ui.txeDialogue.document()
        document.document_body = qt_document.toPlainText()
        document.character_list = self.ui.tbvCharacters.characterList.copy()
        self.document_io.write(document)
        # self.logger.debug("Write to {} {}".format(document_path, "succeeded" if ret_val else "failed"))

    def setPlaybackEnabled(self, value: bool = True):
        self.ui.actReadLine.setEnabled(value)
        self.ui.actReadAll.setEnabled(value)
        self.ui.actReadInterrupt.setEnabled(not value)

    def on_playback_timeout(self):
        if self.runnable and not self.runnable.isRunning():
            self.playback_timer.stop()
            self.setPlaybackEnabled(True)

    @QtCore.Slot()
    def on_actPreferences_triggered(self):
        pref_dialog = DialogPreferences(settings=self.settings, parent=self)

        if pref_dialog.exec_() == QtWidgets.QDialog.Accepted:
            espeak_bin_path = str(self.settings.value(KEY_ESPEAK_PATH))
            espeak_args = str(self.settings.value(KEY_ESPEAK_ARGS))
            if espeak_bin_path:
                espeak_obj = ESpeakNG(espeak_bin_path, espeak_args.split())
                print(espeak_obj)

    @QtCore.Slot(DocumentFragmentDescriptor)
    def on_txeDialogue_readIter(self, dfd):
        initial_char_info = dfd.initial_char_info
        line_generator = ((char_info.get(KEY_ARGS, "").split(), line)
                          for char_info, line
                          in self.ui.txeDialogue.iterBlocks(dfd.block, dfd.block_end, initial_char_info))
        self.processLines(line_generator)

    def on_txeDialogue_readDocument(self):
        line_generator = ((char_info.get(KEY_ARGS, "").split(), line)
                          for char_info, line in self.ui.txeDialogue.iterDocument())
        self.processLines(line_generator)

    @QtCore.Slot()
    def on_actReadInterrupt_triggered(self):
        self.setPlaybackEnabled(True)
        self.logger.debug("Interruption requested")
        if self.thread_pool.activeThreadCount():
            self.runnable.requestInterruption()
            self.statusBar().showMessage("Speech interrupted.", 1000)

    @QtCore.Slot()
    def on_actRecordVoices_triggered(self):
        default_output_path = str(self.settings.value(KEY_OUTPUT_PATH)) or ""
        rec_dialog = DialogRecord(default_output_path, self.document, self)

        if rec_dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.doRecordVoices()

    @QtCore.Slot()
    def on_actFileNew_triggered(self):
        self.document.reset()
        self.setCurrentDocument()

    @QtCore.Slot()
    def on_actFileOpen_triggered(self):
        obo_path, _ = QtWidgets.QFileDialog.getOpenFileName(parent=self, dir=".", filter=FILE_FILTER)
        self.document.document_path = obo_path
        self.setCurrentDocument()
        self.readDocument(self.document)

    @QtCore.Slot()
    def on_actFileSave_triggered(self):
        current_path = self.document.document_path
        if current_path:
            self.writeDocument(self.document)
        else:
            self.on_actFileSaveAs_triggered()
        self.setCurrentDocument(DocumentMode.DOC_WRITE)

    @QtCore.Slot()
    def on_actFileSaveAs_triggered(self):
        new_path, _ = QtWidgets.QFileDialog.getSaveFileName(parent=self, dir=".", filter=FILE_FILTER)
        if new_path:
            self.document.document_path = new_path
            self.writeDocument(self.document)
        self.setCurrentDocument(DocumentMode.DOC_WRITE)

    def processLines(self, value_generator):
        """
        Run text-to-speech program.

        :param value_generator: Generator of (OVERRIDE_ARGS, LINE) pairs.
        """
        espeak_bin_path = str(self.settings.value(KEY_ESPEAK_PATH))
        espeak_args = str(self.settings.value(KEY_ESPEAK_ARGS))
        espeak_obj = ESpeakNG(espeak_bin_path, espeak_args.split())
        espeak_obj.set_value_generator(value_generator)
        self.runnable = Runnable(espeak_obj=espeak_obj)
        self.thread_pool.start(self.runnable)
        self.setPlaybackEnabled(False)
        self.playback_timer.start(PLAYBACK_TIMER_INTERVAL)

    def doRecordVoices(self):
        document = self.document
        name_template = document.output_path_template
        counter = itertools.count(1)
        file_generator = ((char_info.get(KEY_ARGS, "").split() +
                           ["-w", name_template.format(INDEX=next(counter),
                                                       CHAR=char_info.get(KEY_NAME, DEFAULT_CHAR_NAME))],
                           line)
                          for char_info, line in self.ui.txeDialogue.iterDocument())
        self.processLines(file_generator)
