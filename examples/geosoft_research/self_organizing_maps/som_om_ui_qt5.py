# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_som_om.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_som_om:
    def setupUi(self, som_om):
        som_om.setObjectName("som_om")
        som_om.resize(438, 777)
        self.layoutWidget = QtWidgets.QWidget(som_om)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 34))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.databaseName = QtWidgets.QLabel(self.layoutWidget)
        self.databaseName.setObjectName("databaseName")
        self.verticalLayout_2.addWidget(self.databaseName)
        self.layoutWidget1 = QtWidgets.QWidget(som_om)
        self.layoutWidget1.setGeometry(QtCore.QRect(332, 47, 101, 461))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.norm = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm.setObjectName("norm")
        self.verticalLayout.addWidget(self.norm)
        self.norm_1 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_1.setObjectName("norm_1")
        self.verticalLayout.addWidget(self.norm_1)
        self.norm_2 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_2.setObjectName("norm_2")
        self.verticalLayout.addWidget(self.norm_2)
        self.norm_3 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_3.setObjectName("norm_3")
        self.verticalLayout.addWidget(self.norm_3)
        self.norm_4 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_4.setObjectName("norm_4")
        self.verticalLayout.addWidget(self.norm_4)
        self.norm_5 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_5.setObjectName("norm_5")
        self.verticalLayout.addWidget(self.norm_5)
        self.norm_6 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_6.setObjectName("norm_6")
        self.verticalLayout.addWidget(self.norm_6)
        self.norm_7 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_7.setObjectName("norm_7")
        self.verticalLayout.addWidget(self.norm_7)
        self.norm_8 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_8.setObjectName("norm_8")
        self.verticalLayout.addWidget(self.norm_8)
        self.norm_9 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_9.setObjectName("norm_9")
        self.verticalLayout.addWidget(self.norm_9)
        self.norm_10 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_10.setObjectName("norm_10")
        self.verticalLayout.addWidget(self.norm_10)
        self.norm_11 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_11.setObjectName("norm_11")
        self.verticalLayout.addWidget(self.norm_11)
        self.norm_12 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_12.setObjectName("norm_12")
        self.verticalLayout.addWidget(self.norm_12)
        self.norm_13 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_13.setObjectName("norm_13")
        self.verticalLayout.addWidget(self.norm_13)
        self.norm_14 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_14.setObjectName("norm_14")
        self.verticalLayout.addWidget(self.norm_14)
        self.norm_15 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_15.setObjectName("norm_15")
        self.verticalLayout.addWidget(self.norm_15)
        self.norm_16 = QtWidgets.QComboBox(self.layoutWidget1)
        self.norm_16.setObjectName("norm_16")
        self.verticalLayout.addWidget(self.norm_16)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.layoutWidget2 = QtWidgets.QWidget(som_om)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 620, 421, 148))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.filtLab = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.filtLab.setFont(font)
        self.filtLab.setObjectName("filtLab")
        self.gridLayout.addWidget(self.filtLab, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.filterChan = QtWidgets.QComboBox(self.layoutWidget2)
        self.filterChan.setEditable(False)
        self.filterChan.setObjectName("filterChan")
        self.gridLayout.addWidget(self.filterChan, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.outClass = QtWidgets.QLineEdit(self.layoutWidget2)
        self.outClass.setObjectName("outClass")
        self.gridLayout.addWidget(self.outClass, 3, 0, 1, 1)
        self.outError = QtWidgets.QLineEdit(self.layoutWidget2)
        self.outError.setObjectName("outError")
        self.gridLayout.addWidget(self.outError, 3, 1, 1, 1)
        self.filterVal = QtWidgets.QLineEdit(self.layoutWidget2)
        self.filterVal.setObjectName("filterVal")
        self.gridLayout.addWidget(self.filterVal, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.classButton = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.classButton.setFont(font)
        self.classButton.setObjectName("classButton")
        self.gridLayout_2.addWidget(self.classButton, 0, 0, 1, 1)
        self.progLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.progLabel.setObjectName("progLabel")
        self.gridLayout_2.addWidget(self.progLabel, 0, 1, 1, 1)
        self.stopButton = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_2.addWidget(self.stopButton, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 1, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.line = QtWidgets.QFrame(som_om)
        self.line.setGeometry(QtCore.QRect(12, 511, 421, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget3 = QtWidgets.QWidget(som_om)
        self.layoutWidget3.setGeometry(QtCore.QRect(14, 57, 311, 450))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.chan_1 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_1.setObjectName("chan_1")
        self.verticalLayout_4.addWidget(self.chan_1)
        self.chan_2 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_2.setObjectName("chan_2")
        self.verticalLayout_4.addWidget(self.chan_2)
        self.chan_3 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_3.setObjectName("chan_3")
        self.verticalLayout_4.addWidget(self.chan_3)
        self.chan_4 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_4.setObjectName("chan_4")
        self.verticalLayout_4.addWidget(self.chan_4)
        self.chan_5 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_5.setObjectName("chan_5")
        self.verticalLayout_4.addWidget(self.chan_5)
        self.chan_6 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_6.setObjectName("chan_6")
        self.verticalLayout_4.addWidget(self.chan_6)
        self.chan_7 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_7.setObjectName("chan_7")
        self.verticalLayout_4.addWidget(self.chan_7)
        self.chan_8 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_8.setObjectName("chan_8")
        self.verticalLayout_4.addWidget(self.chan_8)
        self.chan_9 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_9.setObjectName("chan_9")
        self.verticalLayout_4.addWidget(self.chan_9)
        self.chan_10 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_10.setObjectName("chan_10")
        self.verticalLayout_4.addWidget(self.chan_10)
        self.chan_11 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_11.setObjectName("chan_11")
        self.verticalLayout_4.addWidget(self.chan_11)
        self.chan_12 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_12.setObjectName("chan_12")
        self.verticalLayout_4.addWidget(self.chan_12)
        self.chan_13 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_13.setObjectName("chan_13")
        self.verticalLayout_4.addWidget(self.chan_13)
        self.chan_14 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_14.setObjectName("chan_14")
        self.verticalLayout_4.addWidget(self.chan_14)
        self.chan_15 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_15.setObjectName("chan_15")
        self.verticalLayout_4.addWidget(self.chan_15)
        self.chan_16 = QtWidgets.QComboBox(self.layoutWidget3)
        self.chan_16.setObjectName("chan_16")
        self.verticalLayout_4.addWidget(self.chan_16)
        self.layoutWidget4 = QtWidgets.QWidget(som_om)
        self.layoutWidget4.setGeometry(QtCore.QRect(88, 530, 238, 76))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.similarity = QtWidgets.QLabel(self.layoutWidget4)
        self.similarity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.similarity.setObjectName("similarity")
        self.verticalLayout_7.addWidget(self.similarity)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.similarity_func = QtWidgets.QComboBox(self.layoutWidget4)
        self.similarity_func.setCurrentText("")
        self.similarity_func.setObjectName("similarity_func")
        self.verticalLayout_6.addWidget(self.similarity_func)
        self.nClasses = QtWidgets.QComboBox(self.layoutWidget4)
        self.nClasses.setObjectName("nClasses")
        self.verticalLayout_6.addWidget(self.nClasses)
        self.anomPercent = QtWidgets.QLineEdit(self.layoutWidget4)
        self.anomPercent.setObjectName("anomPercent")
        self.verticalLayout_6.addWidget(self.anomPercent)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.line.raise_()

        self.retranslateUi(som_om)
        self.similarity_func.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(som_om)

    def retranslateUi(self, som_om):
        _translate = QtCore.QCoreApplication.translate
        som_om.setWindowTitle(_translate("som_om", "Self Organizing Classification"))
        self.label_5.setText(_translate("som_om", "Database:"))
        self.databaseName.setText(_translate("som_om", "database name..."))
        self.label_6.setText(_translate("som_om", "normalize"))
        self.filtLab.setText(_translate("som_om", "Filter on:"))
        self.label.setText(_translate("som_om", "Filter value:"))
        self.label_3.setText(_translate("som_om", "Save classification to:"))
        self.label_4.setText(_translate("som_om", "Save fit to:"))
        self.classButton.setText(_translate("som_om", "Classify"))
        self.progLabel.setText(_translate("som_om", "..."))
        self.stopButton.setText(_translate("som_om", "Stop"))
        self.label_2.setText(_translate("som_om", "Analyse data:"))
        self.similarity.setText(_translate("som_om", "Similarity function"))
        self.label_7.setText(_translate("som_om", "Base classes"))
        self.label_8.setText(_translate("som_om", "Anomalous %"))
        self.similarity_func.setToolTip(_translate("som_om", "Method to determine similarity"))
        self.nClasses.setToolTip(_translate("som_om", "Number of base classes"))

