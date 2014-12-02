# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created: Tue Dec  2 18:30:37 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(364, 386)
        MainWindow.setMinimumSize(QtCore.QSize(364, 386))
        MainWindow.setMaximumSize(QtCore.QSize(364, 386))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 174, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 174, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(174, 174, 174))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        MainWindow.setPalette(palette)
        MainWindow.setMouseTracking(True)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Chile))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.simulate = QtGui.QPushButton(self.gridLayoutWidget)
        self.simulate.setObjectName("simulate")
        self.gridLayout.addWidget(self.simulate, 5, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setEnabled(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.shifts = QtGui.QSpinBox(self.gridLayoutWidget)
        self.shifts.setMaximum(99999)
        self.shifts.setObjectName("shifts")
        self.horizontalLayout.addWidget(self.shifts)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.results = QtGui.QTextBrowser(self.gridLayoutWidget)
        self.results.setObjectName("results")
        self.gridLayout.addWidget(self.results, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 364, 25))
        self.menubar.setObjectName("menubar")
        self.help = QtGui.QMenu(self.menubar)
        self.help.setObjectName("help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.aboutUs = QtGui.QAction(MainWindow)
        self.aboutUs.setObjectName("aboutUs")
        self.help.addAction(self.aboutUs)
        self.menubar.addAction(self.help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Simulador", None, QtGui.QApplication.UnicodeUTF8))
        self.simulate.setText(QtGui.QApplication.translate("MainWindow", "Simular", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Turnos a contar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Resultados de la Simulación", None, QtGui.QApplication.UnicodeUTF8))
        self.help.setTitle(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutUs.setText(QtGui.QApplication.translate("MainWindow", "Acerca de", None, QtGui.QApplication.UnicodeUTF8))

