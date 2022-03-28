from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import psycopg2
import sys
import csv
sys.path.append('..\\QT\\class')
import coating
from coating import *
from copy import deepcopy

class Coating(QWidget) :
    def __init__(self, parent, uname, lst) :
        super(Coating, self).__init__(parent)
        self.connect()
        self.uname = uname
        if 'manager' in [i[0] for i in lst] :
            self.lst = lst
        else :
            self.lst = [[i[0], i[2]] for i in lst if i[1] == "coating"]
        self.setupUI()

    def setupUI(self) :
        ######################################################################################
        #                                      Create Tank                                   #
        ######################################################################################
        splitter = QSplitter(Qt.Vertical, self)
        label1 = QLabel('Create a Coating')
        frame1 = QFrame()
        hlayout = QHBoxLayout()
        ##################################################################
        #                           tank type                            #
        ##################################################################
        splitter1 = QSplitter(Qt.Vertical)
        label = QLabel('Coating name')
        self.coating_type = QComboBox()
        edit = QLineEdit()
        type_coating = []
        if 'manager' in [i[0] for i in self.lst] :
            sql = """SELECT DISTINCT ref FROM type_coating;"""
            self.cur.execute(sql)
            self.conn.commit()
            rows = self.cur.fetchall()
            for row in rows :
                type_coating.append(row[0])
        else :
            for i in self.lst :
                if i[1] not in type_coating :
                    type_coating.append(i[1])
        self.coating_type.clear()
        self.coating_type.setLineEdit(edit)
        self.coating_type.addItems(type_coating)
        self.coating_type.setCurrentText('')
        self.coating_type.installEventFilter(self)
        splitter1.addWidget(label)
        splitter1.addWidget(self.coating_type)
        hlayout.addWidget(splitter1)
        ##################################################################
        #                          tank number                           #
        ##################################################################
        splitter2 = QSplitter(Qt.Vertical)
        label = QLabel('Serial number')
        self.coating_num = QComboBox()
        edit = QLineEdit()
        self.coating_num.setLineEdit(edit)
        self.coating_num.installEventFilter(self)
        splitter2.addWidget(label)
        splitter2.addWidget(self.coating_num)
        hlayout.addWidget(splitter2)
        ####################################################################
        #                                                                  #
        ####################################################################
        frame1.setLayout(hlayout)
        frame1.setFrameStyle(1)
        splitter.addWidget(label1)
        splitter.addWidget(frame1)
        splitter.setGeometry(10, 10, 260, 80)
        ######################################################################################
        #                          Create attributs for test mean                            #
        ######################################################################################
        splitter = QSplitter(Qt.Vertical, self)
        label1 = QLabel('List of characteristic for this test coating')
        frame1 = QFrame()
        ######################################################################################
        #                                    Button search                                   #
        ######################################################################################
        self.search_carac_btn = QPushButton('Search', frame1)
        self.search_carac_btn.setGeometry(200, 0, 120, 20)        

        ##################################################################
        #                           Attribute                            #
        ##################################################################
        splitter1 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Characteristic')
        self.carac = QComboBox()
        edit = QLineEdit()        
        self.carac.setLineEdit(edit)
        self.carac.setCurrentText('')
        self.carac.installEventFilter(self)
        splitter1.addWidget(label)
        splitter1.addWidget(self.carac)
        splitter1.setGeometry(10, 30, 150, 40)
        ##################################################################
        #                        Unity of attribut                       #
        ##################################################################
        splitter2 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Unity')
        self.unity = QComboBox()
        edit = QLineEdit()
        self.unity.setLineEdit(edit)
        self.unity.installEventFilter(self)
        splitter2.addWidget(label)
        splitter2.addWidget(self.unity)
        splitter2.setGeometry(170, 30, 90, 40)
        ####################################################################
        #                        value of attribut                         #
        ####################################################################
        splitter3 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Value')
        self.value = QLineEdit()
        self.value.installEventFilter(self)
        splitter3.addWidget(label)
        splitter3.addWidget(self.value)
        splitter3.setGeometry(270, 30, 120, 40)
        #####################################################################
        #                       create attribut button                      #
        #####################################################################
        self.create_carac_btn = QPushButton('Create', frame1)
        self.create_carac_btn.setGeometry(140, 80, 120, 20)
        #####################################################################
        #                         list of attributes                        #
        #####################################################################
        splitter4 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('List of attributes with their value')
        self.model_carac = self.createCaracModel(self)
        self.list_carac_tree = QTreeView(frame1)
        self.list_carac_tree.setModel(self.model_carac)
        self.list_carac_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(3) :
            self.list_carac_tree.setColumnWidth(i, 380 / 3)
        splitter4.addWidget(label)
        splitter4.addWidget(self.list_carac_tree)
        splitter4.setGeometry(10, 100, 380, 270)
        frame1.setFrameStyle(1)
        splitter.addWidget(label1)
        splitter.addWidget(frame1)
        splitter.setGeometry(10, 100, 400, 400)
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
        #################################################################################
        #################################################################################
        self.create_carac_btn.clicked.connect(self.create_carac)
        self.list_carac_tree.doubleClicked.connect(self.del_carac)
        self.transfer_btn.clicked.connect(self.transfer)

        self.list_carac_tree.clicked.connect(self.viewCarac)
        self.save_btn.clicked.connect(self.save)
        self.search_carac_btn.clicked.connect(self.searchCarac)
        self.cancel_btn.clicked.connect(self.cancel)

    def cancel(self) :
        self.model_carac.removeRows(0, self.model_carac.rowCount())
        type_coating = self.coating_type.currentText()
        num_coating = self.coating_num.currentText()
        if not type_coating.isspace() and type_coating != '' and not num_coating.isspace() and num_coating != '' :
            ct = '_'.join([type_coating, num_coating])
            self.initCarac(ct)
            sql = """SELECT att.attribute, att.unity, att.value 
                                FROM attribute att 
                                JOIN attribute_coating att_c ON att.id = att_c.id_attribute
                                JOIN coating c ON c.id = att_c.id_coating
                                JOIN type_coating tc ON tc.id = c.id_type_coating
                                WHERE tc.ref = %s AND c.number = %s 
                        ;"""
            self.cur.execute(sql, (type_coating, num_coating))
            self.conn.commit()
            rows = self.cur.fetchall()
            self.model_carac.removeRows(0, self.model_carac.rowCount())
            for row in rows :
                self.addCarac(*(row[0:]))


    def searchCarac(self) :
        type_coating = self.coating_type.currentText()
        num_coating = self.coating_num.currentText()
        ct = '_'.join([type_coating, num_coating])
        self.initCarac(ct)
        if not type_coating.isspace() and type_coating != '' and not num_coating.isspace() and num_coating != '' :
            file_name = '_'.join([type_coating, num_coating])
            fname = QFileDialog.getOpenFileName(self, 'Open file', 
            f'.\\file\\coating\\{file_name}_carac',"CSV data files (*.csv *.xlsx)")

            with open(fname[0], 'r') as f :
                try :
                    rows = csv.reader(f)
                    self.model_carac.removeRows(0, self.model_carac.rowCount())
                    for row in rows :
                        self.addCarac(*row) 
                        self.carac_create.addCarac(*row)
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

    def save(self) :
        type_coating = self.coating_type.currentText()
        num_coating = self.coating_num.currentText()

        if not type_coating.isspace() and type_coating != '' and not num_coating.isspace() and num_coating != '' :
            file_name = '_'.join([type_coating, num_coating])

            with open(f'.\\file\\coating\\{file_name}_carac.csv', 'a') as f :
                try :
                    pass
                finally :
                    f.close()

            lines = []
            for i in range(self.model_carac.rowCount()) :
                carac = self.model_carac.data(self.model_carac.index(i, 0))
                unity = self.model_carac.data(self.model_carac.index(i, 1))
                value = self.model_carac.data(self.model_carac.index(i, 2))
                lines.append([carac, unity, value])

            with open(f'.\\file\\coating\\{file_name}_carac.csv', 'w', newline = '') as f :
                try :
                    writer = csv.writer(f)
                    writer.writerows(lines)
                finally :
                    f.close()

            with open(f'.\\file\\coating\\{file_name}_carac.csv', 'a') as f :
                try :
                    pass
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

    def createCaracModel(self, parent) :
        model = QStandardItemModel(0, 3, parent)
        model.setHeaderData(0, Qt.Horizontal, 'Characteristic')
        model.setHeaderData(1, Qt.Horizontal, 'Value')
        model.setHeaderData(2, Qt.Horizontal, 'Unity')
        return model
    
    def addCarac(self, carac, unity, value) :
        self.model_carac.insertRow(self.model_carac.rowCount())
        row = self.model_carac.rowCount() - 1
        self.model_carac.setData(self.model_carac.index(row, 0), carac)
        self.model_carac.setData(self.model_carac.index(row, 1), unity)
        self.model_carac.setData(self.model_carac.index(row, 2), value)

    def create_carac(self) :
        type_coating = self.coating_type.currentText()
        num_coating = self.coating_num.currentText()
         
        carac = self.carac.currentText()
        unity = self.unity.currentText()
        value = self.value.text()
        if not carac.isspace() and carac != '' and not value.isspace() and value != '' :
            if not type_coating.isspace() and type_coating != '' and not num_coating.isspace() and num_coating != '' :
                self.addCarac(carac, unity, value)
                self.carac_create.addCarac(carac, unity, value)
            else :
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Test mean is not identified\nIdentify which test mean")
                msg.setWindowTitle("Error Identify")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return

    def del_carac(self) :
        type_coating = self.coating_type.currentText()
        num_coating = self.coating_num.currentText()
        if  (type_coating.isspace() or type_coating == '') or  (num_coating.isspace() or num_coating == ''):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Coating is not identified\nIdentify which coating")
            msg.setWindowTitle("Error Identify")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        select_carac = self.list_carac_tree.selectedIndexes()[0].row()
        carac = self.model_carac.data(self.model_carac.index(select_carac, 0))
        unity = self.model_carac.data(self.model_carac.index(select_carac, 1))
        value = self.model_carac.data(self.model_carac.index(select_carac, 2))
        self.model_carac.removeRow(select_carac)
        if self.carac_current.findCarac(carac, unity, value) is not None:
            self.carac_delete.addCarac(carac, unity, value)
            self.carac_update.delCarac(carac, unity, value)
        if self.carac_create.findCarac(carac, unity, value) is not None:
            self.carac_create.delCarac(carac, unity, value)
    
    def viewCarac(self):
        if self.list_carac_tree.selectedIndexes()[0] :
            select_row = self.list_carac_tree.selectedIndexes()[0].row()
            carac = self.model_carac.data(self.model_carac.index(select_row, 0))
            unity = self.model_carac.data(self.model_carac.index(select_row, 1))
            value = self.model_carac.data(self.model_carac.index(select_row, 2))
            self.carac.setCurrentText(carac)
            self.unity.setCurrentText(unity)
            self.value.setText(str(value))


    def eventFilter(self, obj, event) :
        if obj == self.coating_type :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                type_coating = []
                if 'manager' in [i[0] for i in self.lst] :
                    sql = """SELECT DISTINCT ref FROM type_coating;"""
                    self.cur.execute(sql)
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    for row in rows :
                        type_coating.append(row[0])
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
                    self.lst = [[i[0], i[2]] for i in self.lst if i[1] == "coating"]
                    for i in self.lst :
                        if i[1] not in type_coating :
                            type_coating.append(i[1])
                self.coating_type.clear()
                self.coating_type.addItems(type_coating)
                self.coating_type.showPopup()
                self.coating_type.view().viewport().installEventFilter(self)
                return True
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return) :
                type_coating = self.coating_type.currentText()
                if not type_coating.isspace() and type_coating != '' :
                    num_coating = []
                    sql = """SELECT c.number 
                                FROM coating c
                                JOIN type_coating tc ON c.id_type_coating = tc.id
                                WHERE tc.ref = %s;"""
                    self.cur.execute(sql, (type_coating,))
                    self.conn.commit()

                    rows = self.cur.fetchall()
                    for row in rows :
                        num_coating.append(str(row[0]))
                    self.coating_num.clear()
                    self.coating_num.addItems(num_coating)
                    self.coating_num.setCurrentText('')
                    carac = []
                    sql = """SELECT att.attribute
                             FROM attribute att 
                             JOIN attribute_coating att_c ON att.id = att_c.id_attribute
                             JOIN coating c ON c.id = att_c.id_coating
                             JOIN type_coating tc ON tc.id = c.id_type_coating
                             WHERE tc.ref = %s                   
                    """
                    self.cur.execute(sql, (type_coating,))
                    self.conn.commit()

                    rows = self.cur.fetchall()
                    for row in rows :
                        carac.append(str(row[0]))
                    self.carac.clear()
                    self.carac.addItems(carac)
                    self.carac.setCurrentText('')
                self.coating_num.setFocus()
                return True
            return False
        if obj == self.coating_type.view().viewport() :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                index = self.coating_type.view().currentIndex().row()
                type_coating = self.coating_type.itemText(index)
                coating_num = []
                sql = """SELECT c.number 
                            FROM coating c
                            JOIN type_coating tc ON c.id_type_coating = tc.id
                            WHERE tc.ref = %s;"""
                self.cur.execute(sql, (type_coating,))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows :
                    coating_num.append(str(row[0]))
                self.coating_num.clear()
                self.coating_num.addItems(coating_num)
                self.coating_num.setCurrentText('')
                carac = []
                sql = """SELECT att.attribute
                            FROM attribute att 
                            JOIN attribute_coating att_c ON att.id = att_c.id_attribute
                            JOIN coating c ON c.id = att_c.id_coating
                            JOIN type_coating tc ON tc.id = c.id_type_coating
                            WHERE tc.ref = %s                   
                """
                self.cur.execute(sql, (type_coating,))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows :
                    carac.append(str(row[0]))
                self.carac.clear()
                self.carac.addItems(carac)
                self.carac.setCurrentText('')
                self.coating_num.setFocus()
                return True
            return False

        if obj == self.coating_num :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                self.coating_num.showPopup()
                self.coating_num.view().viewport().installEventFilter(self)
                return True
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return) :
                num_coating = self.coating_num.currentText()
                type_coating = self.coating_type.currentText()
                if not type_coating.isspace() and type_coating != '' and not num_coating.isspace() and num_coating != '':
                    sql = """SELECT att.attribute, att.unity, att.value 
                             FROM attribute att 
                             JOIN attribute_coating att_c ON att.id = att_c.id_attribute
                             JOIN coating c ON c.id = att_c.id_coating
                             JOIN type_coating tc ON tc.id = c.id_type_coating
                             WHERE tc.ref = %s AND c.number = %s 
                    ;"""
                    self.cur.execute(sql, (type_coating, num_coating))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    self.model_carac.removeRows(0, self.model_carac.rowCount())
                    for row in rows :
                        self.addCarac(*(row[0:]))

                    ct = '_'.join([type_coating, num_coating])
                    self.initCarac(ct)
                self.carac.setFocus()
                return True
            return False

        if obj == self.coating_num.view().viewport() :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                index = self.coating_num.view().currentIndex().row()
                num_coating = self.coating_num.itemText(index)
                type_coating = self.coating_type.currentText()
                sql = """SELECT att.attribute, att.unity, att.value 
                             FROM attribute att 
                             JOIN attribute_coating att_c ON att.id = att_c.id_attribute
                             JOIN coating c ON c.id = att_c.id_coating
                             JOIN type_coating tc ON tc.id = c.id_type_coating
                             WHERE tc.ref = %s AND c.number = %s 
                ;"""
                self.cur.execute(sql, (type_coating, num_coating))
                self.conn.commit()
                rows = self.cur.fetchall()
                self.model_carac.removeRows(0, self.model_carac.rowCount())
                for row in rows :
                    self.addCarac(*(row[0:]))

                ct = '_'.join([type_coating, num_coating])
                self.initCarac(ct)
                return True
            return False

        if obj == self.carac :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                self.carac.showPopup()
                self.carac.view().viewport().installEventFilter(self)
                return True
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
                carac = self.carac.currentText()
                if not carac.isspace() and carac != '' :
                    sql = """SELECT DISTINCT att.unity 
                             FROM attribute att
                             WHERE att.attribute = %s;
                    
                    """
                    self.cur.execute(sql, (carac,))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    unity = []
                    for row in rows :
                        unity.append(row[0])

                    self.unity.clear()
                    self.unity.addItems(unity)
                else :
                    self.unity.setCurrentText('')
                self.unity.setFocus()
                return True
            return False
        
        if obj == self.carac.view().viewport() :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                index = self.carac.view().currentIndex().row()
                carac = self.carac.itemText(index)
                sql = """SELECT DISTINCT att.unity 
                         FROM attribute att
                         WHERE att.attribute = %s;
                    
                """
                self.cur.execute(sql, (carac,))
                self.conn.commit()
                rows = self.cur.fetchall()
                unity = []
                for row in rows :
                    unity.append(row[0])

                self.unity.clear()
                self.unity.addItems(unity)
                self.unity.setFocus()
                return True
            return False

        if obj == self.unity :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                self.unity.showPopup()
                self.unity.view().viewport().installEventFilter(self)
                return True
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
                self.value.setText('')
                self.value.setFocus()
                return True
            return False
        if obj == self.unity.view().viewport() :
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton :
                self.value.setText('')
                self.value.setFocus()
                return True
            return False

        if obj == self.value :
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
                if self.list_carac_tree.selectedIndexes()[0] :
                    select_row = self.list_carac_tree.selectedIndexes()[0].row()
                    carac_old = self.model_carac.data(self.model_carac.index(select_row, 0))
                    unity_old = self.model_carac.data(self.model_carac.index(select_row, 1))
                    value_old = self.model_carac.data(self.model_carac.index(select_row, 2))
                    self.model_carac.setData(self.model_carac.index(select_row, 0), self.carac.currentText())
                    self.model_carac.setData(self.model_carac.index(select_row, 1), self.unity.currentText())
                    self.model_carac.setData(self.model_carac.index(select_row, 2), self.value.text())
                    carac_new = self.carac.currentText()
                    unity_new = self.unity.currentText()
                    value_new = self.value.text()
                    if self.carac_current.findCarac(carac_old, unity_old, value_old) is not None :
                        self.carac_delete.addCarac(carac_old, unity_old, value_old)
                        self.carac_update.delCarac(carac_old, unity_old, value_old)
                    if self.carac_create.findCarac(carac_old, unity_old, value_old) is not None :
                        self.carac_create.addCarac(carac_old, unity_old, value_old)
                    self.carac_create.addCarac(carac_new, unity_new, value_new)
                return True
            return False
        return False

    def initCarac(self, ct) :
        carac = carateristic(ct)
        self.carac_current = deepcopy(carac)
        self.carac_create = deepcopy(carac)
        self.carac_delete = deepcopy(carac)

        sql = """SELECT att.attribute, att.unity, att.value 
                 FROM attribute att 
                 JOIN attribute_coating att_c ON att.id = att_c.id_attribute
                 JOIN coating c ON c.id = att_c.id_coating
                 JOIN type_coating tc ON tc.id = c.id_type_coating
                 WHERE tc.ref = %s AND c.number = %s 
        ;"""

        self.cur.execute(sql, tuple(ct.split('_')))
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows :
            self.carac_current.addCarac(*(row[0:]))
        
        self.carac_update = deepcopy(self.carac_current)

    def transfer(self) :
        type_coating = self.coating_type.currentText()
        num_coating = self.coating_num.currentText()       
        if 'manager' in [i[0] for i in self.lst] or 'admin' in [i[0] for i in self.lst] or 'validate' in [i[0] for i in self.lst] :
            sql = """SELECT c.id_type_coating, c.number FROM coating c JOIN type_coating tc ON c.id_type_coating = tc.id WHERE tc.ref = %s AND c.number = %s"""
            self.cur.execute(sql, (type_coating, num_coating))
            self.conn.commit()
            rows = self.cur.fetchall()
            if rows == []:
                sql = """INSERT INTO coating(id_type_coating, number, validate) VALUES ((SELECT id FROM type_coating WHERE ref = %s), %s, %s);"""
                self.cur.execute(sql, (type_coating, num_coating, 't'))
                self.conn.commit()
            else :
                sql = """UPDATE coating 
                         SET validate = 't'
                         WHERE id_type_coating = (SELECT id FROM type_coating WHERE ref = %s) AND number = %s;
                """
                self.cur.execute(sql, (type_coating, num_coating))
                self.conn.commit()
            for i in self.carac_create.carac :               
                sql = """SELECT * FROM attribute WHERE attribute = %s AND unity = %s AND value = %s;"""
                self.cur.execute(sql, (i[0], i[1], i[2]))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == [] :
                    sql = """INSERT INTO attribute(attribute, unity, value) VALUES (%s, %s, %s);"""
                    self.cur.execute(sql, (i[0], i[1], i[2]))
                    self.conn.commit()
                sql = """SELECT * FROM attribute_coating att_c JOIN coating c ON c.id = att_c.id_coating JOIN attribute att ON att.id = att_c.id_attribute JOIN type_coating tc ON tc.id = c.id_type_coating WHERE tc.ref = %s AND c.number = %s AND att.attribute = %s AND att.unity = %s AND att.value = %s;"""
                self.cur.execute(sql, (type_coating, num_coating, i[0], i[1], i[2]))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == [] :
                    sql = """INSERT INTO attribute_coating(id_coating, id_attribute, validate) VALUES ((SELECT c.id FROM coating c JOIN type_coating tc ON tc.id = c.id_type_coating WHERE tc.ref = %s AND c.number = %s), (SELECT id FROM attribute WHERE attribute = %s AND unity = %s AND value = %s), 't');"""
                    self.cur.execute(sql, (type_coating, num_coating, i[0], i[1], i[2]))
                    self.conn.commit()

            for i in self.carac_update.carac :
                sql ="""UPDATE attribute_coating 
                        SET validate = 't'
                        WHERE id_coating = (SELECT c.id FROM coating c JOIN type_coating tc ON tc.id = c.id_type_coating WHERE tc.ref = %s AND c.number = %s) AND id_attribute = (SELECT id FROM attribute WHERE attribute = %s AND unity = %s AND value = %s);"""
                self.cur.execute(sql, (type_coating, num_coating, i[0], i[1], i[2]))
                self.conn.commit()

            for i in self.carac_delete.carac :
                sql = """DELETE FROM attribute_coating WHERE id_coating = (SELECT c.id FROM coating c JOIN type_coating tc ON tc.id = c.id_type_coating WHERE tc.ref = %s AND c.number = %s) AND id_attribute = (SELECT id FROM attribute WHERE attribute = %s AND unity = %s AND value = %s);"""
                self.cur.execute(sql, (type_coating, num_coating, i[0], i[1], i[2]))
                self.conn.commit()


        elif 'create' in [i[0] for i in self.lst] :
            sql = """SELECT c.id_type_coating, c.number FROM coating c JOIN type_coating tc ON c.id_type_coating = tc.id WHERE tc.ref = %s AND c.number = %s"""
            self.cur.execute(sql, (type_coating, num_coating))
            self.conn.commit()
            rows = self.cur.fetchall()
            if rows == []:
                sql = """INSERT INTO coating(id_type_coating, number, validate) VALUES ((SELECT id FROM type_coating WHERE ref = %s), %s, %s);"""
                self.cur.execute(sql, (type_coating, num_coating, 'f'))
                self.conn.commit()
            for i in self.carac_create.carac :               
                sql = """SELECT * FROM attribute WHERE attribute = %s AND unity = %s AND value = %s;"""
                self.cur.execute(sql, (i[0], i[1], i[2]))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == [] :
                    sql = """INSERT INTO attribute(attribute, unity, value) VALUES (%s, %s, %s);"""
                    self.cur.execute(sql, (i[0], i[1], i[2]))
                    self.conn.commit()

                sql = """INSERT INTO attribute_coating(id_coating, id_attribute, validate) VALUES ((SELECT c.id FROM coating c JOIN type_coating tc ON tc.id = c.id_type_coating WHERE tc.ref = %s AND c.number = %s), (SELECT id FROM attribute WHERE attribute = %s AND unity = %s AND value = %s), 'f');"""
                self.cur.execute(sql, (type_coating, num_coating, i[0], i[1], i[2]))
                self.conn.commit()
            for i in self.carac_delete.carac :
                sql = """DELETE FROM attribute_coating WHERE id_coating = (SELECT c.id FROM coating c JOIN type_coating tc ON tc.id = c.id_type_coating WHERE tc.ref = %s AND c.number = %s) AND id_attribute = (SELECT id FROM attribute WHERE attribute = %s AND unity = %s AND value = %s);"""
                self.cur.execute(sql, (type_coating, num_coating, i[0], i[1], i[2]))
                self.conn.commit()

        self.coating_type.setCurrentText('')
        self.coating_num.setCurrentText('')
        self.carac.setCurrentText('')
        self.model_carac.removeRows(0, self.model_carac.rowCount())
        self.unity.setCurrentText('')
        self.value.setText('')

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

