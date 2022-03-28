from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import psycopg2
import sys
import os
sys.path.append('..\\QT\\class')
import csv
import pandas as pd
import numpy as np
import testmean
from testmean import *
from copy import deepcopy
class testMean(QWidget) :
    def __init__(self, parent, uname, lst) :
        super(testMean, self).__init__(parent)
        self.connect()
        self.uname = uname
        if 'manager' in [i[0] for i in lst] :
            self.lst = lst
        else :
            self.lst = [[i[0], i[2]] for i in lst if i[1] == "test mean"]
        self.setupUI()
    
    def setupUI(self) :
        ######################################################################################
        #                                 Create test mean                                   #
        ######################################################################################
        splitter = QSplitter(Qt.Vertical, self)
        label1 = QLabel('Test means identification')
        frame1 = QFrame()
        hlayout = QHBoxLayout()
        ##################################################################
        #                       test mean type                           #
        ##################################################################
        splitter1 = QSplitter(Qt.Vertical)
        label = QLabel('Test means type')
        self.test_mean_type = QComboBox()
        edit = QLineEdit()
        test_mean_type = []
        if 'manager' in [i[0] for i in self.lst] :
            sql = """SELECT DISTINCT type FROM test_mean;"""
            self.cur.execute(sql)
            self.conn.commit()
            rows = self.cur.fetchall()
            for row in rows :
                test_mean_type.append(row[0])
        else :
            for i in self.lst :
                if i[1].split('_')[0] not in test_mean_type :
                    test_mean_type.append(i[1].split('_')[0])
        self.test_mean_type.clear()
        self.test_mean_type.setLineEdit(edit)
        self.test_mean_type.addItems(test_mean_type)
        self.test_mean_type.setCurrentText('')
        self.test_mean_type.installEventFilter(self)
        splitter1.addWidget(label)
        splitter1.addWidget(self.test_mean_type)
        hlayout.addWidget(splitter1)
        ##################################################################
        #                       test mean name                           #
        ##################################################################
        splitter2 = QSplitter(Qt.Vertical)
        label = QLabel('Test means name')
        self.test_mean_name = QComboBox()
        edit = QLineEdit()
        self.test_mean_name.setLineEdit(edit)
        self.test_mean_name.installEventFilter(self)
        splitter2.addWidget(label)
        splitter2.addWidget(self.test_mean_name)
        hlayout.addWidget(splitter2)
        ####################################################################
        #                       test mean number                           #
        ####################################################################
        splitter3 = QSplitter(Qt.Vertical)
        label = QLabel('Serial number')
        self.test_mean_num = QComboBox()
        edit = QLineEdit()
        self.test_mean_num.setLineEdit(edit)
        self.test_mean_num.installEventFilter(self)
        splitter3.addWidget(label)
        splitter3.addWidget(self.test_mean_num)
        hlayout.addWidget(splitter3)

        frame1.setLayout(hlayout)
        frame1.setFrameStyle(1)
        splitter.addWidget(label1)
        splitter.addWidget(frame1)
        splitter.setGeometry(10, 10, 400, 80)

        ######################################################################################
        #                          Create attributs for test mean                            #
        ######################################################################################
        splitter = QSplitter(Qt.Vertical, self)
        label1 = QLabel('List of attributes for this test means')
        frame1 = QFrame()
        ######################################################################################
        #                                    Button search                                   #
        ######################################################################################
        self.search_att_btn = QPushButton('Search', frame1)
        self.search_att_btn.setGeometry(200, 0, 120, 20)        

        ##################################################################
        #                           Attribute                            #
        ##################################################################
        splitter1 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Attribute')
        self.attribute = QComboBox()
        edit = QLineEdit()        
        self.attribute.setLineEdit(edit)
        self.attribute.setCurrentText('')
        self.attribute.installEventFilter(self)
        splitter1.addWidget(label)
        splitter1.addWidget(self.attribute)
        splitter1.setGeometry(10, 30, 150, 40)
        ##################################################################
        #                        Unity of attribut                       #
        ##################################################################
        splitter2 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Unity')
        self.att_unity = QComboBox()
        edit = QLineEdit()
        self.att_unity.setLineEdit(edit)
        self.att_unity.installEventFilter(self)
        splitter2.addWidget(label)
        splitter2.addWidget(self.att_unity)
        splitter2.setGeometry(170, 30, 90, 40)
        ####################################################################
        #                        value of attribut                         #
        ####################################################################
        splitter3 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Value')
        self.att_value = QLineEdit()
        self.att_value.installEventFilter(self)
        splitter3.addWidget(label)
        splitter3.addWidget(self.att_value)
        splitter3.setGeometry(270, 30, 120, 40)
        #####################################################################
        #                       create attribut button                      #
        #####################################################################
        self.att_create_btn = QPushButton('Create', frame1)
        self.att_create_btn.setGeometry(140, 80, 120, 20)
        #####################################################################
        #                         list of attributes                        #
        #####################################################################
        splitter4 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('List of attributes with their value')
        self.model_attribute = self.createAttributeModel(self)
        self.list_attribute_tree = QTreeView(frame1)
        self.list_attribute_tree.setModel(self.model_attribute)
        self.list_attribute_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(3) :
            self.list_attribute_tree.setColumnWidth(i, 380 / 3)
        splitter4.addWidget(label)
        splitter4.addWidget(self.list_attribute_tree)
        splitter4.setGeometry(10, 100, 380, 270)
        frame1.setFrameStyle(1)
        splitter.addWidget(label1)
        splitter.addWidget(frame1)
        splitter.setGeometry(10, 100, 400, 400)

        #########################################################################
        #                    Create parameters for AC/ WT                       #
        #########################################################################
        splitter = QSplitter(Qt.Vertical, self)
        label1 = QLabel('List of test parameters acquiring during the test')
        frame1 = QFrame()
        #########################################################################
        #######                 List view of parameters                   #######
        #########################################################################
        splitter1 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('List of flight/WT parameters')
        self.model_param = self.createParamModel(self)
        self.list_param_tree = QTreeView()
        self.list_param_tree.setModel(self.model_param)
        self.list_param_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(2) :
            self.list_param_tree.setColumnWidth(i, 310 / 2)
        splitter1.addWidget(label)
        splitter1.addWidget(self.list_param_tree)
        splitter1.setGeometry(10, 10, 320, 510)

        ############################################################################
        #############           Search parameter button               ##############
        ############################################################################
        self.search_param_btn = QPushButton('Search', frame1)
        self.search_param_btn.setGeometry(340, 10, 120, 20)
        ############################################################################
        #############                   Parameters                    ##############
        ############################################################################
        splitter2 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Parameters')
        self.param = QComboBox()
        edit = QLineEdit()
        self.param.setLineEdit(edit)
        self.param.installEventFilter(self)
        splitter2.addWidget(label)
        splitter2.addWidget(self.param)
        splitter2.setGeometry(340, 50, 120, 40)
        ##############################################################################
        #############               Unity of Paramters                ################
        ############################################################################## 
        splitter2 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Unity')
        self.param_unity = QComboBox()
        edit = QLineEdit()
        self.param_unity.setLineEdit(edit)
        self.param_unity.installEventFilter(self)
        splitter2.addWidget(label)
        splitter2.addWidget(self.param_unity)
        splitter2.setGeometry(340, 110, 120, 40)
        ##############################################################################
        #############               Create Param Button                ###############
        ############################################################################## 
        self.param_create_btn = QPushButton('Create', frame1)
        self.param_create_btn.setGeometry(340, 170, 120, 20)
        ################################################################################
        ################################################################################
        frame1.setFrameStyle(1)
        splitter.addWidget(label1)
        splitter.addWidget(frame1)
        splitter.setGeometry(420, 10, 470, 550)
        #################################################################################
        #################################################################################
        self.cancel_btn = QPushButton('Cancel')
        self.save_btn = QPushButton('Save')
        self.transfer_btn = QPushButton('DB transfer')
        frame1 = QFrame(self)
        hlayout = QHBoxLayout()
        hlayout.addWidget(self.cancel_btn)
        hlayout.addWidget(self.save_btn)
        hlayout.addWidget(self.transfer_btn)
        frame1.setFrameStyle(1)
        frame1.setLayout(hlayout)
        frame1.setGeometry(10, 520, 400, 40)
        ###################################################################################
        ##########                    Function of each button                    ##########
        ###################################################################################
        self.att_create_btn.clicked.connect(self.createAttribute)
        self.param_create_btn.clicked.connect(self.createParam)
        self.list_attribute_tree.doubleClicked.connect(self.delAttribute)
        self.list_param_tree.doubleClicked.connect(self.delParam)
        self.list_attribute_tree.clicked.connect(self.viewAttribute)
        self.list_param_tree.clicked.connect(self.viewParam)
        self.transfer_btn.clicked.connect(self.transfer)

        self.search_att_btn.clicked.connect(self.searchAtt)
        self.save_btn.clicked.connect(self.save)
        self.search_param_btn.clicked.connect(self.searchParam)
        self.cancel_btn.clicked.connect(self.cancel)

    def cancel(self) :
        test_mean_type = self.test_mean_type.currentText()
        test_mean_name = self.test_mean_name.currentText()
        test_mean_num = self.test_mean_num.currentText()
        self.model_attribute.removeRows(0, self.model_attribute.rowCount())
        self.model_param.removeRows(0, self.model_param.rowCount())
        if not test_mean_type.isspace() and test_mean_type != '' and not test_mean_name.isspace() and test_mean_name != '' and not test_mean_num.isspace() and test_mean_num != '' :
            testmean = '_'.join([test_mean_type, test_mean_name, test_mean_num])
            self.initAttParam(testmean)

            sql = """SELECT att.attribute, att.unity, att.value
                                FROM attribute att 
                                    JOIN attribute_test_mean att_tm ON att.id = att_tm.id_attribute
                                    JOIN test_mean tm ON tm.id = att_tm.id_test_mean
                                WHERE tm.type = %s AND tm.name =  %s AND tm.number = %s;
                        """
            self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num))
            self.conn.commit()

            rows = self.cur.fetchall()
            
            self.model_attribute.removeRows(0, self.model_attribute.rowCount())

            for row in rows :
                self.addAttribute(*(row[0:])) 
            
            self.model_param.removeRows(0, self.model_param.rowCount())
            sql = """SELECT tp.name, tp.unity
                    FROM type_param tp 
                        JOIN type_param_test_mean tp_tm ON tp.id = tp_tm.id_type_param
                        JOIN test_mean tm ON tm.id = tp_tm.id_test_mean
                    WHERE tm.type = %s AND tm.name =  %s AND tm.number = %s;
            """
            self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num))
            self.conn.commit()

            rows = self.cur.fetchall()
            for row in rows :
                self.addParam(*(row[0:]))


    def searchParam(self) :
        test_mean_type = self.test_mean_type.currentText()
        test_mean_name = self.test_mean_name.currentText()
        test_mean_num = self.test_mean_num.currentText()

        if not test_mean_type.isspace() and test_mean_type != '' and not test_mean_name.isspace() and test_mean_name != '' and not test_mean_num.isspace() and test_mean_num != '' :
            file_name = '_'.join([test_mean_type, test_mean_name, test_mean_num])
            fname = QFileDialog.getOpenFileName(self, 'Open file', 
            f'.\\file\\test_mean\\{file_name}_param',"CSV data files (*.csv *.xlsx)")

            with open(fname[0], 'r') as f :
                try :
                    rows = csv.reader(f)
                    self.model_param.removeRows(0, self.model_param.rowCount())
                    for row in rows :
                        self.addParam(*row) 
                        self.param_create.addParam(*row)
                finally :
                    f.close()
        else :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Test mean is not identified\nIdentify which test mean")
            msg.setWindowTitle("Error Identify")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

    def searchAtt(self) :
        test_mean_type = self.test_mean_type.currentText()
        test_mean_name = self.test_mean_name.currentText()
        test_mean_num = self.test_mean_num.currentText()

        if not test_mean_type.isspace() and test_mean_type != '' and not test_mean_name.isspace() and test_mean_name != '' and not test_mean_num.isspace() and test_mean_num != '' :
            file_name = '_'.join([test_mean_type, test_mean_name, test_mean_num])
            fname = QFileDialog.getOpenFileName(self, 'Open file', 
            f'.\\file\\test_mean\\{file_name}_att',"CSV data files (*.csv *.xlsx)")

            with open(fname[0], 'r') as f :
                try :
                    rows = csv.reader(f)
                    self.model_attribute.removeRows(0, self.model_attribute.rowCount())
                    for row in rows :
                        self.addAttribute(*row) 
                        self.att_create.addAtt(*row)
                finally :
                    f.close()
        else :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Test mean is not identified\nIdentify which test mean")
            msg.setWindowTitle("Error Identify")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        

    def viewAttribute(self) :
        if self.list_attribute_tree.selectedIndexes()[0] :
            select_row = self.list_attribute_tree.selectedIndexes()[0].row()
            att = self.model_attribute.data(self.model_attribute.index(select_row, 0))
            unity = self.model_attribute.data(self.model_attribute.index(select_row, 1))
            value = self.model_attribute.data(self.model_attribute.index(select_row, 2))
            self.attribute.setCurrentText(att)
            self.att_unity.setCurrentText(unity)
            self.att_value.setText(str(value))

    def viewParam(self) : 
        if self.list_param_tree.selectedIndexes()[0] :
            select_row = self.list_param_tree.selectedIndexes()[0].row()
            param = self.model_param.data(self.model_param.index(select_row, 0))
            unity = self.model_param.data(self.model_param.index(select_row, 1))
            self.param.setCurrentText(param)
            self.param_unity.setCurrentText(unity)

    def createAttributeModel(self, parent) :
        model = QStandardItemModel(0, 3, parent)
        model.setHeaderData(0, Qt.Horizontal, 'Attribute')
        model.setHeaderData(1, Qt.Horizontal, 'Value')
        model.setHeaderData(2, Qt.Horizontal, 'Unity')
        return model

    def createAttribute(self) :
        test_mean_type = self.test_mean_type.currentText()
        test_mean_name = self.test_mean_name.currentText()
        test_mean_num = self.test_mean_num.currentText()
        att = self.attribute.currentText()
        unity = self.att_unity.currentText()
        value = self.att_value.text()
        if not att.isspace() and att != '' and not value.isspace() and value != '' :
            if not test_mean_type.isspace() and test_mean_type != '' and not test_mean_name.isspace() and test_mean_name != '' and not test_mean_num.isspace() and test_mean_num != '' :
                self.addAttribute(att, unity, value)
                self.att_create.addAtt(att, unity, value)
            else :
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Test mean is not identified\nIdentify which test mean")
                msg.setWindowTitle("Error Identify")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return

    def createParamModel(self, parent) :
        model = QStandardItemModel(0, 2, parent)
        model.setHeaderData(0, Qt.Horizontal, 'Parameter')
        model.setHeaderData(1, Qt.Horizontal, 'Unity')
        return model

    def createParam(self) :
        test_mean_type = self.test_mean_type.currentText()
        test_mean_name = self.test_mean_name.currentText()
        test_mean_num = self.test_mean_num.currentText()
        param = self.param.currentText()
        unity = self.param_unity.currentText()
        if not param.isspace() and param != '' and not unity.isspace() and unity != '' :
            if not test_mean_type.isspace() and test_mean_type != '' and not test_mean_name.isspace() and test_mean_name != '' and not test_mean_num.isspace() and test_mean_num != '' :
                self.addParam(param, unity)
                self.param_create.addParam(param, unity)
            else :
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Test mean is not identified\nIdentify which test mean")
                msg.setWindowTitle("Error Identify")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return

    def addAttribute(self, att, unity, value) :
        self.model_attribute.insertRow(self.model_attribute.rowCount())
        row = self.model_attribute.rowCount() - 1
        self.model_attribute.setData(self.model_attribute.index(row, 0), att)
        self.model_attribute.setData(self.model_attribute.index(row, 1), unity)
        self.model_attribute.setData(self.model_attribute.index(row, 2), value)
        
    def addParam(self, name, unity) : 
        self.model_param.insertRow(self.model_param.rowCount())
        row = self.model_param.rowCount() - 1
        self.model_param.setData(self.model_param.index(row, 0), name)
        self.model_param.setData(self.model_param.index(row, 1), unity)

    def delAttribute(self) :
        test_mean_type = self.test_mean_type.currentText()
        test_mean_name = self.test_mean_name.currentText()
        test_mean_num = self.test_mean_num.currentText()
        if  (test_mean_type.isspace() or test_mean_type == '') or  (test_mean_name.isspace() or test_mean_name == '')  or  (test_mean_num.isspace() and test_mean_num == '') :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Test mean is not identified\nIdentify which test mean")
            msg.setWindowTitle("Error Identify")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        select_att = self.list_attribute_tree.selectedIndexes()[0].row()
        att = self.model_attribute.data(self.model_attribute.index(select_att, 0))
        unity = self.model_attribute.data(self.model_attribute.index(select_att, 1))
        value = self.model_attribute.data(self.model_attribute.index(select_att, 2))
        self.model_attribute.removeRow(select_att)
        if self.att_current.findAtt(att, unity, value) is not None:
            self.att_delete.addAtt(att, unity, value)
            self.att_update.delAtt(att, unity, value)
        if self.att_create.findAtt(att, unity, value) is not None:
            self.att_create.delAtt(att, unity, value)
    
    def delParam(self) :
        test_mean_type = self.test_mean_type.currentText()
        test_mean_name = self.test_mean_name.currentText()
        test_mean_num = self.test_mean_num.currentText()
        if  (test_mean_type.isspace() or test_mean_type == '') or  (test_mean_name.isspace() or test_mean_name == '')  or  (test_mean_num.isspace() and test_mean_num == '') :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Test mean is not identified\nIdentify which test mean")
            msg.setWindowTitle("Error Identify")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        select_param = self.list_param_tree.selectedIndexes()[0].row()
        param = self.model_param.data(self.model_param.index(select_param, 0))
        unity = self.model_param.data(self.model_param.index(select_param, 1))
        self.model_param.removeRow(select_param)
        if self.param_current.findParam(param, unity) is not None:
            self.param_delete.addParam(param, unity)
            self.param_update.delParam(param, unity)
        if self.param_create.findParam(param, unity) is not None:
            self.param_create.delParam(param, unity)
    def eventFilter(self, obj, event) :
        ######################################
        # Event on Combobox of Type of AC/WT #
        ######################################
        if obj == self.test_mean_type : 
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                test_mean_type = []
                if 'manager' in [i[0] for i in self.lst] :
                    sql = """SELECT DISTINCT type FROM test_mean;"""
                    self.cur.execute(sql)
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    for row in rows :
                        test_mean_type.append(row[0])
                else :
                    sql = """SELECT ur.role, CASE WHEN ur.id_test_mean IS NOT NULL THEN CONCAT('test mean' ,'-', tm.type, '_', tm.name, '_', tm.number)
                                                  WHEN ur.id_type_coating IS NOT NULL THEN CONCAT('coating', '-', tc.ref)
                                                  WHEN ur.id_type_detergent IS NOT NULL THEN CONCAT('detergent', '-', td.ref)
                                                  WHEN ur.id_type_tank IS NOT NULL THEN CONCAT('tank', '-', tt.ref)
                                                  WHEN ur.id_type_sensor IS NOT NULL THEN CONCAT('sensor', '-',ts.ref)
                                                  WHEN ur.id_type_ejector IS NOT NULL THEN CONCAT('ejector', '-',te.ref)
                                                  WHEN ur.id_type_camera IS NOT NULL THEN CONCAT('camera', '-',tca.ref)
                                                  WHEN ur.id_type_test_point IS NOT NULL THEN CONCAT('test point', '-',ttp.ref)
                                                  WHEN id_type_intrinsic_value IS NOT NULL THEN CONCAT('intrinsic value', '-',tiv.ref) END AS object
                             FROM account ac
                             JOIN user_right ur ON ur.id_account = ac.id
                             LEFT JOIN test_mean tm ON tm.id = ur.id_test_mean
                             LEFT JOIN type_coating tc ON tc.id = ur.id_type_coating
                             LEFT JOIN type_detergent td ON td.id = ur.id_type_detergent
                             LEFT JOIN type_tank tt ON tt.id = ur.id_type_tank
                             LEFT JOIN type_sensor ts ON ts.id = ur.id_type_sensor
                             LEFT JOIN type_ejector te ON te.id = ur.id_type_ejector
                             LEFT JOIN type_camera tca ON tca.id = ur.id_type_camera
                             LEFT JOIN type_test_point ttp ON ttp.id = ur.id_type_test_point
                             LEFT JOIN type_intrinsic_value tiv ON tiv.id = ur.id_type_intrinsic_value
                             WHERE ac.uname = %s ;
                        """
                    self.cur.execute(sql, (self.uname,))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    self.lst = []
                    for row in rows :
                        l = [row[0]]
                        if row[1] is not None :
                            for i in row[1].split('-') :
                                l.append(i)
                        self.lst.append(l)
                    self.lst = [[i[0], i[2]] for i in self.lst if i[1] == "test mean"]
                    for i in self.lst :
                        if i[1].split('_')[0] not in test_mean_type :
                            test_mean_type.append(i[1].split('_')[0])
                self.test_mean_type.clear()
                self.test_mean_type.addItems(test_mean_type)
                self.test_mean_type.showPopup()
                self.test_mean_type.view().viewport().installEventFilter(self)
                return True        
            if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab :    
                gen = self.test_mean_type.currentText()
                if not gen.isspace() and gen != '' :
                    test_mean_name = []
                    if 'manager' in [i[0] for i in self.lst] :
                        sql = """SELECT DISTINCT name FROM test_mean WHERE type = %s;"""
                        self.cur.execute(sql, (gen,))
                        self.conn.commit()
                        rows = self.cur.fetchall()
                        for row in rows :
                            test_mean_name.append(row[0])
                    else :
                        for i in self.lst :
                            if i[1].split('_')[0] == gen and i[1].split('_')[1] not in test_mean_name :
                                test_mean_name.append(i[1].split('_')[1])
                    if gen not in [self.test_mean_type.itemText(i) for i in range(self.test_mean_type.count())] :
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Test mean is not existed or you are not allowed to modify this test mean")
                        msg.setWindowTitle("Error Identify")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()
                        self.test_mean_type.setFocus()
                    else :
                        self.test_mean_name.clear()
                        self.test_mean_name.addItems(test_mean_name)

                        sql = """SELECT DISTINCT att.attribute 
                                FROM attribute att 
                                    JOIN attribute_test_mean att_tm ON att.id = att_tm.id_attribute
                                    JOIN test_mean tm ON tm.id = att_tm.id_test_mean
                                WHERE tm.type = %s;        
                        """
                        self.cur.execute(sql, (gen, ))
                        self.conn.commit()
                        rows = self.cur.fetchall()
                        att = []
                        for row in rows :
                            att.append(row[0])
                        self.attribute.clear()
                        self.attribute.addItems(att)

                        sql = """SELECT DISTINCT tp.name
                                FROM type_param tp 
                                    JOIN type_param_test_mean tp_tm ON tp.id = tp_tm.id_type_param
                                    JOIN test_mean tm ON tm.id = tp_tm.id_test_mean
                                WHERE tm.type = %s;
                        """
                        self.cur.execute(sql, (gen, ))
                        self.conn.commit()
                        rows = self.cur.fetchall()
                        param = []
                        for row in rows :
                            param.append(row[0])
                        self.param.clear()
                        self.param.addItems(param)
                        self.test_mean_name.setFocus()
                        self.attribute.setCurrentText('')
                        self.param.setCurrentText('')
                return True
            return False
    
        if obj == self.test_mean_type.view().viewport() :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                index = self.test_mean_type.view().currentIndex().row()
                gen = self.test_mean_type.itemText(index)
                test_mean_name = []
                if 'manager' in [i[0] for i in self.lst] :
                        sql = """SELECT DISTINCT name FROM test_mean WHERE type = %s;"""
                        self.cur.execute(sql, (gen,))
                        self.conn.commit()
                        rows = self.cur.fetchall()
                        for row in rows :
                            test_mean_name.append(row[0])
                else :
                    for i in self.lst :
                        if i[1].split('_')[0] == gen and i[1].split('_')[1] not in test_mean_name :
                            test_mean_name.append(i[1].split('_')[1])
                self.test_mean_name.clear()
                self.test_mean_name.addItems(test_mean_name)

                sql = """SELECT DISTINCT att.attribute 
                            FROM attribute att 
                            JOIN attribute_test_mean att_tm ON att.id = att_tm.id_attribute
                            JOIN test_mean tm ON tm.id = att_tm.id_test_mean
                            WHERE tm.type = %s;        
                """
                self.cur.execute(sql, (gen, ))
                self.conn.commit()
                rows = self.cur.fetchall()
                att = []
                for row in rows :
                    att.append(row[0])
                self.attribute.clear()
                self.attribute.addItems(att)

                sql = """SELECT DISTINCT tp.name
                            FROM type_param tp 
                            JOIN type_param_test_mean tp_tm ON tp.id = tp_tm.id_type_param
                            JOIN test_mean tm ON tm.id = tp_tm.id_test_mean
                            WHERE tm.type = %s;
                """
                self.cur.execute(sql, (gen, ))
                self.conn.commit()
                rows = self.cur.fetchall()
                param = []
                for row in rows :
                    param.append(row[0])
                self.param.clear()
                self.param.addItems(param)

                self.test_mean_name.setFocus()
                self.test_mean_type.view().viewport().removeEventFilter(self)
                return True
            return False
        ######################################
        # Event on Combobox of Name of AC/WT #
        ######################################
        if obj == self.test_mean_name :      
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                self.test_mean_name.showPopup()
                self.test_mean_name.view().viewport().installEventFilter(self)
                return True   
            if event.type() == QEvent.KeyPress and event.key() == Qt.Key_Tab :         
                gen = self.test_mean_type.currentText()
                nom = self.test_mean_name.currentText()
                if not gen.isspace() and gen != '' and not nom.isspace() and nom != '':
                    test_mean_num = []
                    if 'manager' in [i[0] for i in self.lst] :
                        sql = """SELECT DISTINCT number FROM test_mean WHERE type = %s AND name = %s;"""
                        self.cur.execute(sql, (gen, nom))
                        self.conn.commit()
                        rows = self.cur.fetchall()
                        for row in rows :
                            test_mean_num.append(str(row[0]))
                    else :
                        for i in self.lst :
                            if i[1].split('_')[0] == gen and i[1].split('_')[1] == nom and i[1].split('_')[2] not in test_mean_num :
                                test_mean_num.append(str(i[1].split('_')[2]))
                    if nom not in [self.test_mean_name.itemText(i) for i in range(self.test_mean_name.count())] :
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Test mean is not existed or you are not allowed to modify this test mean")
                        msg.setWindowTitle("Error Identify")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()
                        self.test_mean_name.setFocus()
                    else :
                        self.test_mean_num.clear()
                        self.test_mean_num.addItems(test_mean_num)
                        self.test_mean_num.setFocus()
                        self.test_mean_num.setCurrentText('')
                return True   
            return False

        if obj == self.test_mean_name.view().viewport() :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                index = self.test_mean_name.view().currentIndex().row()
                nom = self.test_mean_name.itemText(index)
                gen = self.test_mean_type.currentText()
                test_mean_num = []
                for i in self.lst :
                    test_mean_num = []
                    if 'manager' in [i[0] for i in self.lst] :
                        sql = """SELECT DISTINCT number FROM test_mean WHERE type = %s and name = %s;"""
                        self.cur.execute(sql, (gen,nom))
                        self.conn.commit()
                        rows = self.cur.fetchall()
                        for row in rows :
                            test_mean_num.append(str(row[0]))
                    else :
                        for i in self.lst :
                            if i[1].split('_')[0] == gen and i[1].split('_')[1] == nom and i[1].split('_')[2] not in test_mean_num :
                                test_mean_num.append(str(i[1].split('_')[2]))
                self.test_mean_num.clear()
                self.test_mean_num.addItems(test_mean_num)
                self.test_mean_num.setFocus()
                self.test_mean_num.setCurrentText('')
                self.test_mean_name.view().viewport().removeEventFilter(self)
                return True
            return False


        if obj == self.test_mean_num :     
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                self.test_mean_num.showPopup()
                self.test_mean_num.view().viewport().installEventFilter(self)
                return True
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):      
                num = self.test_mean_num.currentText()
                nom = self.test_mean_name.currentText()
                gen = self.test_mean_type.currentText()
                if ~gen.isspace() and gen != '' and ~nom.isspace() and nom != '' and ~num.isspace() and num != '':
                    if num not in [self.test_mean_num.itemText(i) for i in range(self.test_mean_num.count())] :
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Test mean is not existed or you are not allowed to modify this test mean")
                        msg.setWindowTitle("Error Identify")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()
                        self.test_mean_num.setFocus()
                    else :
                        sql = """SELECT att.attribute, att.unity, att.value
                                FROM attribute att 
                                    JOIN attribute_test_mean att_tm ON att.id = att_tm.id_attribute
                                    JOIN test_mean tm ON tm.id = att_tm.id_test_mean
                                WHERE tm.type = %s AND tm.name =  %s AND tm.number = %s;
                        """
                        self.cur.execute(sql, (gen, nom, num))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        
                        self.model_attribute.removeRows(0, self.model_attribute.rowCount())

                        for row in rows :
                            self.addAttribute(*(row[0:])) 
                        
                        self.model_param.removeRows(0, self.model_param.rowCount())
                        sql = """SELECT tp.name, tp.unity
                                FROM type_param tp 
                                    JOIN type_param_test_mean tp_tm ON tp.id = tp_tm.id_type_param
                                    JOIN test_mean tm ON tm.id = tp_tm.id_test_mean
                                WHERE tm.type = %s AND tm.name =  %s AND tm.number = %s;
                        """
                        self.cur.execute(sql, (gen, nom, num))
                        self.conn.commit()

                        rows = self.cur.fetchall()
                        for row in rows :
                            self.addParam(*(row[0:]))

                        testmean = '_'.join([gen, nom, num])
                        self.initAttParam(testmean)
                        self.attribute.setFocus()
                return True
            return False

        if obj == self.test_mean_num.view().viewport() :
            index = self.test_mean_num.view().currentIndex().row()
            num = self.test_mean_num.itemText(index)
            nom = self.test_mean_name.currentText()
            gen = self.test_mean_type.currentText()
            testmean = '_'.join([gen, nom, num])
            self.initAttParam(testmean)
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                if ~gen.isspace() and gen != '' and ~nom.isspace() and nom != '' and ~num.isspace() and num != '':
                    sql = """SELECT att.attribute, att.unity, att.value
                             FROM attribute att 
                                JOIN attribute_test_mean att_tm ON att.id = att_tm.id_attribute
                                JOIN test_mean tm ON tm.id = att_tm.id_test_mean
                             WHERE tm.type = %s AND tm.name =  %s AND tm.number = %s;
                    """
                    self.cur.execute(sql, (gen, nom, num))
                    self.conn.commit()

                    rows = self.cur.fetchall()
                    
                    self.model_attribute.removeRows(0, self.model_attribute.rowCount())

                    for row in rows :
                        self.addAttribute(*(row[0:])) 
                    
                    self.model_param.removeRows(0, self.model_param.rowCount())
                    sql = """SELECT tp.name, tp.unity
                             FROM type_param tp 
                                JOIN type_param_test_mean tp_tm ON tp.id = tp_tm.id_type_param
                                JOIN test_mean tm ON tm.id = tp_tm.id_test_mean
                             WHERE tm.type = %s AND tm.name =  %s AND tm.number = %s;
                    """
                    self.cur.execute(sql, (gen, nom, num))
                    self.conn.commit()

                    rows = self.cur.fetchall()
                    for row in rows :
                        self.addParam(*(row[0:]))

                return True
            return False
        
    
        if obj == self.attribute :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                self.attribute.showPopup()
                self.attribute.view().viewport().installEventFilter(self)
                return True
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
                att = self.attribute.currentText()
                if not att.isspace() and att != '' :
                    sql = """SELECT DISTINCT att.unity 
                             FROM attribute att
                             WHERE att.attribute = %s;
                    
                    """
                    self.cur.execute(sql, (att,))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    unity = []
                    for row in rows :
                        unity.append(row[0])

                    self.att_unity.clear()
                    self.att_unity.addItems(unity)
                else :
                    self.att_unity.setCurrentText('')
                self.att_unity.setFocus()
                return True
            return False
        
        if obj == self.attribute.view().viewport() :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                index = self.attribute.view().currentIndex().row()
                att = self.attribute.itemText(index)
                sql = """SELECT DISTINCT att.unity 
                         FROM attribute att
                         WHERE att.attribute = %s;
                    
                """
                self.cur.execute(sql, (att,))
                self.conn.commit()
                rows = self.cur.fetchall()
                unity = []
                for row in rows :
                    unity.append(row[0])

                self.att_unity.clear()
                self.att_unity.addItems(unity)
                self.att_unity.setFocus()
                return True
            return False

        if obj == self.att_unity :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                self.att_unity.showPopup()
                self.att_unity.view().viewport().installEventFilter(self)
                return True
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
                self.att_value.setText('')
                self.att_value.setFocus()
                return True
            return False
        if obj == self.att_unity.view().viewport() :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                self.att_value.setText('')
                self.att_value.setFocus()
                return True
            return False

        if obj == self.att_value :
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
                if self.list_attribute_tree.selectedIndexes()[0] :
                    select_row = self.list_attribute_tree.selectedIndexes()[0].row()
                    att_old = self.model_attribute.data(self.model_attribute.index(select_row, 0))
                    unity_old = self.model_attribute.data(self.model_attribute.index(select_row, 1))
                    value_old = self.model_attribute.data(self.model_attribute.index(select_row, 2))
                    self.model_attribute.setData(self.model_attribute.index(select_row, 0), self.attribute.currentText())
                    self.model_attribute.setData(self.model_attribute.index(select_row, 1), self.att_unity.currentText())
                    self.model_attribute.setData(self.model_attribute.index(select_row, 2), self.att_value.text())
                    att_new = self.attribute.currentText()
                    unity_new = self.att_unity.currentText()
                    value_new = self.att_value.text()
                    if self.att_current.findAtt(att_old, unity_old, value_old) is not None :
                        self.att_delete.addAtt(att_old, unity_old, value_old)
                        self.att_update.delAtt(att_old, unity_old, value_old)
                    if self.att_create.findAtt(att_old, unity_old, value_old) is not None :
                        self.att_create.delAtt(att_old, unity_old, value_old)
                    self.att_create.addAtt(att_new, unity_new, value_new)
                return True
            return False
        if obj == self.param :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                self.param.showPopup()
                self.param.view().viewport().installEventFilter(self)
                return True
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
                param = self.param.currentText()
                if not param.isspace() and param != '' :
                    sql = """SELECT DISTINCT tp.unity 
                             FROM type_param tp
                             WHERE tp.name = %s;
                    
                    """
                    self.cur.execute(sql, (param,))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    unity = []
                    for row in rows :
                        unity.append(row[0])

                    self.param_unity.clear()
                    self.param_unity.addItems(unity)
                else :
                    self.param_unity.setCurrentText('')
                self.param_unity.setFocus()
                return True
            return False
        if obj == self.param.view().viewport() :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                index = self.param.view().currentIndex().row()
                param = self.param.itemText(index)
                sql = """SELECT DISTINCT tp.unity 
                             FROM type_param tp
                             WHERE tp.name = %s;
                    
                    """
                self.cur.execute(sql, (param,))
                self.conn.commit()
                rows = self.cur.fetchall()
                unity = []
                for row in rows :
                    unity.append(row[0])

                self.param_unity.clear()
                self.param_unity.addItems(unity)
                self.param_unity.setFocus()
                return True
            return False
        if obj == self.param_unity :
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
                if self.list_param_tree.selectedIndexes()[0] :
                    select_row = self.list_param_tree.selectedIndexes()[0].row()
                    param_old = self.model_param.data(self.model_param.index(select_row, 0))
                    unity_old = self.model_param.data(self.model_param.index(select_row, 1))
                    self.model_param.setData(self.model_param.index(select_row, 0), self.param.currentText())
                    self.model_param.setData(self.model_param.index(select_row, 1), self.param_unity.currentText())
                    param_new = self.param.currentText()
                    unity_new = self.param_unity.currentText()
                    if self.param_current.findParam(param_old, unity_old) is not None :
                        self.param_delete.addParam(param_old, unity_old)
                        self.param_update.delParam(param_old, unity_old)
                    if self.param_create.findParam(param_old, unity_old) is not None :
                        self.param_create.delParam(param_old, unity_old)
                    self.param_create.addParam(param_old, unity_old)
                return True
            return False
        return False

    def transfer(self): 
        test_mean_type = self.test_mean_type.currentText()
        test_mean_name = self.test_mean_name.currentText()
        test_mean_num = self.test_mean_num.currentText()        
        if 'manager' in [i[0] for i in self.lst] or 'admin' in [i[0] for i in self.lst if i[1] == '_'.join([test_mean_type, test_mean_name, test_mean_num])] or 'validate' in [i[0] for i in self.lst if i[1] == '_'.join([test_mean_type, test_mean_name, test_mean_num])] :
            for i in self.att_delete.lst_att :
                sql = """DELETE FROM attribute_test_mean WHERE id_test_mean = (SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s) AND id_attribute = (SELECT id FROM attribute WHERE attribute = %s AND unity = %s AND value = %s);"""
                self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1], i[2]))
                self.conn.commit()

            for i in self.att_create.lst_att :               
                sql = """SELECT * FROM attribute WHERE attribute = %s AND unity = %s AND value = %s;"""
                self.cur.execute(sql, (i[0], i[1], i[2]))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == [] :
                    print(i[0], i[1], i[2])
                    sql = """INSERT INTO attribute(attribute, unity, value) VALUES (%s, %s, %s);"""
                    self.cur.execute(sql, (i[0], i[1], i[2]))
                    self.conn.commit()
                sql = """SELECT * FROM attribute_test_mean att_tm JOIN test_mean tm ON tm.id = att_tm.id_test_mean JOIN attribute att ON att.id = att_tm.id_attribute WHERE tm.type = %s AND tm.name = %s AND tm.number = %s AND att.attribute = %s AND att.unity = %s AND att.value = %s;""" 
                self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1], i[2]))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == [] :
                    sql = """INSERT INTO attribute_test_mean(id_test_mean, id_attribute, validate) VALUES ((SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s), (SELECT id FROM attribute WHERE attribute = %s AND unity = %s AND value = %s), 't');"""
                    self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1], i[2]))
                    self.conn.commit()
                else : 
                    sql ="""UPDATE attribute_test_mean 
                        SET validate = 't'
                        WHERE id_test_mean = (SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s) AND id_attribute = (SELECT id FROM attribute WHERE attribute = %s AND unity = %s AND value = %s);"""
                    self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1], i[2]))
                    self.conn.commit()
            for i in self.att_update.lst_att :
                sql ="""UPDATE attribute_test_mean 
                        SET validate = 't'
                        WHERE id_test_mean = (SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s) AND id_attribute = (SELECT id FROM attribute WHERE attribute = %s AND unity = %s AND value = %s);"""
                self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1], i[2]))
                self.conn.commit()

            for i in self.param_create.lst_param :
                sql = """SELECT * FROM type_param WHERE name = %s AND unity = %s;"""
                self.cur.execute(sql, (i[0], i[1]))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == [] :
                    sql = """INSERT INTO type_param(name, unity) VALUES (%s, %s);"""
                    self.cur.execute(sql, (i[0], i[1]))
                    self.conn.commit()  
                sql = """SELECT * FROM type_param_test_mean tp_tm JOIN test_mean tm ON tm.id = tp_tm.id_test_mean JOIN type_param tp ON tp.id = tp_tm.id_attribute WHERE tm.type = %s AND tm.name = %s AND tm.number = %s AND tp.name = %s AND tp.unity = %s;""" 
                self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1]))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == [] : 
                    sql = """INSERT INTO type_param_test_mean(id_test_mean, id_type_param, validate) VALUES ((SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s), (SELECT id FROM type_param WHERE name = %s AND unity = %s), 't');"""
                    self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1]))
                    self.conn.commit()
                else :
                    sql ="""UPDATE type_param_test_mean 
                        SET validate = 't'
                        WHERE id_test_mean = (SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s) AND id_attribute = (SELECT id FROM type_param WHERE name = %s AND unity = %s);"""
                    self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1]))
                    self.conn.commit()
                    
                
            for i in self.param_update.lst_param :
                sql ="""UPDATE type_param_test_mean 
                        SET validate = 't'
                        WHERE id_test_mean = (SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s) AND id_attribute = (SELECT id FROM type_param WHERE name = %s AND unity = %s);"""
                self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1]))
                self.conn.commit()
                    

            for i in self.att_delete.lst_att :
                sql = """DELETE FROM attribute_test_mean WHERE id_test_mean = (SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s) AND id_attribute = (SELECT id FROM type_param WHERE name = %s AND unity = %s);"""
                self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1]))
                self.conn.commit()

        elif 'create' in [i[0] for i in self.lst if i[1] == '_'.join([test_mean_type, test_mean_name, test_mean_num])] :
            for i in self.att_create.lst_att :
                sql = """SELECT * FROM attribute WHERE attribute = %s AND unity = %s AND value = %s;"""
                self.cur.execute(sql, (i[0], i[1], i[2]))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == [] :
                    sql = """INSERT INTO attribute(attribute, unity, value) VALUES (%s, %s, %s);"""
                    self.cur.execute(sql, (i[0], i[1], i[2]))
                    self.conn.commit()
                sql = """SELECT * FROM attribute_test_mean att_tm JOIN test_mean tm ON tm.id = att_tm.id_test_mean JOIN attribute att ON att.id = att_tm.id_attribute WHERE tm.type = %s AND tm.name = %s AND tm.number = %s AND att.attribute = %s AND att.unity = %s AND att.value = %s;""" 
                self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1], i[2]))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == [] :
                    sql = """INSERT INTO attribute_test_mean(id_test_mean, id_attribute, validate) VALUES ((SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s), (SELECT id FROM attribute WHERE attribute = %s AND unity = %s AND value = %s), 'f');"""
                    self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1], i[2]))
                    self.conn.commit()
            for i in self.att_delete.lst_att :
                sql = """DELETE FROM attribute_test_mean WHERE id_test_mean = (SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s) AND id_attribute = (SELECT id FROM attribute WHERE attribute = %s AND unity = %s AND value = %s);"""
                self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1], i[2]))
                self.conn.commit()

            for i in self.param_create.lst_param :
                sql = """SELECT * FROM type_param WHERE name = %s AND unity = %s;"""
                self.cur.execute(sql, (i[0], i[1]))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == []:
                    sql = """INSERT INTO type_param(name, unity) VALUES (%s, %s);"""
                    self.cur.execute(sql, (i[0], i[1]))
                    self.conn.commit()
                sql = """SELECT * FROM type_param_test_mean tp_tm JOIN test_mean tm ON tm.id = tp_tm.id_test_mean JOIN type_param tp ON tp.id = tp_tm.id_attribute WHERE tm.type = %s AND tm.name = %s AND tm.number = %s AND tp.name = %s AND tp.unity = %s;""" 
                self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1]))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == [] : 
                    sql = """INSERT INTO type_param_test_mean(id_test_mean, id_type_param, validate) VALUES ((SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s), (SELECT id FROM type_param WHERE name = %s AND unity = %s), 'f');"""
                    self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1]))
                    self.conn.commit()

            for i in self.att_delete.lst_att :
                sql = """DELETE FROM attribute_test_mean WHERE id_test_mean = (SELECT id FROM test_mean WHERE type = %s AND name = %s AND number = %s) AND id_attribute = (SELECT id FROM type_param WHERE name = %s AND unity = %s);"""
                self.cur.execute(sql, (test_mean_type, test_mean_name, test_mean_num, i[0], i[1]))
                self.conn.commit()

        self.test_mean_type.setCurrentText('')
        self.test_mean_name.setCurrentText('')
        self.test_mean_num.setCurrentText('')
        self.model_attribute.removeRows(0, self.model_attribute.rowCount())
        self.model_param.removeRows(0, self.model_param.rowCount())
        self.attribute.setCurrentText('')
        self.att_unity.setCurrentText('')
        self.att_value.setText('')
        self.param.setCurrentText('')
        self.param_unity.setCurrentText('')
        file_name = "_".join([test_mean_type, test_mean_name, test_mean_num])
        # os.remove(f'.\\file\\test_mean\\{file_name}_att.csv')
        # os.remove(f'.\\file\\test_mean\\{file_name}_param.csv')

    def initAttParam(self, testmean) :
        att = attribute(testmean)
        self.att_current = deepcopy(att)
        self.att_delete = deepcopy(att)
        self.att_create = deepcopy(att)

        sql = """SELECT att.attribute, att.unity, att.value
                 FROM attribute att 
                    JOIN attribute_test_mean att_tm ON att.id = att_tm.id_attribute
                    JOIN test_mean tm ON tm.id = att_tm.id_test_mean 
                 WHERE tm.type = %s AND tm.name = %s AND tm.number = %s;
        """

        self.cur.execute(sql, tuple(testmean.split('_')))
        self.conn.commit()

        rows = self.cur.fetchall()
        for row in rows :
            self.att_current.addAtt(row[0], row[1], row[2])
        self.att_update = deepcopy(self.att_current)
        parametre = param(testmean)
        self.param_current = deepcopy(parametre)
        self.param_delete = deepcopy(parametre)
        self.param_create = deepcopy(parametre)

        sql = """SELECT tp.name, tp.unity
                 FROM type_param tp
                    JOIN type_param_test_mean tp_tm ON tp.id = tp_tm.id_type_param
                    JOIN test_mean tm ON tm.id = tp_tm.id_test_mean 
                 WHERE tm.type = %s AND tm.name = %s AND tm.number = %s;
        """

        self.cur.execute(sql, tuple(testmean.split('_')))
        self.conn.commit()

        rows = self.cur.fetchall()
        for row in rows :
            self.param_current.addParam(row[0], row[1])

        self.param_update = deepcopy(self.param_current)

    def save(self) :
        test_mean_type = self.test_mean_type.currentText()
        test_mean_name = self.test_mean_name.currentText()
        test_mean_num = self.test_mean_num.currentText()

        if not test_mean_type.isspace() and test_mean_type != '' and not test_mean_name.isspace() and test_mean_name != '' and not test_mean_num.isspace() and test_mean_num != '' :
            file_name = '_'.join([test_mean_type, test_mean_name, test_mean_num])

            with open(f'.\\file\\test_mean\\{file_name}_att.csv', 'a') as f :
                try :
                    pass
                finally :
                    f.close()

            lines = []
            for i in range(self.model_attribute.rowCount()) :
                att = self.model_attribute.data(self.model_attribute.index(i, 0))
                unity = self.model_attribute.data(self.model_attribute.index(i, 1))
                value = self.model_attribute.data(self.model_attribute.index(i, 2))
                lines.append([att, unity, value])

            with open(f'.\\file\\test_mean\\{file_name}_att.csv', 'w', newline = '') as f :
                try :
                    writer = csv.writer(f)
                    writer.writerows(lines)
                finally :
                    f.close()

            with open(f'.\\file\\test_mean\\{file_name}_param.csv', 'a') as f :
                try :
                    pass
                finally :
                    f.close()

            lines = []
            for i in range(self.model_param.rowCount()) :
                param = self.model_param.data(self.model_param.index(i, 0))
                unity = self.model_param.data(self.model_param.index(i, 1))
                lines.append([param, unity])
            
            with open(f'.\\file\\test_mean\\{file_name}_param.csv', 'w', newline = '') as f :
                try :
                    writer = csv.writer(f)
                    writer.writerows(lines)
                finally :
                    f.close()
        else :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Test mean is not identified\nIdentify which test mean")
            msg.setWindowTitle("Error Identify")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
    def connect(self) :
        try :
            host = "localhost"
            username = "iventre"
            dbname = "lmsm"
            password = "lmsm"
            self.conn = psycopg2.connect(host = host, user = username, dbname = dbname, password = password)
            self.cur = self.conn.cursor() 
        except psycopg2.Error as err:   
            print(str(err))
