# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Management.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1273, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setMaximumSize(QtCore.QSize(10000, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 8, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout.addWidget(self.comboBox_4, 3, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 7)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 4, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab_3)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(75, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 10, 4, 1, 1)
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_6, 9, 0, 2, 2)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_4.setMaximumSize(QtCore.QSize(1000, 200))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_4, 9, 4, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setMaximumSize(QtCore.QSize(1000, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(75, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 10, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setMaximumSize(QtCore.QSize(1000, 200))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_3, 9, 2, 1, 2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_9.setFont(font)
        self.comboBox_9.setObjectName("comboBox_9")
        self.horizontalLayout.addWidget(self.comboBox_9)
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.comboBox_10 = QtWidgets.QComboBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_10.setFont(font)
        self.comboBox_10.setObjectName("comboBox_10")
        self.horizontalLayout.addWidget(self.comboBox_10)
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout.addWidget(self.label_16)
        self.comboBox_11 = QtWidgets.QComboBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_11.setFont(font)
        self.comboBox_11.setObjectName("comboBox_11")
        self.horizontalLayout.addWidget(self.comboBox_11)
        self.gridLayout_2.addWidget(self.groupBox_4, 1, 0, 1, 4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.horizontalLayout_6.addWidget(self.comboBox_6)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_4.addWidget(self.label_15)
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName("comboBox_7")
        self.horizontalLayout_4.addWidget(self.comboBox_7)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_5.addWidget(self.label_26)
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_8.setFont(font)
        self.comboBox_8.setObjectName("comboBox_8")
        self.horizontalLayout_5.addWidget(self.comboBox_8)
        self.gridLayout_2.addWidget(self.groupBox, 0, 2, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_24 = QtWidgets.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_2.addWidget(self.label_24)
        self.comboBox_18 = QtWidgets.QComboBox(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_18.setFont(font)
        self.comboBox_18.setObjectName("comboBox_18")
        self.horizontalLayout_2.addWidget(self.comboBox_18)
        self.gridLayout_2.addWidget(self.groupBox_7, 0, 3, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_25 = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_3.addWidget(self.label_25)
        self.comboBox_19 = QtWidgets.QComboBox(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_19.setFont(font)
        self.comboBox_19.setObjectName("comboBox_19")
        self.horizontalLayout_3.addWidget(self.comboBox_19)
        self.gridLayout_2.addWidget(self.groupBox_8, 0, 4, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_17 = QtWidgets.QComboBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_17.setFont(font)
        self.comboBox_17.setObjectName("comboBox_17")
        self.verticalLayout_4.addWidget(self.comboBox_17)
        self.gridLayout_2.addWidget(self.groupBox_6, 1, 4, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_5.setMinimumSize(QtCore.QSize(0, 175))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_23 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 0, 5, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 0, 1, 1, 1)
        self.comboBox_12 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_12.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_12.setFont(font)
        self.comboBox_12.setObjectName("comboBox_12")
        self.gridLayout_3.addWidget(self.comboBox_12, 1, 1, 1, 1)
        self.comboBox_16 = QtWidgets.QComboBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_16.setFont(font)
        self.comboBox_16.setObjectName("comboBox_16")
        self.gridLayout_3.addWidget(self.comboBox_16, 1, 5, 1, 1)
        self.comboBox_15 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_15.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_15.setFont(font)
        self.comboBox_15.setObjectName("comboBox_15")
        self.gridLayout_3.addWidget(self.comboBox_15, 1, 8, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 0, 8, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 2, 1, 1, 1)
        self.comboBox_13 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_13.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_13.setFont(font)
        self.comboBox_13.setObjectName("comboBox_13")
        self.gridLayout_3.addWidget(self.comboBox_13, 3, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 2, 5, 1, 1)
        self.comboBox_14 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_14.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_14.setFont(font)
        self.comboBox_14.setObjectName("comboBox_14")
        self.gridLayout_3.addWidget(self.comboBox_14, 3, 5, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_5, 3, 0, 1, 2)
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_9)
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 100000))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_4.addWidget(self.listWidget, 3, 6, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_9)
        self.tableWidget_2.setMaximumSize(QtCore.QSize(16777215, 100000))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_4.addWidget(self.tableWidget_2, 3, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_14 = QtWidgets.QLabel(self.groupBox_9)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.comboBox_5.setFont(font)
        self.comboBox_5.setObjectName("comboBox_5")
        self.verticalLayout.addWidget(self.comboBox_5)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.gridLayout_4.addLayout(self.verticalLayout, 3, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 6, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_9)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 3, 7, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_9, 3, 2, 1, 3)
        self.tabWidget.addTab(self.tab_4, "")
        self.horizontalLayout_7.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Management"))
        self.label_10.setText(_translate("MainWindow", "Administrators"))
        self.pushButton.setText(_translate("MainWindow", "New Password"))
        self.label_4.setText(_translate("MainWindow", "First Name"))
        self.label_5.setText(_translate("MainWindow", "Last Name"))
        self.pushButton_3.setText(_translate("MainWindow", "Remove"))
        self.label_7.setText(_translate("MainWindow", "List of users"))
        self.pushButton_2.setText(_translate("MainWindow", "Validate"))
        self.label_6.setText(_translate("MainWindow", "Tel"))
        self.label_2.setText(_translate("MainWindow", "User Name"))
        self.label.setText(_translate("MainWindow", "Organization"))
        self.label_3.setText(_translate("MainWindow", "E-mail"))
        self.pushButton_5.setText(_translate("MainWindow", "DB transfer"))
        self.label_9.setText(_translate("MainWindow", "Users rights"))
        self.pushButton_4.setText(_translate("MainWindow", "Cancel"))
        self.label_8.setText(_translate("MainWindow", "New or modified or removed uers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "User management"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Create a test means"))
        self.label_18.setText(_translate("MainWindow", "Test means type"))
        self.label_17.setText(_translate("MainWindow", "Test means name"))
        self.label_16.setText(_translate("MainWindow", "Serial number"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Creating a coating"))
        self.label_12.setText(_translate("MainWindow", "Coating name"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Create a detergent"))
        self.label_15.setText(_translate("MainWindow", "Detergent name"))
        self.groupBox.setTitle(_translate("MainWindow", "Insect autorization"))
        self.label_26.setText(_translate("MainWindow", "Insect"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Create a test point type"))
        self.label_24.setText(_translate("MainWindow", "Name of test point type"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Create an intrinsic value"))
        self.label_25.setText(_translate("MainWindow", "Name of an intrinsic value type"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Create teams for A/C &WT tests"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Create an instrumentation"))
        self.label_23.setText(_translate("MainWindow", "Acquisition system"))
        self.label_19.setText(_translate("MainWindow", "Tank reference"))
        self.label_22.setText(_translate("MainWindow", "Camera reference"))
        self.label_21.setText(_translate("MainWindow", "Sensor type"))
        self.label_20.setText(_translate("MainWindow", "Insect ejector reference"))
        self.groupBox_9.setTitle(_translate("MainWindow", "User rights"))
        self.label_14.setText(_translate("MainWindow", "Rights"))
        self.pushButton_8.setText(_translate("MainWindow", "Validate"))
        self.label_11.setText(_translate("MainWindow", "Authorized users"))
        self.label_13.setText(_translate("MainWindow", "Other users"))
        self.pushButton_6.setText(_translate("MainWindow", "DB transfer"))
        self.pushButton_7.setText(_translate("MainWindow", "Cancel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "User\'s allocation"))
