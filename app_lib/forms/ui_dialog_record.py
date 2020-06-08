# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_record.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from app_lib.template_line_edit import TemplateLineEdit


class Ui_DialogRecord(object):
    def setupUi(self, DialogRecord):
        if not DialogRecord.objectName():
            DialogRecord.setObjectName(u"DialogRecord")
        DialogRecord.resize(456, 218)
        self.verticalLayout = QVBoxLayout(DialogRecord)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(DialogRecord)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(25, 16777215))

        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)

        self.lneOutputPath = QLineEdit(self.widget_3)
        self.lneOutputPath.setObjectName(u"lneOutputPath")
        self.lneOutputPath.setReadOnly(True)

        self.gridLayout.addWidget(self.lneOutputPath, 0, 1, 1, 1)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.btnOutputPathBrowse = QPushButton(self.widget_3)
        self.btnOutputPathBrowse.setObjectName(u"btnOutputPathBrowse")

        self.gridLayout.addWidget(self.btnOutputPathBrowse, 0, 3, 1, 1)

        self.lneNameTemplateChecker = QLineEdit(self.widget_3)
        self.lneNameTemplateChecker.setObjectName(u"lneNameTemplateChecker")
        self.lneNameTemplateChecker.setReadOnly(True)

        self.gridLayout.addWidget(self.lneNameTemplateChecker, 4, 1, 1, 3)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lneNameTemplate = TemplateLineEdit(self.widget_3)
        self.lneNameTemplate.setObjectName(u"lneNameTemplate")
        self.lneNameTemplate.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lneNameTemplate, 1, 1, 1, 3)

        self.wdgTemplateFields = QWidget(self.widget_3)
        self.wdgTemplateFields.setObjectName(u"wdgTemplateFields")
        self.gridLayout_3 = QGridLayout(self.wdgTemplateFields)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tbtFieldCHAR = QToolButton(self.wdgTemplateFields)
        self.tbtFieldCHAR.setObjectName(u"tbtFieldCHAR")

        self.gridLayout_3.addWidget(self.tbtFieldCHAR, 0, 4, 1, 1)

        self.tbtFieldINDEX = QToolButton(self.wdgTemplateFields)
        self.tbtFieldINDEX.setObjectName(u"tbtFieldINDEX")

        self.gridLayout_3.addWidget(self.tbtFieldINDEX, 0, 1, 1, 1)

        self.spbIndexDigits = QSpinBox(self.wdgTemplateFields)
        self.spbIndexDigits.setObjectName(u"spbIndexDigits")
        self.spbIndexDigits.setMinimum(1)
        self.spbIndexDigits.setMaximum(10)

        self.gridLayout_3.addWidget(self.spbIndexDigits, 1, 1, 1, 1)

        self.label_4 = QLabel(self.wdgTemplateFields)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_6 = QLabel(self.wdgTemplateFields)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.wdgTemplateFields)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.wdgTemplateFields, 2, 1, 1, 3)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(DialogRecord)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer = QSpacerItem(370, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnRecord = QPushButton(self.widget_2)
        self.btnRecord.setObjectName(u"btnRecord")
        self.btnRecord.setMinimumSize(QSize(100, 50))

        self.horizontalLayout.addWidget(self.btnRecord)


        self.verticalLayout.addWidget(self.widget_2)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.lneOutputPath)
        self.label_2.setBuddy(self.lneNameTemplate)
        self.label_4.setBuddy(self.tbtFieldINDEX)
        self.label_6.setBuddy(self.spbIndexDigits)
        self.label_5.setBuddy(self.tbtFieldCHAR)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lneOutputPath, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.btnOutputPathBrowse)
        QWidget.setTabOrder(self.btnOutputPathBrowse, self.lneNameTemplate)
        QWidget.setTabOrder(self.lneNameTemplate, self.lneNameTemplateChecker)
        QWidget.setTabOrder(self.lneNameTemplateChecker, self.btnRecord)
        QWidget.setTabOrder(self.btnRecord, self.tbtFieldINDEX)
        QWidget.setTabOrder(self.tbtFieldINDEX, self.tbtFieldCHAR)

        self.retranslateUi(DialogRecord)

        self.btnRecord.setDefault(True)


        QMetaObject.connectSlotsByName(DialogRecord)
    # setupUi

    def retranslateUi(self, DialogRecord):
        DialogRecord.setWindowTitle(QCoreApplication.translate("DialogRecord", u"Record Voices", None))
        self.pushButton.setText(QCoreApplication.translate("DialogRecord", u"X", None))
        self.label.setText(QCoreApplication.translate("DialogRecord", u"Output &Path:", None))
        self.label_3.setText(QCoreApplication.translate("DialogRecord", u"Checker:", None))
        self.btnOutputPathBrowse.setText(QCoreApplication.translate("DialogRecord", u"&Browse", None))
        self.label_2.setText(QCoreApplication.translate("DialogRecord", u"&Template:", None))
        self.tbtFieldCHAR.setText(QCoreApplication.translate("DialogRecord", u"CHAR", None))
        self.tbtFieldINDEX.setText(QCoreApplication.translate("DialogRecord", u"INDEX", None))
        self.label_4.setText(QCoreApplication.translate("DialogRecord", u"&1. Index of current line:", None))
        self.label_6.setText(QCoreApplication.translate("DialogRecord", u"Index &digits:", None))
        self.label_5.setText(QCoreApplication.translate("DialogRecord", u"&2. Character name:", None))
        self.btnRecord.setText(QCoreApplication.translate("DialogRecord", u"&Record", None))
    # retranslateUi

