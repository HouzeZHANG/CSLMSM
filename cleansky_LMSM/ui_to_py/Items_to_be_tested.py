# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Items_to_be_tested.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(976, 561)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_4.addWidget(self.pushButton_12, 3, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_4.addWidget(self.pushButton_13, 3, 1, 1, 1)
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.groupBox_14.setFont(font)
        self.groupBox_14.setObjectName("groupBox_14")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_14)
        self.gridLayout.setObjectName("gridLayout")
        self.label_22 = QtWidgets.QLabel(self.groupBox_14)
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_14)
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 0, 1, 1, 1)
        self.comboBox_11 = QtWidgets.QComboBox(self.groupBox_14)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.comboBox_11.setFont(font)
        self.comboBox_11.setObjectName("comboBox_11")
        self.gridLayout.addWidget(self.comboBox_11, 1, 0, 1, 1)
        self.comboBox_12 = QtWidgets.QComboBox(self.groupBox_14)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.comboBox_12.setFont(font)
        self.comboBox_12.setObjectName("comboBox_12")
        self.gridLayout.addWidget(self.comboBox_12, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_14, 0, 0, 1, 2)
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_15.setMinimumSize(QtCore.QSize(0, 350))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setObjectName("groupBox_15")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_15)
        self.lineEdit_8.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 1, 2, 1, 1)
        self.comboBox_14 = QtWidgets.QComboBox(self.groupBox_15)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.comboBox_14.setFont(font)
        self.comboBox_14.setObjectName("comboBox_14")
        self.gridLayout_2.addWidget(self.comboBox_14, 1, 0, 1, 1)
        self.comboBox_13 = QtWidgets.QComboBox(self.groupBox_15)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.comboBox_13.setFont(font)
        self.comboBox_13.setObjectName("comboBox_13")
        self.gridLayout_2.addWidget(self.comboBox_13, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_15)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 2, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_15)
        self.label_25.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 0, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox_15)
        self.label_26.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 0, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox_15)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_15)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 3, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_15)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_14.addWidget(self.pushButton_14, 0, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_15)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_14.addWidget(self.pushButton_15, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_14, 3, 3, 1, 1)
        self.tableWidget_4 = QtWidgets.QTableWidget(self.groupBox_15)
        self.tableWidget_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(0)
        self.tableWidget_4.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget_4, 3, 0, 1, 3)
        self.gridLayout_4.addWidget(self.groupBox_15, 1, 0, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_13.setObjectName("groupBox_13")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_13)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_11 = QtWidgets.QLabel(self.groupBox_13)
        self.label_11.setMinimumSize(QtCore.QSize(0, 25))
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_13)
        self.label_10.setMinimumSize(QtCore.QSize(0, 25))
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_13)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 0, 2, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_13)
        self.comboBox_8.setObjectName("comboBox_8")
        self.gridLayout_6.addWidget(self.comboBox_8, 1, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_13)
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout_6.addWidget(self.comboBox_7, 1, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_13)
        self.lineEdit_9.setMaximumSize(QtCore.QSize(400, 16777215))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_6.addWidget(self.lineEdit_9, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_13)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 2, 0, 1, 2)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_13)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.gridLayout_6.addWidget(self.tableWidget_2, 3, 0, 1, 2)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_8.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_13)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_8.addWidget(self.pushButton_8, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_8, 3, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_13, 1, 0, 1, 2)
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_12)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_12)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_12)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 0, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_12)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_5.addWidget(self.comboBox_5, 1, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_12)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_5.addWidget(self.comboBox_6, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_12, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_9.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_9.addWidget(self.pushButton_10, 1, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_10.addWidget(self.lineEdit_6, 2, 5, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_10.addWidget(self.lineEdit, 2, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.gridLayout_10.addWidget(self.label_19, 1, 2, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_10.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout_10.addWidget(self.comboBox_10, 2, 7, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setObjectName("label_18")
        self.gridLayout_10.addWidget(self.label_18, 1, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridLayout_10.addWidget(self.label_21, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")
        self.gridLayout_10.addWidget(self.label_16, 1, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout_10.addWidget(self.label_13, 3, 0, 1, 9)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_10.addWidget(self.lineEdit_5, 2, 4, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_10.addWidget(self.lineEdit_3, 2, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setObjectName("label_14")
        self.gridLayout_10.addWidget(self.label_14, 1, 7, 1, 1)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.gridLayout_10.addWidget(self.tableWidget_3, 4, 0, 1, 9)
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.gridLayout_10.addWidget(self.label_15, 1, 5, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_10.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_10.addLayout(self.gridLayout_12, 0, 7, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_10.addWidget(self.lineEdit_7, 2, 6, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_10.addWidget(self.pushButton_11, 2, 8, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_9.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_9.setObjectName("comboBox_9")
        self.gridLayout_10.addWidget(self.comboBox_9, 2, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setObjectName("label_28")
        self.gridLayout_10.addWidget(self.label_28, 1, 6, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout_10.addWidget(self.label_20, 1, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_10)
        self.gridLayout_9.addWidget(self.groupBox, 0, 0, 1, 2)
        self.verticalLayout_7.addLayout(self.gridLayout_9)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Items to be tested"))
        self.pushButton_12.setText(_translate("MainWindow", "DB transfer"))
        self.pushButton_13.setText(_translate("MainWindow", "Cancel"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Create a coating"))
        self.label_22.setText(_translate("MainWindow", "Type coating"))
        self.label_23.setText(_translate("MainWindow", "Serial number"))
        self.groupBox_15.setTitle(_translate("MainWindow", "List of caractristics for this coating"))
        self.label_24.setText(_translate("MainWindow", "List of caractristics with their unity&value"))
        self.label_25.setText(_translate("MainWindow", "Unity"))
        self.label_26.setText(_translate("MainWindow", "Charactristic"))
        self.label_27.setText(_translate("MainWindow", "Value"))
        self.pushButton.setText(_translate("MainWindow", "Validate"))
        self.pushButton_14.setText(_translate("MainWindow", "download"))
        self.pushButton_15.setText(_translate("MainWindow", "upload"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Coatings"))
        self.pushButton_5.setText(_translate("MainWindow", "DB transfer"))
        self.pushButton_6.setText(_translate("MainWindow", "Cancel"))
        self.groupBox_13.setTitle(_translate("MainWindow", "List of caractristics for this detergent"))
        self.label_11.setText(_translate("MainWindow", "Charactristic"))
        self.label_10.setText(_translate("MainWindow", "Unity"))
        self.label_12.setText(_translate("MainWindow", "Value"))
        self.label_9.setText(_translate("MainWindow", "List of caractristics with their unity&value"))
        self.pushButton_7.setText(_translate("MainWindow", "Search"))
        self.pushButton_8.setText(_translate("MainWindow", "Create"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Create a detergent"))
        self.label_7.setText(_translate("MainWindow", "Detergent name"))
        self.label_8.setText(_translate("MainWindow", "Detergent variant"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Detergents"))
        self.pushButton_9.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_10.setText(_translate("MainWindow", "DB transfer"))
        self.groupBox.setTitle(_translate("MainWindow", "Insects"))
        self.label_19.setText(_translate("MainWindow", "Flight altitude min(m)"))
        self.label_18.setText(_translate("MainWindow", "Flight altitude max(m)"))
        self.label_21.setText(_translate("MainWindow", "Name of insect"))
        self.label_16.setText(_translate("MainWindow", "Length(mm)"))
        self.label_13.setText(_translate("MainWindow", "List of insects"))
        self.label_14.setText(_translate("MainWindow", "Hemolymphe"))
        self.label_15.setText(_translate("MainWindow", "Width"))
        self.pushButton_11.setText(_translate("MainWindow", "Add"))
        self.label_28.setText(_translate("MainWindow", "Thickness(mm)"))
        self.label_20.setText(_translate("MainWindow", "Mass(g)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Insects"))
