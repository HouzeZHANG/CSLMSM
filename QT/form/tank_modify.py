from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import psycopg2
import sys
import csv

sys.path.append('..QT\\class')
import tank
from tank import *
from copy import deepcopy


class Tank(QWidget):
    def __init__(self, parent, uname, lst):
        super(Tank, self).__init__(parent)
        self.uname = uname
        self.connect()
        if 'manager' in [i[0] for i in lst]:
            self.lst = lst
        else:
            self.lst = [[i[0], i[2]] for i in lst if i[1] == "tank"]
        self.setupUI()

    def setupUI(self):
        ######################################################################################
        #                                      Create Tank                                   #
        ######################################################################################
        splitter = QSplitter(Qt.Vertical, self)
        label1 = QLabel('Tank identification')
        frame1 = QFrame()
        hlayout = QHBoxLayout()
        ##################################################################
        #                           tank type                            #
        ##################################################################
        splitter1 = QSplitter(Qt.Vertical)
        label = QLabel('Tank reference')
        self.tank_type = QComboBox()
        edit = QLineEdit()
        type_tank = []
        if 'manager' in [i[0] for i in self.lst]:
            sql = """SELECT DISTINCT ref FROM type_tank;"""
            self.cur.execute(sql)
            self.conn.commit()
            rows = self.cur.fetchall()
            for row in rows:
                type_tank.append(row[0])
        else:
            for i in self.lst:
                if i[1] not in type_tank:
                    type_tank.append(i[1])
        self.tank_type.clear()
        self.tank_type.setLineEdit(edit)
        self.tank_type.addItems(type_tank)
        self.tank_type.setCurrentText('')
        self.tank_type.installEventFilter(self)
        splitter1.addWidget(label)
        splitter1.addWidget(self.tank_type)
        hlayout.addWidget(splitter1)
        ##################################################################
        #                          tank number                           #
        ##################################################################
        splitter2 = QSplitter(Qt.Vertical)
        label = QLabel('Serial number')
        self.tank_num = QComboBox()
        edit = QLineEdit()
        self.tank_num.setLineEdit(edit)
        self.tank_num.installEventFilter(self)
        splitter2.addWidget(label)
        splitter2.addWidget(self.tank_num)
        hlayout.addWidget(splitter2)
        ####################################################################
        #                                                                  #
        ####################################################################
        frame1.setLayout(hlayout)
        frame1.setFrameStyle(1)
        splitter.addWidget(label1)
        splitter.addWidget(frame1)
        splitter.setGeometry(10, 10, 260, 80)
        #####################################################################
        #                      List of posion on tank                       #
        #####################################################################
        splitter = QSplitter(Qt.Vertical, self)
        label1 = QLabel('Position :  coordinates (nm) in aircraft reference & tangente plane')
        frame1 = QFrame()
        #####################################################################
        #                      Extract geometrical file                     #
        #####################################################################
        self.extract_btn = QPushButton('Extract from geometrical file', frame1)
        self.extract_btn.setGeometry(10, 10, 180, 30)
        ######################################################################
        #                           Location number                          #
        ######################################################################
        splitter1 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Location number')
        self.loc_num = QComboBox()
        edit = QLineEdit()
        self.loc_num.setLineEdit(edit)
        self.loc_num.installEventFilter(self)
        splitter1.addWidget(label)
        splitter1.addWidget(self.loc_num)
        splitter1.setGeometry(10, 40, 120, 40)

        #######################################################################
        #                           sensor/coating ref                        #
        #######################################################################
        splitter1 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Sensor/coating Reference')
        self.sensor_coating_ref = QComboBox()
        edit = QLineEdit()
        self.sensor_coating_ref.setLineEdit(edit)
        self.sensor_coating_ref.installEventFilter(self)
        splitter1.addWidget(label)
        splitter1.addWidget(self.sensor_coating_ref)
        splitter1.setGeometry(140, 40, 150, 40)
        #######################################################################
        #                                                                     #
        #######################################################################
        splitter1 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('X')
        label.setAlignment(Qt.AlignCenter)
        self.x = QLineEdit(frame1)
        self.x.setAlignment(Qt.AlignCenter)
        splitter1.addWidget(label)
        splitter1.addWidget(self.x)
        splitter1.setGeometry(10, 80, 120, 40)
        #######################################################################
        #                                                                     #
        #######################################################################
        splitter1 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Y')
        label.setAlignment(Qt.AlignCenter)
        self.y = QLineEdit(frame1)
        self.y.setAlignment(Qt.AlignCenter)
        splitter1.addWidget(label)
        splitter1.addWidget(self.y)
        splitter1.setGeometry(140, 80, 120, 40)
        #######################################################################
        #                                                                     #
        #######################################################################
        splitter1 = QSplitter(Qt.Vertical, frame1)
        label = QLabel('Z')
        label.setAlignment(Qt.AlignCenter)
        self.z = QLineEdit(frame1)
        self.z.setAlignment(Qt.AlignCenter)
        splitter1.addWidget(label)
        splitter1.addWidget(self.z)
        splitter1.setGeometry(270, 80, 120, 40)
        #######################################################################
        #                                                                     #
        #######################################################################
        frame2 = QFrame(frame1)
        layout = QGridLayout()
        #######################################################################
        #                                                                     #
        #######################################################################
        label = QLabel('Tangent vector U')
        layout.addWidget(label, 0, 1)
        label = QLabel('Tangent vector V')
        layout.addWidget(label, 0, 2)
        label = QLabel('Tangent vector N')
        layout.addWidget(label, 0, 3)
        label = QLabel('I')
        layout.addWidget(label, 1, 0)
        self.u_i = QLineEdit()
        layout.addWidget(self.u_i, 1, 1)
        self.v_i = QLineEdit()
        layout.addWidget(self.v_i, 1, 2)
        self.n_i = QLineEdit()
        layout.addWidget(self.n_i, 1, 3)
        label = QLabel('J')
        layout.addWidget(label, 2, 0)
        self.u_j = QLineEdit()
        layout.addWidget(self.u_j, 2, 1)
        self.v_j = QLineEdit()
        layout.addWidget(self.v_j, 2, 2)
        self.n_j = QLineEdit()
        layout.addWidget(self.n_j, 2, 3)
        label = QLabel('K')
        layout.addWidget(label, 3, 0)
        self.u_k = QLineEdit()
        layout.addWidget(self.u_k, 3, 1)
        self.v_k = QLineEdit()
        layout.addWidget(self.v_k, 3, 2)
        self.n_k = QLineEdit()
        layout.addWidget(self.n_k, 3, 3)
        self.validate_btn = QPushButton('Validate')
        layout.addWidget(self.validate_btn, 4, 2)
        frame2.setLayout(layout)
        frame2.move(10, 120)

        #######################################################################
        #                                                                     #
        #######################################################################

        self.model_position = self.createPositionModel(self)
        self.list_position_tree = QTreeView(frame1)
        self.list_position_tree.setModel(self.model_position)
        self.list_position_tree.setGeometry(10, 250, 860, 180)
        #######################################################################
        #                                                                     #
        #######################################################################
        frame1.setFrameStyle(1)
        splitter.addWidget(label1)
        splitter.addWidget(frame1)
        splitter.setGeometry(10, 100, 880, 450)
        #######################################################################
        #                                                                     #
        #######################################################################
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
        frame1.setGeometry(240, 555, 400, 40)

        self.validate_btn.clicked.connect(self.validate_position)
        self.list_position_tree.doubleClicked.connect(self.del_position)
        self.transfer_btn.clicked.connect(self.transfer)
        self.save_btn.clicked.connect(self.save)
        self.list_position_tree.clicked.connect(self.viewPosition)
        self.cancel_btn.clicked.connect(self.cancel)

    def cancel(self):
        self.model_position.removeRows(0, self.model_position.rowCount())
        type_tank = self.tank_type.currentText()
        num_tank = self.tank_num.currentText()
        if not type_tank.isspace() and type_tank != '' and not num_tank.isspace() and num_tank != '':
            tk_np = '_'.join([type_tank, num_tank])
            self.initPos(tk_np)
            sql = """SELECT pot.num_loc, pot.ref, pot.coord[1], pot.coord[2], pot.coord[3], pot.metric[1][1], pot.metric[2][1], pot.metric[3][1], pot.metric[1][2], pot.metric[2][2], pot.metric[3][2], pot.metric[1][3], pot.metric[2][3], pot.metric[3][3] 
                             FROM position_on_tank pot 
                                JOIN tank tk ON pot.id_tank = tk.id
                                JOIN type_tank tt ON tt.id = tk.id_type_tank
                             WHERE tt.ref = %s AND tk.number = %s 
                    ;"""
            self.cur.execute(sql, (type_tank, num_tank))
            self.conn.commit()
            rows = self.cur.fetchall()
            for row in rows:
                self.addPosition(*(row[0:]))

    def save(self):
        type_tank = self.tank_type.currentText()
        num_tank = self.tank_num.currentText()
        if not type_tank.isspace() and type_tank != '' and not num_tank.isspace() and num_tank != '':
            file_name = '_'.join([type_tank, num_tank])

            with open(f'.\\file\\tank\\{file_name}_pos.csv', 'a') as f:
                try:
                    pass
                finally:
                    f.close()

            lines = []
            for i in range(self.model_position.rowCount()):
                loc = self.model_position.data(self.model_position.index(i, 0))
                ref = self.model_position.data(self.model_position.index(i, 1))
                x = self.model_position.data(self.model_position.index(i, 2))
                y = self.model_position.data(self.model_position.index(i, 3))
                z = self.model_position.data(self.model_position.index(i, 4))
                u_i = self.model_position.data(self.model_position.index(i, 5))
                u_j = self.model_position.data(self.model_position.index(i, 6))
                u_k = self.model_position.data(self.model_position.index(i, 7))
                v_i = self.model_position.data(self.model_position.index(i, 8))
                v_j = self.model_position.data(self.model_position.index(i, 9))
                v_k = self.model_position.data(self.model_position.index(i, 10))
                n_i = self.model_position.data(self.model_position.index(i, 11))
                n_j = self.model_position.data(self.model_position.index(i, 12))
                n_k = self.model_position.data(self.model_position.index(i, 13))
                lines.append([loc, ref, x, y, z, u_i, u_j, u_k, v_i, v_j, v_k, n_i, n_j, n_k])

            with open(f'.\\file\\tank\\{file_name}_pos.csv', 'w', newline='') as f:
                try:
                    writer = csv.writer(f)
                    writer.writerows(lines)
                finally:
                    f.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Tank is not identified\nIdentify which tank")
            msg.setWindowTitle("Error Identify")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return

    def viewPosition(self):
        if self.list_position_tree.selectedIndexes()[0]:
            select_row = self.list_position_tree.selectedIndexes()[0].row()
            loc = self.model_position.data(self.model_position.index(select_row, 0))
            ref = self.model_position.data(self.model_position.index(select_row, 1))
            x = self.model_position.data(self.model_position.index(select_row, 2))
            y = self.model_position.data(self.model_position.index(select_row, 3))
            z = self.model_position.data(self.model_position.index(select_row, 4))
            u_i = self.model_position.data(self.model_position.index(select_row, 5))
            u_j = self.model_position.data(self.model_position.index(select_row, 6))
            u_k = self.model_position.data(self.model_position.index(select_row, 7))
            v_i = self.model_position.data(self.model_position.index(select_row, 8))
            v_j = self.model_position.data(self.model_position.index(select_row, 9))
            v_k = self.model_position.data(self.model_position.index(select_row, 10))
            n_i = self.model_position.data(self.model_position.index(select_row, 11))
            n_j = self.model_position.data(self.model_position.index(select_row, 12))
            n_k = self.model_position.data(self.model_position.index(select_row, 13))

            self.loc_num.setCurrentText(loc)
            self.sensor_coating_ref.setCurrentText(ref)
            self.x.setText(str(x))
            self.y.setText(str(y))
            self.z.setText(str(z))
            self.u_i.setText(str(u_i))
            self.u_j.setText(str(u_j))
            self.u_k.setText(str(u_k))
            self.v_i.setText(str(v_i))
            self.v_j.setText(str(v_j))
            self.v_k.setText(str(v_k))
            self.n_i.setText(str(n_i))
            self.n_j.setText(str(n_j))
            self.n_k.setText(str(n_k))

    def del_position(self):
        type_tank = self.tank_type.currentText()
        num_tank = self.tank_num.currentText()
        if (type_tank.isspace() or type_tank == '') or (num_tank.isspace() or num_tank == ''):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Tank is not identified\nIdentify which tank")
            msg.setWindowTitle("Error Identify")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            return
        select_pos = self.list_position_tree.selectedIndexes()[0].row()
        self.loc_num.removeItem(select_pos)
        loc = self.model_position.data(self.model_position.index(select_pos, 0))
        ref = self.model_position.data(self.model_position.index(select_pos, 1))
        x = self.model_position.data(self.model_position.index(select_pos, 2))
        y = self.model_position.data(self.model_position.index(select_pos, 3))
        z = self.model_position.data(self.model_position.index(select_pos, 4))
        u_i = self.model_position.data(self.model_position.index(select_pos, 5))
        u_j = self.model_position.data(self.model_position.index(select_pos, 6))
        u_k = self.model_position.data(self.model_position.index(select_pos, 7))
        v_i = self.model_position.data(self.model_position.index(select_pos, 8))
        v_j = self.model_position.data(self.model_position.index(select_pos, 9))
        v_k = self.model_position.data(self.model_position.index(select_pos, 10))
        n_i = self.model_position.data(self.model_position.index(select_pos, 11))
        n_j = self.model_position.data(self.model_position.index(select_pos, 12))
        n_k = self.model_position.data(self.model_position.index(select_pos, 13))
        self.model_position.removeRow(select_pos)
        if self.tank_current.findPos(loc) is not None:
            self.tank_delete.addPos(loc, ref, x, y, z, u_i, u_j, u_k, v_i, v_j, v_k, n_i, n_j, n_k)
            self.tank_current.delPos(loc)
        if self.tank_create.findPos(loc) is not None:
            self.tank_create.delPos(loc)
        self.loc_num.setCurrentText('')
        self.sensor_coating_ref.setCurrentText('')
        self.x.setText('')
        self.y.setText('')
        self.z.setText('')
        self.u_i.setText('')
        self.u_j.setText('')
        self.u_k.setText('')
        self.v_i.setText('')
        self.v_j.setText('')
        self.v_k.setText('')
        self.n_i.setText('')
        self.n_j.setText('')
        self.n_k.setText('')

    def createPositionModel(self, parent):
        model = QStandardItemModel(0, 14, parent)
        model.setHeaderData(0, Qt.Horizontal, 'Location')
        model.setHeaderData(1, Qt.Horizontal, 'Reference')
        model.setHeaderData(2, Qt.Horizontal, 'X')
        model.setHeaderData(3, Qt.Horizontal, 'Y')
        model.setHeaderData(4, Qt.Horizontal, 'Z')
        model.setHeaderData(5, Qt.Horizontal, '<U,I>')
        model.setHeaderData(6, Qt.Horizontal, '<U,J>')
        model.setHeaderData(7, Qt.Horizontal, '<U,K>')
        model.setHeaderData(8, Qt.Horizontal, '<V,I>')
        model.setHeaderData(9, Qt.Horizontal, '<V,J>')
        model.setHeaderData(10, Qt.Horizontal, '<V,K>')
        model.setHeaderData(11, Qt.Horizontal, '<N,I>')
        model.setHeaderData(12, Qt.Horizontal, '<N,J>')
        model.setHeaderData(13, Qt.Horizontal, '<N,K>')
        return model

    def addPosition(self, loc, ref, x, y, z, u_i, u_j, u_k, v_i, v_j, v_k, n_i, n_j, n_k):
        self.model_position.insertRow(self.model_position.rowCount())
        row = self.model_position.rowCount() - 1
        self.model_position.setData(self.model_position.index(row, 0), loc)
        self.model_position.setData(self.model_position.index(row, 1), ref)
        self.model_position.setData(self.model_position.index(row, 2), x)
        self.model_position.setData(self.model_position.index(row, 3), y)
        self.model_position.setData(self.model_position.index(row, 4), z)
        self.model_position.setData(self.model_position.index(row, 5), u_i)
        self.model_position.setData(self.model_position.index(row, 6), u_j)
        self.model_position.setData(self.model_position.index(row, 7), u_k)
        self.model_position.setData(self.model_position.index(row, 8), v_i)
        self.model_position.setData(self.model_position.index(row, 9), v_j)
        self.model_position.setData(self.model_position.index(row, 10), v_k)
        self.model_position.setData(self.model_position.index(row, 11), n_i)
        self.model_position.setData(self.model_position.index(row, 12), n_j)
        self.model_position.setData(self.model_position.index(row, 13), n_k)

    def validate_position(self):
        type_tank = self.tank_type.currentText()
        num_tank = self.tank_num.currentText()
        loc = self.loc_num.currentText()
        ref = self.sensor_coating_ref.currentText()
        x = self.x.text()
        y = self.y.text()
        z = self.z.text()
        u_i = self.u_i.text()
        u_j = self.u_j.text()
        u_k = self.u_k.text()
        v_i = self.v_i.text()
        v_j = self.v_j.text()
        v_k = self.v_k.text()
        n_i = self.n_i.text()
        n_j = self.n_j.text()
        n_k = self.n_k.text()
        if not loc.isspace() and loc != '' and not ref.isspace() and ref != '' and not x.isspace() and x != '' and not y.isspace() and y != '' and not z.isspace() and z != '' and not u_i.isspace() and u_i != '' and not u_j.isspace() and u_j != '' and not u_k.isspace() and u_k != '' and not v_i.isspace() and v_i != '' and not v_j.isspace() and v_j != '' and not v_k.isspace() and v_k != '' and not n_i.isspace() and n_i != '' and not n_j.isspace() and n_j != '' and not n_k.isspace() and n_k != '':
            if not type_tank.isspace() and type_tank != '' and not num_tank.isspace() and num_tank != '':
                if loc not in [self.loc_num.itemText(i) for i in range(self.loc_num.count())]:
                    self.loc_num.addItem(loc)
                    self.addPosition(loc, ref, x, y, z, u_i, u_j, u_k, v_i, v_j, v_k, n_i, n_j, n_k)
                    self.tank_create.addPos(loc, ref, x, y, z, u_i, u_j, u_k, v_i, v_j, v_k, n_i, n_j, n_k)
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("This position is identified\nTry other positon")
                    msg.setWindowTitle("Error Identify")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                    return
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Test mean is not identified\nIdentify which test mean")
                msg.setWindowTitle("Error Identify")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
                return

    def eventFilter(self, obj, event):
        if obj == self.tank_type:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                type_tank = []
                if 'manager' in [i[0] for i in self.lst]:
                    sql = """SELECT DISTINCT ref FROM type_tank;"""
                    self.cur.execute(sql)
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    for row in rows:
                        type_tank.append(row[0])
                else:
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
                    for row in rows:
                        l = [row[0]]
                        if row[1] is not None:
                            for i in row[1].split('-'):
                                l.append(i)
                        self.lst.append(l)
                    self.lst = [[i[0], i[2]] for i in self.lst if i[1] == "tank"]
                    for i in self.lst:
                        if i[1] not in type_tank:
                            type_tank.append(i[1])
                self.tank_type.clear()
                self.tank_type.addItems(type_tank)
                self.tank_type.showPopup()
                self.tank_type.view().viewport().installEventFilter(self)
                return True
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return):
                type_tank = self.tank_type.currentText()
                if not type_tank.isspace() and type_tank != '':
                    tank_num = []
                    sql = """SELECT t.number 
                                FROM tank t
                                JOIN type_tank tk ON t.id_type_tank = tk.id
                                WHERE tk.ref = %s;"""
                    self.cur.execute(sql, (type_tank,))
                    self.conn.commit()

                    rows = self.cur.fetchall()
                    for row in rows:
                        tank_num.append(str(row[0]))
                    self.tank_num.clear()
                    self.tank_num.addItems(tank_num)
                    self.tank_num.setCurrentText('')
                self.tank_num.setFocus()
                return True
            return False
        if obj == self.tank_type.view().viewport():
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                index = self.tank_type.view().currentIndex().row()
                type_tank = self.tank_type.itemText(index)
                tank_num = []
                sql = """SELECT t.number 
                            FROM tank t
                            JOIN type_tank tk ON t.id_type_tank = tk.id
                            WHERE tk.ref = %s;"""
                self.cur.execute(sql, (type_tank,))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows:
                    tank_num.append(str(row[0]))
                self.tank_num.clear()
                self.tank_num.addItems(tank_num)
                self.tank_num.setCurrentText('')
                self.tank_num.setFocus()
                return True
            return False

        if obj == self.tank_num:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.tank_num.showPopup()
                self.tank_num.view().viewport().installEventFilter(self)
                return True
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return):
                num_tank = self.tank_num.currentText()
                type_tank = self.tank_type.currentText()
                if not type_tank.isspace() and type_tank != '' and not num_tank.isspace() and num_tank != '':
                    num_loc = []
                    sql = """SELECT DISTINCT pot.num_loc
                             FROM position_on_tank pot
                                JOIN tank tk ON tk.id = pot.id_tank
                                JOIN type_tank tt ON tt.id = tk.id_type_tank
                             WHERE tt.ref = %s AND tk.number = %s;"""
                    self.cur.execute(sql, (type_tank, num_tank))
                    self.conn.commit()

                    rows = self.cur.fetchall()
                    for row in rows:
                        num_loc.append(row[0])
                    self.loc_num.clear()
                    self.loc_num.addItems(num_loc)
                    self.loc_num.setCurrentText('')
                    sql = """SELECT pot.num_loc, pot.ref, pot.coord[1], pot.coord[2], pot.coord[3], pot.metric[1][1], pot.metric[2][1], pot.metric[3][1], pot.metric[1][2], pot.metric[2][2], pot.metric[3][2], pot.metric[1][3], pot.metric[2][3], pot.metric[3][3] 
                             FROM position_on_tank pot 
                                JOIN tank tk ON pot.id_tank = tk.id
                                JOIN type_tank tt ON tt.id = tk.id_type_tank
                             WHERE tt.ref = %s AND tk.number = %s 
                    ;"""
                    self.cur.execute(sql, (type_tank, num_tank))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    self.model_position.removeRows(0, self.model_position.rowCount())
                    for row in rows:
                        self.addPosition(*(row[0:]))

                    tk_np = '_'.join([type_tank, num_tank])
                    self.initPos(tk_np)
                self.loc_num.setFocus()
                return True
            return False
        if obj == self.tank_num.view().viewport():
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                index = self.tank_num.view().currentIndex().row()
                num_tank = self.tank_num.itemText(index)
                type_tank = self.tank_type.currentText()
                num_loc = []
                sql = """SELECT DISTINCT pot.num_loc
                            FROM position_on_tank pot
                            JOIN tank tk ON tk.id = pot.id_tank
                            JOIN type_tank tt ON tt.id = tk.id_type_tank
                            WHERE tt.ref = %s AND tk.number = %s;"""
                self.cur.execute(sql, (type_tank, num_tank))
                self.conn.commit()

                rows = self.cur.fetchall()
                for row in rows:
                    num_loc.append(row[0])
                self.loc_num.clear()
                self.loc_num.addItems(num_loc)
                self.loc_num.setCurrentText('')
                sql = """SELECT pot.num_loc, pot.ref, pot.coord[1], pot.coord[2], pot.coord[3], pot.metric[1][1], pot.metric[2][1], pot.metric[3][1], pot.metric[1][2], pot.metric[2][2], pot.metric[3][2], pot.metric[1][3], pot.metric[2][3], pot.metric[3][3] 
                            FROM position_on_tank pot 
                            JOIN tank tk ON pot.id_tank = tk.id
                            JOIN type_tank tt ON tt.id = tk.id_type_tank
                            WHERE tt.ref = %s AND tk.number = %s 
                ;"""
                self.cur.execute(sql, (type_tank, num_tank))
                self.conn.commit()
                rows = self.cur.fetchall()
                self.model_position.removeRows(0, self.model_position.rowCount())
                for row in rows:
                    self.addPosition(*(row[0:]))
                tk_np = '_'.join([type_tank, num_tank])
                self.initPos(tk_np)
                self.loc_num.setFocus()
                return True
            return False

        if obj == self.loc_num:
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self.loc_num.showPopup()
                self.loc_num.view().viewport().installEventFilter(self)
                return True
            if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Tab or event.key() == Qt.Key_Return):
                num_tank = self.tank_num.currentText()
                type_tank = self.tank_type.currentText()
                loc_num = self.loc_num.currentText()
                if not type_tank.isspace() and type_tank != '' and not num_tank.isspace() and num_tank != '' and not loc_num.isspace() and loc_num != '':
                    sql = """SELECT pot.ref, pot.coord[1], pot.coord[2], pot.coord[3], pot.metric[1][1], pot.metric[2][1], pot.metric[3][1], pot.metric[1][2], pot.metric[2][2], pot.metric[3][2], pot.metric[1][3], pot.metric[2][3], pot.metric[3][3] 
                             FROM position_on_tank pot 
                                JOIN tank tk ON pot.id_tank = tk.id
                                JOIN type_tank tt ON tt.id = tk.id_type_tank
                             WHERE tt.ref = %s AND tk.number = %s AND pot.num_loc = %s
                    ;"""
                    self.cur.execute(sql, (type_tank, num_tank, loc_num))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    for row in rows:
                        self.sensor_coating_ref.setCurrentText(row[0])
                        self.x.setText(str(row[1]))
                        self.y.setText(str(row[2]))
                        self.z.setText(str(row[3]))
                        self.u_i.setText(str(row[4]))
                        self.u_j.setText(str(row[5]))
                        self.u_k.setText(str(row[6]))
                        self.v_i.setText(str(row[7]))
                        self.v_j.setText(str(row[8]))
                        self.v_k.setText(str(row[9]))
                        self.n_i.setText(str(row[10]))
                        self.n_j.setText(str(row[11]))
                        self.n_k.setText(str(row[12]))

                self.sensor_coating_ref.setFocus()
                return True
            return False
        if obj == self.loc_num.view().viewport():
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                index = self.loc_num.view().currentIndex().row()
                loc_num = self.loc_num.itemText(index)
                num_tank = self.tank_num.currentText()
                type_tank = self.tank_type.currentText()
                sql = """SELECT pot.ref, pot.coord[1], pot.coord[2], pot.coord[3], pot.metric[1][1], pot.metric[2][1], pot.metric[3][1], pot.metric[1][2], pot.metric[2][2], pot.metric[3][2], pot.metric[1][3], pot.metric[2][3], pot.metric[3][3] 
                             FROM position_on_tank pot 
                                JOIN tank tk ON pot.id_tank = tk.id
                                JOIN type_tank tt ON tt.id = tk.id_type_tank
                             WHERE tt.ref = %s AND tk.number = %s AND pot.num_loc = %s
                    ;"""
                self.cur.execute(sql, (type_tank, num_tank, loc_num))
                self.conn.commit()
                rows = self.cur.fetchall()
                for row in rows:
                    self.sensor_coating_ref.setCurrentText(row[0])
                    self.x.setText(str(row[1]))
                    self.y.setText(str(row[2]))
                    self.z.setText(str(row[3]))
                    self.u_i.setText(str(row[4]))
                    self.u_j.setText(str(row[5]))
                    self.u_k.setText(str(row[6]))
                    self.v_i.setText(str(row[7]))
                    self.v_j.setText(str(row[8]))
                    self.v_k.setText(str(row[9]))
                    self.n_i.setText(str(row[10]))
                    self.n_j.setText(str(row[11]))
                    self.n_k.setText(str(row[12]))
                self.sensor_coating_ref.setFocus()
                return True
            return False
        return False

    def initPos(self, tk_np):
        tk = position(tk_np)
        self.tank_current = deepcopy(tk)
        self.tank_create = deepcopy(tk)
        self.tank_delete = deepcopy(tk)

        sql = """SELECT pot.num_loc, pot.ref, pot.coord[1], pot.coord[2], pot.coord[3], pot.metric[1][1], pot.metric[2][1], pot.metric[3][1], pot.metric[1][2], pot.metric[2][2], pot.metric[3][2], pot.metric[1][3], pot.metric[2][3], pot.metric[3][3] 
                FROM position_on_tank pot 
                JOIN tank tk ON pot.id_tank = tk.id
                JOIN type_tank tt ON tt.id = tk.id_type_tank
                WHERE tt.ref = %s AND tk.number = %s 
        ;"""

        self.cur.execute(sql, tuple(tk_np.split('_')))
        self.conn.commit()
        rows = self.cur.fetchall()
        for row in rows:
            self.tank_current.addPos(*(row[0:]))
        self.tank_update = deepcopy(self.tank_current)

    def transfer(self):
        type_tank = self.tank_type.currentText()
        num_tank = self.tank_num.currentText()
        try:
            if 'manager' in [i[0] for i in self.lst] or 'admin' in [i[0] for i in self.lst] or 'validate' in [i[0] for i
                                                                                                              in
                                                                                                              self.lst]:
                sql = """SELECT t.id_type_tank, t.number FROM tank t JOIN type_tank tt ON t.id_type_tank = tt.id WHERE tt.ref = %s AND t.number = %s"""
                self.cur.execute(sql, (type_tank, num_tank))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == []:
                    sql = """INSERT INTO tank(id_type_tank, number, validate) VALUES ((SELECT id FROM type_tank WHERE ref = %s), %s, %s);"""
                    self.cur.execute(sql, (type_tank, num_tank, 't'))
                    self.conn.commit()

                for i in self.tank_create.position:
                    sql = """SELECT * FROM position_on_tank pot JOIN tank t ON pot.id_tank = t.id JOIN type_tank tt ON tt.id = t.id_type_tank WHERE tt.ref = %s AND t.number = %s AND pot.num_loc = %s"""
                    self.cur.execute(sql, (type_tank, num_tank, i[0]))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    if rows == []:
                        sql = """INSERT INTO position_on_tank(id_tank, num_loc, ref, coord, metric, validate) VALUES ((SELECT t.id from tank t JOIN type_tank tt ON t.id_type_tank = tt.id WHERE tt.ref = %s AND t.number = %s), %s, %s, '{%s, %s, %s}', '{{%s, %s, %s},{%s, %s, %s},{%s, %s, %s}}', %s);"""
                        self.cur.execute(sql, (
                        type_tank, num_tank, i[0], i[1], int(i[2]), int(i[3]), int(i[4]), int(i[5]), int(i[8]),
                        int(i[11]), int(i[6]), int(i[9]), int(i[12]), int(i[7]), int(i[10]), int(i[13]), 't'))
                        self.conn.commit()
                    else:
                        sql = """UPDATE position_on_tank 
                                 SET validate = 't' 
                                 WHERE id_tank = (SELECT t.id from tank t JOIN type_tank tt ON t.id_type_tank = tt.id WHERE tt.ref = %s AND t.number = %s) AND num_loc = %s;
                        """
                        self.cur.execute(sql, (type_tank, num_tank, i[0]))
                        self.conn.commit()
                for i in self.tank_update.position:
                    sql = """UPDATE position_on_tank
                                 SET validate = 't' 
                                 WHERE id_tank = (SELECT t.id from tank t JOIN type_tank tt ON t.id_type_tank = tt.id WHERE tt.ref = %s AND t.number = %s) AND num_loc = %s;
                        """
                    self.cur.execute(sql, (type_tank, num_tank, i[0]))
                    self.conn.commit()

                for i in self.tank_delete.position:
                    sql = """DELETE FROM position_on_tank WHERE id_tank = (SELECT t.id FROM tank t JOIN type_tank tt ON t.id_type_tank = tt.id WHERE tt.ref = %s AND t.number = %s) AND num_loc = %s"""
                    self.cur.execute(sql, (type_tank, num_tank, i[0]))
                    self.conn.commit()
        except:
            pass
        try:
            if 'create' in [i[0] for i in self.lst]:
                sql = """SELECT t.id_type_tank, t.number FROM tank t JOIN type_tank tt ON t.id_type_tank = tt.id WHERE tt.ref = %s AND t.number = %s"""
                self.cur.execute(sql, (type_tank, num_tank))
                self.conn.commit()
                rows = self.cur.fetchall()
                if rows == []:
                    sql = """INSERT INTO tank(id_type_tank, number, validate) VALUES ((SELECT id FROM type_tank WHERE ref = %s), %s, %s);"""
                    self.cur.execute(sql, (type_tank, num_tank, 'f'))
                    self.conn.commit()

                for i in self.tank_create.position:
                    sql = """SELECT * FROM position_on_tank WHERE num_loc = %s AND id_tank = (SELECT t.id from tank t JOIN type_tank tt ON t.id_type_tank = tt.id WHERE tt.ref = %s AND t.number = %s); """
                    self.cur.execute(sql, (i[0], type_tank, num_tank))
                    self.conn.commit()
                    rows = self.cur.fetchall()
                    if rows == []:
                        sql = """INSERT INTO position_on_tank(id_tank, num_loc, ref, coord, metric, validate) VALUES ((SELECT t.id from tank t JOIN type_tank tt ON t.id_type_tank = tt.id WHERE tt.ref = %s AND t.number = %s), %s, %s, '{%s, %s, %s}', '{{%s, %s, %s},{%s, %s, %s},{%s, %s, %s}}', %s);"""
                        self.cur.execute(sql, (
                        type_tank, num_tank, i[0], i[1], int(i[2]), int(i[3]), int(i[4]), int(i[5]), int(i[8]),
                        int(i[11]), int(i[6]), int(i[9]), int(i[12]), int(i[7]), int(i[10]), int(i[13]), 'f'))
                        self.conn.commit()
                for i in self.tank_delete.position:
                    sql = """DELETE FROM position_on_tank WHERE id_tank = (SELECT t.id FROM tank t JOIN type_tank tt ON t.id_type_tank = tt.id WHERE tt.ref = %s AND t.number = %s) AND num_loc = %s"""
                    self.cur.execute(sql, (type_tank, num_tank, i[0]))
                    self.conn.commit()
        except:
            pass

        self.model_position.removeRows(0, self.model_position.rowCount())
        self.loc_num.setCurrentText('')
        self.sensor_coating_ref.setCurrentText('')
        self.x.setText('')
        self.y.setText('')
        self.z.setText('')
        self.u_i.setText('')
        self.u_j.setText('')
        self.u_k.setText('')
        self.v_i.setText('')
        self.v_j.setText('')
        self.v_k.setText('')
        self.n_i.setText('')
        self.n_j.setText('')
        self.n_k.setText('')
        self.tank_type.setCurrentText('')
        self.tank_num.setCurrentText('')

    def connect(self):
        try:
            host = "localhost"
            username = "iventre"
            dbname = "lmsm"
            password = "lmsm"
            self.conn = psycopg2.connect(host=host, user=username, dbname=dbname, password=password)
            self.cur = self.conn.cursor()
        except psycopg2.Error as err:
            print(str(err))
