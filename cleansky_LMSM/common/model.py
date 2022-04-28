"""
https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/
https://www.postgresqltutorial.com/postgresql-python/transaction/
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
        # self.__transaction_flag = 0

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

        self.type_strategy = {
            None: None,
            'coating': 'type_coating',
            'detergent': 'type_detergent'
        }

    # def is_in_transaction(self):
    #     if self.__transaction_flag == 1:
    #         return True
    #     else:
    #         return False

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

    # tcl interface
    def model_start_transaction(self):
        self.get_db().get_connect().commit()

    def model_roll_back(self):
        self.get_db().get_connect().rollback()
        print("\nROLLBACK\n")
        print("\nSTART TRANSACTION\n")

    def model_commit(self):
        self.get_db().get_connect().commit()
        print("\nCOMMIT\n")

    # sql template pattern
    def tcl_template(self, dcl, error_info='dcl error'):
        try:
            cursor = self.get_db().get_connect().cursor()
            cursor.execute(dcl)
            # self.get_db().get_connect().commit()
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
            # logging.info('dql success')
        except Exception:
            # logging.error(error_info)
            print(error_info+dql)
        return result

    def dml_template(self, dml, error_info='dml error'):
        try:
            print(dml)
            cursor = self.get_db().get_connect().cursor()
            cursor.execute(dml)
            # self.get_db().get_connect().commit()
            cursor.close()
        except Exception:
            print(error_info)
            print(dml)

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

    def model_get_role_id(self, role_ref):
        sql = """
                select id from type_role where ref='{0}'
        """.format(role_ref)
        return self.dql_template(sql)

    def model_get_mean(self, mean_id):
        sql = """
                select concat(t1.type, '_',t1.name, '_',t1.number)
                from test_mean as t1
                where t1.id = {0}
        """.format(mean_id)
        return self.dql_template(sql)

    def model_get_simple_ele(self, table_name, ele_id):
        """
        用id查找ref
        """
        sql = """
                select t1.ref
                from {0} t1
                where t1.id = {1}
        """.format(table_name, ele_id)
        return self.dql_template(sql)

    def model_get_simple_id(self, table_name, ele_ref):
        """查找简单元素的id"""
        sql = """
            select id from {0} t1 where t1.ref = '{1}'
        """.format(table_name, ele_ref)
        return self.dql_template(sql)

    def tools_get_elements_info(self, lis):
        """
        用于配合元素字典使用
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
            select uname from account where id = {0}
        """.format(uid)
        return self.dql_template(sql)

    def model_get_ele_id_by_ref(self, table_number, ref_tup):
        """
        很显然的吗，要么是testMean表，要么是其他表，testmean表有三个字段记录信息，所以特别照顾
        """
        if table_number == 0:
            sql = """
                select id from test_mean where type = '{0}' and name = '{1}' and number = '{2}'
            """.format(ref_tup[0], ref_tup[1], ref_tup[2])
            return self.dql_template(sql)
        elif table_number != 10 and table_number != 11:
            # 该死的逻辑符号。。。
            sql = """
                select id from {0} where ref = '{1}'
            """.format(self.field_name[table_number], ref_tup[0])
            return self.dql_template(sql)
        else:
            # 这里必须返回布尔类型的数据。。。因为返回的elementid会用来拼装为person字典的键，在字典中布尔类型的数据就是按照布尔类型进行存储的
            if ref_tup[0] == 'YES':
                return [(True,)]
            elif ref_tup[0] == 'NO':
                return [(False,)]
            else:
                return [ref_tup]

    def model_get_element_type(self, table_name):
        """
        策略模式，输入的strategy为想要获取的对象的名称
        """
        sql = """
                select ref from {0} order by ref asc
        """.format(table_name)
        return self.dql_template(sql)

    @staticmethod
    def tools_insert(**kwargs):
        """string_type参数将以集合，列表的形式传入需要添加引号的元素"""
        column_str, value_str = '', ''
        for key, value in kwargs.items():
            if key != 'str_type':
                column_str += key + ', '
                if key in kwargs['str_type']:
                    value_str += "'" + value + "', "
                else:
                    value_str += str(value) + ', '

        column_str, value_str = column_str[:-2], value_str[:-2]
        return column_str, value_str

    @staticmethod
    def tools_update(**kwargs):
        """string_type将参数以集合，列表的形式传入需要添加引号的元素"""
        update_string = ''
        for key, value in kwargs.items():
            if key != 'str_type':
                if key in kwargs['str_type']:
                    update_string += key + "='" + value + "', "
                else:
                    update_string += key + "=" + str(value) + ", "
        return update_string[:-2]

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

    def model_get_means(self):
        sql = """
                select distinct type
                from test_mean
                order by type asc
        """
        return self.dql_template(sql)


class InsectModel(Model):
    def model_get_insect(self):
        sql = """
            select
            name, masse, alt_min, alt_max, length, width, thickness, hemolymphe
            from insect
            order by name asc
        """
        return self.dql_template(sql)

    def model_get_insect_names(self):
        sql = """
            select distinct name from insect order by name asc
        """
        return self.dql_template(sql)

    def model_get_hemo(self):
        sql = """
            select distinct hemolymphe from insect order by hemolymphe asc
        """
        return self.dql_template(sql)

    def model_update_insect(self, **kwargs):
        update_string = Model.tools_update(**kwargs)
        sql = """
            update insect set {0} where name='{1}'
        """.format(update_string, kwargs['name'])
        self.dml_template(sql)

    def model_insert_insect(self, **kwargs):
        column_str, value_str = Model.tools_insert(**kwargs)
        sql = """
            insert into insect({0}) values({1})
        """.format(column_str, value_str)
        self.dml_template(sql)

    def model_is_exist_insect(self, name):
        sql = """
            select * from insect where name='{0}'
        """.format(name)
        return self.dql_template(sql)


class AttributeModel(Model):
    """负责管理attribute，attribute_coating，attribute_detergent和attribute_test_mean这几张表的增删改查"""
    def get_element_id(self, element_name, number, strategy=True):
        """从coating，detergent和test_mean表格中用元素的信息查找元素的id"""
        if strategy == 1:
            sql = """
                select c.id
                from coating as c
                join type_coating tc on tc.id = c.id_type_coating
                where tc.ref='{0}' and c.number='{1}'
            """.format(element_name, number)
            return self.dql_template(sql)
        elif strategy == 2:
            sql = """
                select d.id
                from detergent as d
                join type_detergent td on td.id = d.id_type_detergent
                where td.ref='{0}' and d.number='{1}'
            """.format(element_name, number)
            return self.dql_template(sql)
        elif strategy == 3:
            sql = """
                select id
                from test_mean as tm
                where type = '{0}' and name = '{1}' and number = '{2}'
            """.format(element_name, number[0], number[1])
            return self.dql_template(sql)

    def get_attribute_id(self, attribute_name, value, unity):
        """根据attribute的信息查找attribute的id"""
        sql = """
            select a.id
            from attribute as a 
            join type_unity tu on a.id_unity = tu.id
            where a.attribute='{0}' and a.value={1} and tu.ref='{2}'
        """.format(attribute_name, value, unity)
        return self.dql_template(sql)

    def delete_element_attr(self, element_type_name, number, attribute_name, value, unity, strategy=1):
        """将attribute和元素解绑！用的是字符串"""
        element_id = self.get_element_id(element_type_name, number, strategy)[0][0]
        aid = self.get_attribute_id(attribute_name, value, unity)[0][0]
        if strategy == 1:
            sql = """
                delete from attribute_coating where id_attribute={0} and id_coating={1}
            """.format(aid, element_id)
            self.dml_template(sql)
        elif strategy == 2:
            sql = """
                delete from attribute_detergent where id_attribute={0} and id_detergent={1}
            """.format(aid, element_id)
            self.dml_template(sql)
        elif strategy == 3:
            sql = """
                delete from attribute_test_mean where id_attribute={0} and id_test_mean={1}
            """.format(aid, element_id)
            self.dml_template(sql)

    def model_get_element_attributes(self, type_element, number, strategy=True):
        """三张表，如果是attribute_test_mean，传入的number函数参数为元组，分别代表means name和serial number"""
        if strategy == 1:
            sql = """
            select a.attribute, a.value, tu.ref
            from attribute_coating as ac
            join attribute a on a.id = ac.id_attribute
            join coating c on c.id = ac.id_coating
            join type_coating tc on c.id_type_coating = tc.id
            join type_unity tu on a.id_unity = tu.id
            where tc.ref = '{0}' and  c.number = '{1}'
            order by a.attribute asc
            """.format(type_element, number)
            return self.dql_template(sql)
        elif strategy == 0:
            sql = """
            select a.attribute, a.value, tu.ref
            from attribute_detergent as ad
            join attribute a on ad.id_attribute = a.id
            join detergent d on ad.id_detergent = d.id
            join type_detergent td on d.id_type_detergent = td.id
            join type_unity tu on a.id_unity = tu.id
            where td.ref='{0}' and d.number='{1}'
            order by a.attribute asc
            """.format(type_element, number)
            return self.dql_template(sql)
        elif strategy == 2:
            # 做一个小小的适配器number将携带
            means_type, means_name, serial_number = type_element, number[0], number[1]
            sql = """
            select a.attribute, a.value, tu.ref
            from attribute_test_mean atm
            join attribute a on a.id = atm.id_attribute
            join type_unity tu on a.id_unity = tu.id
            join test_mean tm on tm.id = atm.id_test_mean
            where tm.type = '{0}' and tm.name = '{1}' and tm.number = '{2}'
            order by a. attribute asc
            """.format(means_type, means_name, serial_number)
            print(sql)
            return self.dql_template(sql)

    def model_is_exist_attr(self, attribute_name, unity_id, value):
        sql = """
            select id from attribute a
            where a.attribute='{0}' and a.id_unity={1} and a.value={2}
        """.format(attribute_name, unity_id, value)
        return self.dql_template(sql)

    def model_create_new_attr(self, attribute_name, unity, value):
        sql = """
            insert into attribute(attribute, id_unity, value)
            values('{0}', {1}, {2})
        """.format(attribute_name, unity, value)
        self.dml_template(sql)
        return self.model_is_exist_attr(attribute_name, unity, value)

    def model_get_element_char(self, type_element, strategy=True):
        """填list of characteristic，获取该element_type的所有chara"""
        if strategy == 1:
            sql = """
            select distinct a.attribute
            from attribute_coating as ac
            join attribute a on a.id = ac.id_attribute
            join coating c on c.id = ac.id_coating
            join type_coating tc on c.id_type_coating = tc.id
            where tc.ref = '{0}'
            order by a.attribute asc
            """.format(type_element)
            return self.dql_template(sql)
        elif strategy == 0:
            sql = """
            select distinct a.attribute
            from attribute_detergent as ad
            join attribute a on a.id = ad.id_attribute
            join detergent d on ad.id_detergent = d.id 
            join type_detergent td on d.id_type_detergent = td.id
            where td.ref = '{0}'
            order by a.attribute asc
            """.format(type_element)
            return self.dql_template(sql)
        elif strategy == 2:
            sql = """
            select
            distinct a.attribute
            from attribute_test_mean as atm
            join test_mean tm on tm.id = atm.id_test_mean
            join attribute a on atm.id_attribute = a.id
            where tm.type = '{0}' and tm.name = '{1}' and tm.number = '{2}'
            order by a.attribute
            """.format(type_element[0], type_element[1], type_element[2])
            return self.dql_template(sql)


class UnityModel(Model):
    def model_is_unity_exist(self, unity):
        sql = """
            select id from type_unity where ref='{0}'
        """.format(unity)
        return self.dql_template(sql)

    def model_create_new_unity(self, unity):
        """顺带会返回新创建的unity的id"""
        sql = """
            insert into type_unity(ref) values('{0}')
        """.format(unity)
        self.dml_template(sql)
        return self.model_is_unity_exist(unity)

    def model_get_unity(self):
        sql = """
            select ref from type_unity order by ref asc
        """
        return self.dql_template(sql)


class ParamModel(Model):
    def get_all_params(self):
        """追加和unity的表连接"""
        sql = """
            select
            tp.name, tu.ref, tp.axes
            from type_param as tp
            join type_unity tu on tp.id_unity = tu.id
            order by tp.name asc
        """
        return self.dql_template(sql)

    def get_params_by_element(self, ele_tup, strategy):
        """type_param_test_mean join type_id_test_mean"""
        if strategy == 2:
            sql = """
            select
            tp.name, tu.ref, tptm.validate
            from type_param_test_mean as tptm
            join type_param tp on tptm.id_type_param = tp.id
            join test_mean tm on tptm.id_test_mean = tm.id
            join type_unity tu on tp.id_unity = tu.id
            where tm.type='{0}' and tm.name='{1}' and tm.number='{2}'
            """.format(ele_tup[0], ele_tup[1], ele_tup[2])
            return self.dql_template(sql)


class LoginModel(Model):
    def model_login(self, username, password):
        """
        Obtain user information
        if our username not exists in table account or the password is wrong, return []
        """
        sql = """
                select * from account
                where uname = '{0}' and password = '{1}'
        """.format(username, password)
        return self.dql_template(dql=sql)


class MenuModel(Model):
    pass


class ManagementModel(Model):
    def model_get_uid_by_uname(self, uname):
        """
        可以通过用户名来查找用的id
        也可以用来判断用户是否存在于系统中
        """
        sql = """
            select id from account where uname='{0}'
        """.format(uname)
        return self.dql_template(sql)

    def model_get_orga(self):
        """Returns a de-redo record of the orga field in the Account table directly as a Python list data structure"""
        sql = """
                select distinct a.orga
                from account as a
                order by a.orga asc
        """
        return self.dql_template(dql=sql, error_info="model get_orga error")

    def model_get_list_of_users(self):
        """The query displays the List of users table"""
        sql = """
                select
                a.orga, a.uname, a.email, a.fname, a.lname, a.tel
                from account as a
                order by a.orga asc, a.uname asc
        """
        return self.dql_template(dql=sql)

    def model_get_username_and_lastname(self, organisation):
        """by page 3 <les listes dependants>"""
        sql = """
                select uname,lname from account where orga='{0}'
        """.format(organisation)
        return self.dql_template(dql=sql)

    def model_get_list_of_users_by_organisation(self, organisation):
        sql = """
                select uname
                from account
                where orga = '{0}'
        """.format(organisation)
        return self.dql_template(sql)

    # def model_get_first_name_and_lastname(self, username):
    #     """by page 3 <les listes dependants>"""
    #     sql = """
    #             select fname,lname
    #             from account
    #             where uname = '{0}'
    #     """.format(username)
    #     return self.dql_template(dql=sql)

    def model_get_lname(self, username):
        sql = """
                select lname
                from account
                where uname = '{0}'
        """.format(username)
        return self.dql_template(sql)

    def model_get_fname(self, username):
        sql = """
                select fname
                from account
                where uname = '{0}'
        """.format(username)
        return self.dql_template(sql)

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

    def model_get_insect(self):
        pass


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

    def model_create_new_element(self, element_type, ref_tup):
        table_name = self.field_name[element_type]
        insert_str = None
        column_name = None
        # 为什么？作用域研究
        if element_type == 0:
            insert_str = "'" + ref_tup[0] + "', '" + ref_tup[1] + "', '" + ref_tup[2] + "'"
            column_name = "type, name, number"
        else:
            insert_str = "'" + ref_tup[0] + "'"
            column_name = "ref"
        sql = """
            insert into {0}({2})
            values ({1})
        """.format(table_name, insert_str, column_name)
        print(sql)
        self.dml_template(dml=sql)

    def model_delete_user_right(self, uid, element_type, element_id):
        column_name = ""
        if element_type != 10 and element_type != 11:
            column_name = 'id_' + self.field_name[element_type]
        else:
            column_name = self.field_name[element_type]
        sql = """
            delete from user_right
            where id_account={0} and {1}={2}
        """.format(uid, column_name, element_id)
        print(sql)
        self.dml_template(dml=sql)

    def model_update_user_right(self, uid, element_type, element_id, role_id):
        column_name = ""
        if element_type != 10 and element_type != 11:
            column_name = 'id_' + self.field_name[element_type]
        else:
            column_name = self.field_name[element_type]
        sql = """
            update user_right
            set role={0}
            where id_account={1} and {2}={3}
        """.format(role_id, uid, column_name, element_id)
        print(sql)
        self.dml_template(sql)

    def model_insert_user_right(self, uid, element_type, element_id, role_id):
        column_name = ""
        if element_type != 10 and element_type != 11:
            column_name = 'id_' + self.field_name[element_type]
        else:
            column_name = self.field_name[element_type]
        sql = """
                insert into user_right(id_account, role, {0})
                values({1}, {2}, {3})
        """.format(column_name, uid, role_id, element_id)
        print(sql)
        self.dml_template(sql)


class ItemsToBeTestedModel(InsectModel, UnityModel, AttributeModel):
    def model_get_coating_type(self):
        """
        获得所有的coating type
        """
        sql = """
            select ref from type_coating order by ref asc
        """
        return self.dql_template(sql)

    def model_get_coating_type_id_by_name(self, coating_type):
        """
        根据coating type string 查找type id
        """
        sql = """
            select id
            from type_coating
            where ref = '{0}'
        """.format(coating_type)
        return self.dql_template(sql)

    def model_get_number(self, element_type, strategy=True):
        """
        根据coating name查找所有的number
        """
        if strategy:
            sql = """
            select c.number
            from coating as c
            join type_coating as tc on c.id_type_coating = tc.id
            where tc.ref = '{0}'
            order by c.number asc
            """.format(element_type)
            return self.dql_template(sql)
        elif strategy is False:
            sql = """
            select d.number
            from detergent d
            join type_detergent td on d.id_type_detergent = td.id
            where td.ref='{0}'
            order by d.number asc
            """.format(element_type)
            return self.dql_template(sql)


    def model_is_validate(self, type_element, number, strategy=True):
        res = self.model_is_exist_element(type_element, number, strategy)
        if not res:
            return []
        else:
            return [(res[0][3],)]

    def model_is_exist_element(self, type_element, number, strategy=True):
        """
        效果一样的
        """
        if strategy:
            sql = """
            select * from coating as c
            join type_coating tc on c.id_type_coating = tc.id
            where tc.ref = '{0}' and c.number = '{1}'
            """.format(type_element, number)
            return self.dql_template(sql)
        elif strategy is False:
            sql = """
            select * from detergent as d
            join type_detergent td on d.id_type_detergent = td.id
            where td.ref='{0}' and d.number='{1}'
            """.format(type_element, number)
            return self.dql_template(sql)

    def model_is_connected_element_and_attribute(self, element_id, attr_id, strategy=True):
        if strategy:
            sql = """
                select id from attribute_coating ac
                where ac.id_attribute={0} and ac.id_coating={1}
            """.format(element_id, attr_id)
            return self.dql_template(sql)
        elif strategy is False:
            sql = """
                select id from attribute_detergent ad
                where ad.id_attribute={0} and ad.id_detergent={1}
            """.format(element_id, attr_id)
            return self.dql_template(sql)

    def create_connexion_between_element_and_attribute(self, element_id, attr_id, strategy=True):
        if strategy:
            sql = """
                insert into attribute_coating(id_attribute, id_coating)
                values({1}, {0})
            """.format(element_id, attr_id)
            self.dml_template(sql)
            return self.model_is_connected_element_and_attribute(element_id, attr_id, strategy)
        elif strategy is False:
            sql = """
                insert into attribute_detergent(id_attribute, id_detergent)
                values({1}, {0})
            """.format(element_id, attr_id)
            self.dml_template(sql)
            return self.model_is_connected_element_and_attribute(element_id, attr_id, strategy)

    def model_create_new_element(self, element_id, number, strategy=True):
        """
        创建新的（coating，number）
        """
        if strategy:
            sql = """
                insert into coating(id_type_coating, number, validate)
                values ({0}, '{1}', False)
            """.format(element_id, number)
            self.dml_template(sql)
        elif strategy is False:
            sql = """
                insert into detergent(id_type_detergent, number, validate)
                values ({0}, '{1}', False)
            """.format(element_id, number)
            self.dml_template(sql)

    def model_validate_element_type(self, element_type_name, number, strategy=True):
        element_id = self.get_element_id(element_type_name, number, strategy)[0][0]
        if strategy:
            sql = """
                update coating set validate=true where id={0}
            """.format(element_id)
            self.dml_template(sql)
        elif strategy is False:
            sql = """
                update detergent set validate=true where id={0}
            """.format(element_id)
            self.dml_template(sql)


class TankModel(Model):
    def tank_type(self):
        sql = """select ref from type_tank order by ref asc"""
        return self.dql_template(sql)

    def tank_id(self, tank_type_name):
        sql = """select id from type_tank where ref = '{0}'""".format(tank_type_name)
        return self.dql_template(sql)

    def tank_number(self, type_id):
        sql = """select number, validate
                from tank where id_type_tank == {0}
                order by number asc 
        """.format(type_id)
        return self.dql_template(sql)


class SensorModel(Model):
    pass


class ListOfTestMeansModel(AttributeModel, ParamModel, UnityModel, TankModel):
    pass


if __name__ == '__main__':
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()
    model = ItemsToBeTestedModel(db_object=unittest_db)
    print(model.model_is_exist_insect('Fly'))
