# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_preferences.ui'
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


class Ui_DialogPreferences(object):
    def setupUi(self, DialogPreferences):
        if not DialogPreferences.objectName():
            DialogPreferences.setObjectName(u"DialogPreferences")
        DialogPreferences.resize(476, 221)
        self.verticalLayout = QVBoxLayout(DialogPreferences)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(DialogPreferences)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnEspeakPathBrowse = QPushButton(self.groupBox)
        self.btnEspeakPathBrowse.setObjectName(u"btnEspeakPathBrowse")

        self.gridLayout.addWidget(self.btnEspeakPathBrowse, 0, 3, 1, 1)

        self.lneEspeakPath = QLineEdit(self.groupBox)
        self.lneEspeakPath.setObjectName(u"lneEspeakPath")
        self.lneEspeakPath.setReadOnly(True)

        self.gridLayout.addWidget(self.lneEspeakPath, 0, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lneEspeakArgs = QLineEdit(self.groupBox)
        self.lneEspeakArgs.setObjectName(u"lneEspeakArgs")

        self.gridLayout.addWidget(self.lneEspeakArgs, 1, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.btnEspeakTest = QPushButton(self.groupBox)
        self.btnEspeakTest.setObjectName(u"btnEspeakTest")

        self.gridLayout.addWidget(self.btnEspeakTest, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(DialogPreferences)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lneDefaultOutputPath = QLineEdit(self.groupBox_2)
        self.lneDefaultOutputPath.setObjectName(u"lneDefaultOutputPath")

        self.horizontalLayout.addWidget(self.lneDefaultOutputPath)

        self.btnDefaultOutputPathBrowse = QPushButton(self.groupBox_2)
        self.btnDefaultOutputPathBrowse.setObjectName(u"btnDefaultOutputPathBrowse")

        self.horizontalLayout.addWidget(self.btnDefaultOutputPathBrowse)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.widget_2 = QWidget(DialogPreferences)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(349, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnSave = QPushButton(self.widget_2)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(100, 50))

        self.horizontalLayout_2.addWidget(self.btnSave)


        self.verticalLayout.addWidget(self.widget_2)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.lneEspeakPath)
        self.label_2.setBuddy(self.lneEspeakArgs)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(DialogPreferences)

        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(DialogPreferences)
    # setupUi

    def retranslateUi(self, DialogPreferences):
        DialogPreferences.setWindowTitle(QCoreApplication.translate("DialogPreferences", u"Preferences", None))
        self.groupBox.setTitle(QCoreApplication.translate("DialogPreferences", u"eSpeak NG", None))
        self.btnEspeakPathBrowse.setText(QCoreApplication.translate("DialogPreferences", u"&Browse", None))
        self.label.setText(QCoreApplication.translate("DialogPreferences", u"&Path:", None))
        self.label_2.setText(QCoreApplication.translate("DialogPreferences", u"&Args:", None))
        self.btnEspeakTest.setText(QCoreApplication.translate("DialogPreferences", u"&Test", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DialogPreferences", u"Defaults", None))
        self.label_3.setText(QCoreApplication.translate("DialogPreferences", u"Output Path:", None))
        self.btnDefaultOutputPathBrowse.setText(QCoreApplication.translate("DialogPreferences", u"B&rowse", None))
        self.btnSave.setText(QCoreApplication.translate("DialogPreferences", u"&Save", None))
    # retranslateUi

