# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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

from app_lib.text_edit_dialogue import TextEditDialogue
from app_lib.character_table_view import CharacterTableView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(460, 619)
        self.actQuit = QAction(MainWindow)
        self.actQuit.setObjectName(u"actQuit")
        self.actPreferences = QAction(MainWindow)
        self.actPreferences.setObjectName(u"actPreferences")
        self.actFileOpen = QAction(MainWindow)
        self.actFileOpen.setObjectName(u"actFileOpen")
        self.actFileSave = QAction(MainWindow)
        self.actFileSave.setObjectName(u"actFileSave")
        self.actReadLine = QAction(MainWindow)
        self.actReadLine.setObjectName(u"actReadLine")
        self.actReadAll = QAction(MainWindow)
        self.actReadAll.setObjectName(u"actReadAll")
        self.actReadInterrupt = QAction(MainWindow)
        self.actReadInterrupt.setObjectName(u"actReadInterrupt")
        self.actFileNew = QAction(MainWindow)
        self.actFileNew.setObjectName(u"actFileNew")
        self.actRecordVoices = QAction(MainWindow)
        self.actRecordVoices.setObjectName(u"actRecordVoices")
        self.actFileSaveAs = QAction(MainWindow)
        self.actFileSaveAs.setObjectName(u"actFileSaveAs")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"Arial")
        self.centralwidget.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.tbvCharacters = CharacterTableView(self.widget)
        self.tbvCharacters.setObjectName(u"tbvCharacters")

        self.verticalLayout.addWidget(self.tbvCharacters)

        self.splitter.addWidget(self.widget)
        self.widget_2 = QWidget(self.splitter)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.txeDialogue = TextEditDialogue(self.widget_2)
        self.txeDialogue.setObjectName(u"txeDialogue")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.txeDialogue.setFont(font1)

        self.verticalLayout_2.addWidget(self.txeDialogue)

        self.splitter.addWidget(self.widget_2)

        self.verticalLayout_3.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 460, 21))
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Edit = QMenu(self.menubar)
        self.menu_Edit.setObjectName(u"menu_Edit")
        self.menu_Voice = QMenu(self.menubar)
        self.menu_Voice.setObjectName(u"menu_Voice")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.tbvCharacters)
        self.label_2.setBuddy(self.txeDialogue)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Voice.menuAction())
        self.menu_File.addAction(self.actFileNew)
        self.menu_File.addAction(self.actFileOpen)
        self.menu_File.addAction(self.actFileSave)
        self.menu_File.addAction(self.actFileSaveAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actQuit)
        self.menu_Edit.addAction(self.actPreferences)
        self.menu_Voice.addAction(self.actReadAll)
        self.menu_Voice.addAction(self.actReadLine)
        self.menu_Voice.addAction(self.actReadInterrupt)
        self.menu_Voice.addSeparator()
        self.menu_Voice.addAction(self.actRecordVoices)

        self.retranslateUi(MainWindow)
        self.actQuit.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actQuit.setText(QCoreApplication.translate("MainWindow", u"&Quit", None))
#if QT_CONFIG(shortcut)
        self.actQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actPreferences.setText(QCoreApplication.translate("MainWindow", u"&Preferences", None))
        self.actFileOpen.setText(QCoreApplication.translate("MainWindow", u"&Open", None))
#if QT_CONFIG(shortcut)
        self.actFileOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actFileSave.setText(QCoreApplication.translate("MainWindow", u"&Save", None))
#if QT_CONFIG(shortcut)
        self.actFileSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actReadLine.setText(QCoreApplication.translate("MainWindow", u"Read Lin&e", None))
#if QT_CONFIG(shortcut)
        self.actReadLine.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Return", None))
#endif // QT_CONFIG(shortcut)
        self.actReadAll.setText(QCoreApplication.translate("MainWindow", u"Read &All", None))
#if QT_CONFIG(shortcut)
        self.actReadAll.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actReadInterrupt.setText(QCoreApplication.translate("MainWindow", u"Inte&rrupt", None))
#if QT_CONFIG(shortcut)
        self.actReadInterrupt.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.actFileNew.setText(QCoreApplication.translate("MainWindow", u"&New", None))
#if QT_CONFIG(shortcut)
        self.actFileNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actRecordVoices.setText(QCoreApplication.translate("MainWindow", u"Record &Voices", None))
#if QT_CONFIG(shortcut)
        self.actRecordVoices.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actFileSaveAs.setText(QCoreApplication.translate("MainWindow", u"S&ave As", None))
#if QT_CONFIG(shortcut)
        self.actFileSaveAs.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"&1. Character List:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"&2. Lines:", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menu_Edit.setTitle(QCoreApplication.translate("MainWindow", u"&Edit", None))
        self.menu_Voice.setTitle(QCoreApplication.translate("MainWindow", u"&Voice", None))
    # retranslateUi

