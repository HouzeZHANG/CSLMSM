"""
https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/
"""
import cleansky_LMSM.common.database as database
from enum import Enum
import logging


class DataType(Enum):
    serial = 'serial'
    integer = 'integer'
    varchar = 'varchar'
    boolean = 'boolean'


type_list_def = ({
    # account
    'id': DataType.serial,
    'uname': DataType.varchar,
    'orga': DataType.varchar,
    'fname': DataType.varchar,
    'lname': DataType.varchar,
    'tel': DataType.varchar,
    'email': DataType.varchar,
    'password': DataType.varchar,
    # user_right:
    'id_account': DataType.integer,
    'role': DataType.integer,
    'id_test_mean': DataType.integer,
    'id_type_coating': DataType.integer,
    'id_type_detergent': DataType.integer,
    'id_type_tank': DataType.integer,
    'id_type_sensor': DataType.integer,
    'id_type_ejector': DataType.integer,
    'id_type_camera': DataType.integer,
    'id_type_test_point': DataType.integer,
    'id_type_intrinsic_value': DataType.integer,
    'id_test_team': DataType.integer,
    'insect': DataType.boolean,
    'acqui_system': DataType.boolean
},)

type_no_str = [DataType.serial, DataType.integer]


class Model:
    def __init__(self, db_object=None, transaction_mode=None):
        self.__transaction_mode = transaction_mode
        self.__db = db_object
        self.__controller = None

        # field name of table user_right
        self.field_name = {
            0: 'test_mean',
            1: 'type_coating',
            2: 'type_detergent',
            3: 'type_tank',
            4: 'type_sensor',
            5: 'type_ejector',
            6: 'type_camera',
            7: 'type_test_point',
            8: 'type_intrinsic_value',
            9: 'test_team',
            10: 'insect',
            11: 'acqui_system'
        }

    def set_controller(self, controller_obj):
        self.__controller = controller_obj

    def get_db(self):
        return self.__db

    # little tools
    @staticmethod
    def tools_get_field_str_insert(locals_dict, type_list=type_list_def):
        field_str, value_str = "", ""
        if locals_dict is None:
            return "", ""
        for key in locals_dict.keys():
            if key != 'self' and locals_dict[key] is not None:
                field_str += (key + ', ')
                if key in type_list[0].keys():
                    if type_list[0][key] in type_no_str:
                        value_str += (str(locals_dict[key]) + ', ')
                    else:
                        value_str += ("'" + str(locals_dict[key]) + "', ")
                else:
                    value_str += ("'" + str(locals_dict[key]) + "', ")
        field_str = field_str[:-2]
        value_str = value_str[:-2]
        return field_str, value_str

    @staticmethod
    def tools_get_field_str_update(locals_dict, type_list=type_list_def):
        field_str = ""
        if locals_dict is None:
            return ""
        for key in locals_dict.keys():
            if key != 'self' and locals_dict[key] is not None:
                if key in type_list[0].keys():
                    if type_list[0][key] in type_no_str:
                        field_str += (key + ' = ' + str(locals_dict[key]) + ', ')
                    else:
                        field_str += (key + " = '" + str(locals_dict[key]) + "', ")
                else:
                    field_str += (key + " = '" + str(locals_dict[key]) + "', ")
        field_str = field_str[:-2]
        return field_str

    # dcl interface
    def model_start_transaction(self):
        self.tcl_template("START TRANSACTION")

    def model_roll_back(self):
        self.tcl_template("ROLLBACK")

    def model_commit(self):
        self.tcl_template("COMMIT")

    # sql template pattern
    def tcl_template(self, dcl, error_info='dcl error'):
        try:
            cursor = self.get_db().get_connect().cursor()
            cursor.execute(dcl)
            self.get_db().get_connect().commit()
            cursor.close()
        except Exception:
            print(error_info)

    def dql_template(self, dql, error_info='dql error'):
        result = []
        try:
            cursor = self.get_db().get_connect().cursor()
            cursor.execute(dql)
            result = cursor.fetchall()
            cursor.close()
            logging.info('dql success')
        except Exception:
            logging.error(error_info)
        return result

    def dml_template(self, dml, error_info='dml error'):
        try:
            cursor = self.get_db().get_connect().cursor()
            cursor.execute(dml)
            self.get_db().get_connect().commit()
            cursor.close()
        except Exception:
            print(error_info)

    def model_get_all_rights(self):
        sql = """
                select * from user_right
        """
        return self.dql_template(sql)

    def model_get_role_ref(self, role_id):
        sql = """
                select ref from type_role where id = {0}
        """.format(role_id)
        return self.dql_template(sql)

    def model_get_mean(self, mean_id):
        sql = """
                select concat(t1.type, '_',t1.name, '_',t1.number)
                from test_mean as t1
                where t1.id = {0}
        """.format(mean_id)
        return self.dql_template(sql)

    def model_get_simple_ele(self, table_name, ele_id):
        sql = """
                select t1.ref
                from {0} t1
                where t1.id = {1}
        """.format(table_name, ele_id)
        print(sql)
        return self.dql_template(sql)

    def tools_get_elements_info(self, lis):
        """
        input [user_id, role_id, ele_type(-2), ele_id]  (number)
                or
        input [role_id, ele_type(-2), ele_id] (number)

        output [ele_type, ele_id, role] (str)
        """
        info = []
        table_name = self.field_name[lis[-2]]
        info.append(table_name)

        if lis[-2] == 0:
            # our element is test_mean type
            info.append(self.model_get_mean(lis[-1])[0][0])
        elif lis[-2] == 10 or lis[-2] == 11:
            # our element is boolean type
            if lis[-1] is True:
                info.append('True')
            else:
                info.append('False')
        else:
            # else types
            info.append(self.model_get_simple_ele(table_name, lis[-1])[0][0])
        info.append(self.model_get_role_ref(lis[0])[0][0])
        return info

    def model_get_username_by_uid(self, uid):
        sql = """
                select uname
                from account
                where id = {0}
        """.format(uid)
        return self.dql_template(sql)


class LoginModel(Model):
    def model_login(self, username, password):
        """
        Obtain user information
        if our username not exists in table account or the password is wrong, return []
        """
        sql = """
                select *
                from account
                where uname = '{0}' and password = '{1}'
        """.format(username, password)
        return self.dql_template(dql=sql)


class MenuModel(Model):
    pass


class ManagementModel(Model):
    def model_get_uid_by_uname(self, uname):
        sql = """
            select id from account where uname='{0}'
        """.format(uname)
        return self.dql_template(sql)

    def model_get_orga(self):
        """Returns a de-redo record of the orga field in the Account table directly as a Python list data structure"""
        sql = """
                select
                distinct a.orga
                from
                account as a
                order by
                a.orga asc
        """
        return self.dql_template(dql=sql, error_info="model get_orga error")

    def model_get_list_of_users(self):
        """The query displays the List of users table"""
        sql = """
                select
                a.orga, a.uname, a.email, a.fname, a.lname, a.tel
                from
                account as a
                order by
                a.orga asc, a.uname asc
        """
        return self.dql_template(dql=sql)

    def model_get_username_and_lastname(self, organisation):
        """by page 3 <les listes dependants>"""
        sql = """
                select uname,lname
                from account
                where orga='{0}'
        """.format(organisation)
        return self.dql_template(dql=sql)

    def model_get_list_of_users_by_organisation(self, organisation):
        sql = """
                select uname
                from account
                where orga = '{0}'
        """.format(organisation)
        return self.dql_template(sql)

    def model_get_first_name_and_lastname(self, username):
        """by page 3 <les listes dependants>"""
        sql = """
                select fname,lname
                from account
                where uname = '{0}'
        """.format(username)
        return self.dql_template(dql=sql)

    def model_get_firstname(self, lastname):
        """by page 3 <les listes depandants>"""
        sql = """
                select lname
                from account
                where lname = '{0}'
        """.format(lastname)
        return self.dql_template(dql=sql)

    def model_create_new_user(self, uname, orga=None, fname=None, lname=None, tel=None,
                              email=None, password=None):
        self.model_insert_table_account(uname=uname, orga=orga, fname=fname, lname=lname,
                                        tel=tel, email=email, password=password)
        self.model_insert_table_user_right(id_account=self.model_get_user_id(uname=uname)[0][0], role=6)

    def model_insert_table_account(self, uname, orga=None, fname=None, lname=None,
                                   tel=None, email=None, password=None):
        """by page 5"""
        tup = Model.tools_get_field_str_insert(locals())
        sql = """
                insert into account ({0})
                values ({1})
        """.format(tup[0], tup[1])
        self.dml_template(dml=sql)

    def model_insert_table_user_right(self, id_account, role, id_test_mean=None, id_type_coating=None,
                                      id_type_detergent=None, id_type_tank=None, id_type_sensor=None,
                                      id_type_ejector=None, id_type_camera=None, id_type_test_point=None,
                                      id_type_intrinsic_value=None, id_test_team=None, insect=None, acqui_system=None):
        """
        role=6，无权限，不去重，有可能会重复添加权限
        插入的布尔类型参数'true' or 'false'
        """
        tup = Model.tools_get_field_str_insert(locals())
        sql = """
                insert into user_right({0})
                values ({1})
        """.format(tup[0], tup[1])
        self.dml_template(dml=sql)

    def model_get_user_id(self, uname):
        sql = """
                select id from account where uname = '{0}'
        """.format(uname)
        return self.dql_template(dql=sql)

    def model_user_have_role(self, uid):
        sql = """
                select role from user_right where id_account={0}
        """.format(uid)
        return self.dql_template(sql)

    def model_delete_user(self, uname):
        sql = """
                delete from account where uname = '{0}'
        """.format(uname)
        self.dml_template(sql)

    @staticmethod
    def model_update_user_pre(uname=None, orga=None, fname=None, lname=None, tel=None, email=None, password=None):
        return Model.tools_get_field_str_update(locals())

    def model_update_user(self, uname, new_username=None, organisation=None, last_name=None, first_name=None,
                          email=None, tel=None, password=None):
        """
        通过适配器来去除uname，提供全新的update接口
        """
        tup = ManagementModel.model_update_user_pre(uname=new_username, orga=organisation, lname=last_name,
                                                    fname=first_name, email=email, tel=tel, password=password)
        sql = """
                update account
                set {1}
                where uname = '{0}'
        """.format(uname, tup)
        self.dml_template(sql)

    def model_get_coatings(self):
        sql = """
                select ref
                from type_coating
                order by ref asc
        """
        return self.dql_template(sql)

    def model_get_detergent(self):
        sql = """
                select ref
                from type_detergent
                order by ref asc
        """
        return self.dql_template(sql)

    def model_get_insect(self):
        pass

    def model_get_means(self):
        sql = """
                select distinct type
                from test_mean
                order by type asc
        """
        return self.dql_template(sql)

    def model_get_tank(self):
        sql = """
                select ref
                from type_tank
                order by ref asc
        """
        return self.dql_template(sql)

    def model_get_sensor(self):
        sql = """
                select ref
                from type_sensor
                order by ref asc
        """
        return self.dql_template(sql)

    def model_get_acqui(self):
        pass

    def model_get_ejector(self):
        sql = """
                select ref
                from type_ejector
                order by ref asc
        """
        return self.dql_template(sql)

    def model_get_camera(self):
        sql = """
                select ref
                from type_camera
                order by ref asc
        """
        return self.dql_template(sql)

    def model_get_teams(self):
        sql = """
                select ref
                from test_team
                order by ref asc
        """
        return self.dql_template(sql)

    def model_get_points(self):
        pass
        sql = """
                select ref
                from type_test_point
                order by ref asc
        """
        return self.dql_template(sql)

    def model_get_intrinsic(self):
        pass
        sql = """
                select ref
                from type_intrinsic_value
                order by ref asc
        """
        return self.dql_template(sql)

    def model_get_rights(self):
        pass
        sql = """
                select ref
                from type_role
                where id <> 1
                order by id asc
        """
        return self.dql_template(sql)

    def model_get_means_name_by_means_type(self, means_type):
        sql = """
            select distinct name
            from test_mean
            where type = '{0}'
            order by
            name asc
        """.format(means_type)
        return self.dql_template(sql)

    def model_get_means_number_by_means_name(self, means_type, means_name):
        sql = """
            select distinct number
            from test_mean
            where type = '{0}' and name = '{1}'
            order by
            number asc
        """.format(means_type, means_name)
        return self.dql_template(sql)


if __name__ == '__main__':
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()
