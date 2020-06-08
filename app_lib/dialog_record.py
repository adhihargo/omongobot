import os
import re

from PySide2 import QtCore, QtGui, QtWidgets

from app_lib.forms.ui_dialog_record import Ui_DialogRecord
from app_lib.struct.document_descriptor import DocumentDescriptor

QT_TEMPLATE_REGEXP_STR = r"([A-Za-z0-9_-.]+|\{[A-Z]+\})+"

PY_TEMPLATE_FIELDS_STR = "(?<={)[A-Z]+(?=})"


class DialogRecord(QtWidgets.QDialog):
    def __init__(self, default_output_path: str = "", output_descriptor: DocumentDescriptor = None, parent=None):
        super(DialogRecord, self).__init__(parent=parent)
        self.ui = Ui_DialogRecord()
        self.ui.setupUi(self)

        if os.path.isdir(default_output_path):
            self.ui.lneOutputPath.setPlaceholderText("default: {}".format(default_output_path))

        output_regex = QtCore.QRegExp(QT_TEMPLATE_REGEXP_STR)
        self.checker_regex = re.compile(PY_TEMPLATE_FIELDS_STR)
        self.default_output_path = default_output_path
        self.ui.lneNameTemplate.setValidator(QtGui.QRegExpValidator(output_regex))

        widget: QtWidgets.QToolButton
        self.field_signal_mapper = QtCore.QSignalMapper(self)
        self.field_signal_mapper.mapped[str].connect(self.on_fieldSignalMapper_mapped)
        self.available_field_list = []
        for widget in self.ui.wdgTemplateFields.children():
            if isinstance(widget, QtWidgets.QToolButton):
                widget_text = widget.text()
                widget.clicked.connect(self.field_signal_mapper.map)
                self.field_signal_mapper.setMapping(widget, widget_text)
                self.available_field_list.append(widget_text)

        self.document_descriptor = output_descriptor
        self.ui.lneOutputPath.setText(self.document_descriptor.output_path)
        self.ui.lneNameTemplate.setText(self.document_descriptor.output_name_template)
        self.ui.spbIndexDigits.setValue(self.document_descriptor.index_digits)

        self.ui.btnRecord.setEnabled(False)
        self.ui.lneNameTemplateChecker.setPlaceholderText(u"« invalid template »")

    @property
    def output_path(self):
        return self.ui.lneOutputPath.text() or self.default_output_path

    @property
    def name_template(self):
        return self.ui.lneNameTemplate.text().replace("{INDEX}", "{{INDEX:0{}d}}".format(self.index_digits))

    @property
    def index_digits(self):
        return self.ui.spbIndexDigits.value()

    @QtCore.Slot()
    def on_btnRecord_clicked(self):
        if not self.document_descriptor.output_path:
            self.document_descriptor.output_path = self.default_output_path
        self.accept()

    @QtCore.Slot()
    def on_btnOutputPathBrowse_clicked(self):
        output = QtWidgets.QFileDialog.getExistingDirectory(parent=self)
        if os.path.isdir(output):
            self.ui.lneOutputPath.setText(output)
            self.document_descriptor.output_path = output

    @QtCore.Slot(str)
    def on_lneNameTemplate_textChanged(self, value):
        state, _, _ = self.ui.lneNameTemplate.validator().validate(value, 0)
        acceptable_state = state == QtGui.QValidator.Acceptable
        if acceptable_state:
            found_field_list = self.checker_regex.findall(value)
            if found_field_list:
                map_result = list(map(lambda x: x in self.available_field_list, found_field_list))
                acceptable_state = all(map_result)
        if acceptable_state:
            self.document_descriptor.output_name_template = value
            self.set_template_sample()
        else:
            self.ui.lneNameTemplateChecker.clear()
        self.ui.btnRecord.setEnabled(acceptable_state)

    @QtCore.Slot(int)
    def on_spbIndexDigits_valueChanged(self, value):
        self.document_descriptor.index_digits = value
        self.set_template_sample()

    def set_template_sample(self):
        template = self.document_descriptor.output_path_template
        self.ui.lneNameTemplateChecker.setText(template.format(INDEX=1, CHAR="Char_A"))

    def on_fieldSignalMapper_mapped(self, value):
        self.ui.lneNameTemplate.insert("{" + value + "}")
        self.ui.lneNameTemplate.setFocus()
