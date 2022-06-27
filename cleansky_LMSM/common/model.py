"""
https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/
https://www.postgresqltutorial.com/postgresql-python/transaction/
"""
from enum import Enum
import random

import cleansky_LMSM.common.database as database
import cleansky_LMSM.config.sensor_config as csc


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

        # 用于标注事务处理模式的参数
        self.__transaction_mode = transaction_mode

        # database对象
        self.__db = db_object

        # control层对象
        self.__controller = None

        # user_right表的字段字典
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
        """在controller被创建的时候，绑定model和controller"""
        self.__controller = controller_obj

    def get_db(self):
        """获取该model绑定的database对象"""
        return self.__db

    @staticmethod
    def tools_get_field_str_insert(locals_dict, type_list=type_list_def):
        """历史遗留问题"""
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
        """历史遗留问题"""
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

    def model_roll_back(self):
        """model层的回滚接口，被control层调用"""
        self.get_db().get_connect().rollback()
        print("\nROLLBACK\n")
        print("\nSTART TRANSACTION\n")

    def model_commit(self):
        """model层的事务提交接口，在CRUD的时候调用该函数以实时上传数据库"""
        self.get_db().get_connect().commit()
        print("\nCOMMIT\n")

    def tcl_template(self, dcl, error_info='dcl error'):
        """tcl模板"""
        try:
            cursor = self.get_db().get_connect().cursor()
            cursor.execute(dcl)
            # self.get_db().get_connect().commit()
            cursor.close()
            # raise TclError(sql=dcl)
        except:
            print("###TCL Error###")
            print("sql:")
            print(dcl)

    def dql_template(self, dql, error_info='dql error'):
        """dql模板方法；如果没查到数据，返回空表[]；如果查到数据，以元组列表的形式返回数据：[(1, 2, 3), (4, 5, 6)]"""
        result = []
        try:
            cursor = self.get_db().get_connect().cursor()
            cursor.execute(dql)
            result = cursor.fetchall()
            cursor.close()
            # logging.info('dql success')
        except:
            print("###DQL Error###")
            print("sql:")
            print(dql)
        return result

    def dml_template(self, dml, error_info='###DML Error###'):
        try:
            cursor = self.get_db().get_connect().cursor()
            cursor.execute(dml)
            cursor.close()
        except:
            print(error_info)
            print(dml)

    def model_get_role_ref(self, role_id):
        """通过id获取特定权限的ref"""
        sql = """select ref from type_role where id = {0}""".format(role_id)
        return self.dql_template(sql)

    def model_get_role_id(self, role_ref):
        """通过ref获取特定权限的ref"""
        sql = """select id from type_role where ref='{0}'""".format(role_ref)
        return self.dql_template(sql)

    def model_get_simple_ele(self, table_name: str, ele_id: int):
        """给出table name,用id查找ref"""
        sql = """
            select t1.ref
            from {0} t1
            where t1.id = {1}
        """.format(table_name, ele_id)
        return self.dql_template(sql)

    def model_get_simple_id(self, table_name, ele_ref):
        """通过ref查找简单元素的id"""
        sql = """
            select id from {0} t1 where t1.ref = '{1}'
        """.format(table_name, ele_ref)
        return self.dql_template(sql)

    def model_get_mean(self, mean_id):
        """用字符串拼接的工具方法，表示means，用于management页面的信息展示"""
        sql = """
            select concat(t1.type, '_',t1.name, '_',t1.number)
            from test_mean as t1
            where t1.id = {0}
        """.format(mean_id)
        return self.dql_template(sql)

    def tools_get_elements_info(self, lis):
        """
        配合元素字典使，用于将代号转化为字符串，便于图数据结构提取信息
        两种输入模式，四元素或三元素，格式如下
        input [user_id, role_id, ele_type(-2), ele_id]  (number)
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
        info.append(self.model_get_role_ref(lis[-3])[0][0])
        return info

    def model_get_username_by_uid(self, uid):
        sql = """
            select uname from account where id = {0}
        """.format(uid)
        return self.dql_template(sql)

    def get_ele_id_by_ref(self, table_number, ref_tup):
        """
        通过元素的ref，以及表的代号，查找元素id并返回
        三种情况：
        1.test_mean表，则传入元素为三元组，分别记录三个参数的信息
        2.布尔类型，对应insect和acqui
        3.其他表，这是最简单最正常的情况
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
            # 这里必须返回布尔类型的数据。。。因为返回的element id会用来拼装为person字典的键，在字典中布尔类型的数据就是按照布尔类型进行存储的
            if ref_tup[0] == 'YES':
                return [(True,)]
            elif ref_tup[0] == 'NO':
                return [(False,)]
            else:
                return [ref_tup]

    def model_get_element_ref(self, table_name):
        """任何有ref字段的表都可以使用这个接口获取ref信息"""
        sql = """select ref from {0} order by ref asc""".format(table_name)
        return self.dql_template(sql)

    @staticmethod
    def tools_insert(**kwargs):
        """
        **kwargs多参数传参实现灵活生成适配sql语法的insert字符串
        在kwargs中配置string_type参数以在生成的字符串中添加引号
        输入参数表遵循：参数名=参数值
        返回结果为两个字符串组成的元组，第一个元素为字段名字符串，第二个元素为字段值字符串

        举例：
        输入：a=2,b=3,c='abc',str_type=['c']
        输出：('a, b, c', "1, 2, '123'")

        输入：a=2,b=3,c='abc'
        输出：异常（因为c为字符串，但是没有传入str_type参数）

        输入：str_type=['a']
        输出：('', '')
        """
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
        """
        string_type将参数以集合，列表的形式传入需要添加引号的元素
        """
        update_string = ''
        for key, value in kwargs.items():
            if key != 'str_type':
                if key in kwargs['str_type']:
                    update_string += key + "='" + value + "', "
                else:
                    update_string += key + "=" + str(value) + ", "
        return update_string[:-2]

    @staticmethod
    def tools_update_with_none(**kwargs):
        """
        string_type将参数以集合，列表的形式传入需要添加引号的元素
        """
        update_string = ''
        for key, value in kwargs.items():
            if key != 'str_type':
                if value is None or value == "":
                    update_string += key + " = NULL, "
                else:
                    if key in kwargs['str_type']:
                        update_string += key + "='" + value + "', "
                    else:
                        update_string += key + "=" + str(value) + ", "
        return update_string[:-2]

    @staticmethod
    def tools_array_to_string(lis: list, str_type: list) -> str:
        """
        lis传递待插入数据数组
        str_type传递01编码的等长串，0代表不需要添加双引号，1代表为字符型数据，需要添加双引号
        用于配置PostgreSQL中用于insert语句的字符串，便于转换数组
        lis 参数的参数类型为字符或整型均可

        3表示如果为空字符串，则插入null，如果非空，转换成int，针对有三维坐标的单位专门设计
        """
        index, array_string = 0, ''
        while index < len(lis):
            if str_type[index] == 3:
                if lis[index] == '':
                    array_string += "NULL, "
                else:
                    array_string += str(lis[index]) + ", "
            elif str_type[index] == 1:
                array_string += "'" + str(lis[index]) + "', "
            else:
                array_string += str(lis[index]) + ', '
            index = index + 1
        array_string = array_string[:-2]
        array_string = "{" + array_string + "}"
        return array_string

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


class RightsModel(Model):
    def model_get_rights_for_graph(self):
        """查找user_right表，用于初始化权限图"""
        sql = """select * from user_right"""
        return self.dql_template(sql)


class ElementModel(Model):
    def model_get_coating_type(self):
        """获得所有的coating type"""
        sql = """
            select ref from type_coating order by ref asc
        """
        return self.dql_template(sql)

    def model_get_all_coating_number(self):
        sql = """
        select distinct number
        from coating
        order by number
        """
        return self.dql_template(sql)

    def model_get_coating_tree(self):
        sql = """
        select tc.ref, c.number
        from coating as c 
        join type_coating tc on c.id_type_coating = tc.id
        order by tc.ref, c.number
        """
        return self.dql_template(sql)

    def test_means_str_by_uid(self, uid):
        """用uid获取他所拥有权限的test_means的字符串信息"""
        sql = """
            select tm.type, tm.name, tm.number
            from user_right as ur
            join test_mean tm on ur.id_test_mean = tm.id
            where id_account = {0}
        """.format(uid)
        return self.dql_template(sql)

    def all_test_means(self):
        """获取全部test_means，给manager用的"""
        sql = """
            select tm.type, tm.name, tm.number
            from test_mean tm
            order by tm.type asc, tm.name asc, tm.number asc
        """
        return self.dql_template(sql)

    def is_validate(self, type_element: str, number, strategy=1) -> list:
        """将该元素的validate项返回"""
        res = self.is_exist_element(type_element, number, strategy)
        if not res:
            return []
        else:
            if strategy != 2:
                return [(res[0][3],)]
            if strategy == 2:
                return [(res[0][4],)]

    def is_exist_element(self, type_element, number, strategy=1):
        """返回coating，detergent，test_mean的*"""
        if strategy == 1:
            sql = """
            select * from coating as c
            join type_coating tc on c.id_type_coating = tc.id
            where tc.ref = '{0}' and c.number = '{1}'
            """.format(type_element, number)
            return self.dql_template(sql)
        elif strategy == 0:
            sql = """
            select * from detergent as d
            join type_detergent td on d.id_type_detergent = td.id
            where td.ref='{0}' and d.number='{1}'
            """.format(type_element, number)
            return self.dql_template(sql)
        elif strategy == 2:
            sql = """
            select * from test_mean where type='{0}' and name='{1}' and number='{2}'
            """.format(type_element, number[0], number[1])
            return self.dql_template(sql)


class EjectorModel(Model):
    def type_ejector(self):
        """获取ejector的类型"""
        sql = """select ref from type_ejector order by ref asc"""
        return self.dql_template(sql)

    def ejector_table(self):
        """填充ejector表格"""
        sql = """
            select te.ref, e.number, e.v_min, e.v_max, e.e_axe, e.ins_vol, e.nb_type
            from ejector as e 
            join type_ejector te on te.id = e.id_type_ejector
            order by te.ref asc
        """
        return self.dql_template(sql)

    def ejector_number(self, ref):
        """根据ejector的类型获取其编号"""
        sql = """
            select distinct e.number
            from ejector as e 
            join type_ejector te on te.id = e.id_type_ejector
            where te.ref='{0}'
            order by e.number asc
        """.format(ref)
        return self.dql_template(sql)

    def update_ejector(self, **kwargs):
        """调用tools_update方法动态传参，必须传入id_type_ejector参数以注明update哪一行记录"""
        update_string = Model.tools_update(**kwargs)
        sql = """
            update ejector set {0} where id_type_ejector={1}
        """.format(update_string, kwargs['id_type_ejector'])
        self.dml_template(sql)

    def insert_ejector(self, **kwargs):
        """新建ejector，调用tools_insert方法动态传参"""
        column_str, value_str = Model.tools_insert(**kwargs)
        sql = """
            insert into ejector({0}) values({1})
        """.format(column_str, value_str)
        self.dml_template(sql)

    def is_exist_ejector(self, ref, num):
        """判断ejector是否存在，如果存在，返回ejector的id"""
        sql = """
            select e.id
            from ejector as e 
            join type_ejector te on te.id = e.id_type_ejector
            where te.ref='{0}' and e.number='{1}'
        """.format(ref, num)
        return self.dql_template(sql)


class CameraModel(Model):
    def type_camera(self):
        sql = """
            select ref from type_camera order by ref asc
        """
        return self.dql_template(sql)

    def camera_table(self):
        sql = """
        select tc.ref, c.number, c.s_min, c.s_max, c.axe, c.h_aperture, c.w_aperture
            from camera as c 
        join type_camera tc on c.id_type_camera = tc.id
        order by tc.ref asc , c.number asc
        """
        return self.dql_template(sql)

    def camera_number(self, ref):
        sql = """
        select c.number
            from camera as c
        join type_camera tc on c.id_type_camera = tc.id
        where tc.ref='{0}'
        """.format(ref)
        return self.dql_template(sql)

    def create_camera(self, **kwargs):
        pass

    def is_exist_camera(self, ref, num):
        sql = """
        select c.id
        from camera as c 
        join type_camera tc on tc.id = c.id_type_camera
        where tc.ref='{0}' and c.number='{1}'
        """.format(ref, num)
        return self.dql_template(sql)

    def insert_camera(self, **kwargs):
        pass

    def update_camera(self, **kwargs):
        pass

    def model_camera_config(self):
        sql = """
        select distinct cc.ref
        from config_camera as cc
        where cc.validate is true
        order by cc.ref
        """
        return self.dql_template(sql)

    def model_is_camera_config_exist(self, ref):
        sql = """
        select id
        from config_camera
        where ref='{0}'
        """.format(ref)
        return self.dql_template(sql)


class InsectModel(Model):
    def model_get_insect(self):
        """填充insect表格，获取insect的全部信息"""
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
        sql = """select ref from type_unity order by ref asc"""
        return self.dql_template(sql)

    def check_unity(self, ref):
        """如果unity存在，返回unity的id，如果unity不存在，创建unity，随后返回unity的id"""
        ret = self.model_is_unity_exist(ref)
        if not ret:
            return self.model_create_new_unity(ref)[0][0]
        else:
            return self.model_is_unity_exist(ref)[0][0]


class AttributeModel(UnityModel):
    """负责管理attribute，attribute_coating，attribute_detergent和attribute_test_mean这几张表的增删改查"""

    def check_attribute(self, attribute_name, value, unity):
        """验证attribute，如果存在，返回attribute的id，如果不存在，创建该attribute，返回attribute的id"""
        unity_id = self.check_unity(unity)
        ret = self.model_is_exist_attr(attribute_name, unity_id, value)
        if not ret:
            # 不存在
            return self.model_create_new_attr(attribute_name, unity_id, value)[0][0]
        return self.model_is_exist_attr(attribute_name, unity_id, value)[0][0]

    def is_connected_element_and_attribute(self, element_id, attr_id, strategy=1):
        """用于判断链接是否存在，如果存在，返回id，如果不存在，返回[]"""
        if strategy == 1:
            sql = """
                select id from attribute_coating ac
                where ac.id_attribute={0} and ac.id_coating={1}
            """.format(attr_id, element_id)
            return self.dql_template(sql)
        elif strategy == 0:
            sql = """
                select id from attribute_detergent ad
                where ad.id_attribute={0} and ad.id_detergent={1}
            """.format(attr_id, element_id)
            return self.dql_template(sql)
        elif strategy == 2:
            sql = """
                select id from attribute_test_mean atm
                where id_attribute={0} and id_test_mean={1}
            """.format(attr_id, element_id)
            return self.dql_template(sql)

    def create_connexion(self, element_id, attr_id, strategy):
        """创建attribute和ele的链接"""
        if strategy == 1:
            sql = """
                insert into attribute_coating(id_attribute, id_coating)
                values({1}, {0})
            """.format(element_id, attr_id)
            self.dml_template(sql)
            return self.is_connected_element_and_attribute(element_id, attr_id, strategy)
        elif strategy == 0:
            sql = """
                insert into attribute_detergent(id_attribute, id_detergent)
                values({1}, {0})
            """.format(element_id, attr_id)
            self.dml_template(sql)
            return self.is_connected_element_and_attribute(element_id, attr_id, strategy)
        elif strategy == 2:
            sql = """
                insert into attribute_test_mean(id_attribute, id_test_mean)
                values({1}, {0})
            """.format(element_id, attr_id)
            self.dml_template(sql)

    def validate_element(self, element_type_name, number, strategy):
        element_id = self.get_element_id(element_type_name, number, strategy)[0][0]
        if strategy == 1:
            sql = """
                update coating set validate=true where id={0}
            """.format(element_id)
            self.dml_template(sql)
        elif strategy == 0:
            sql = """
                update detergent set validate=true where id={0}
            """.format(element_id)
            self.dml_template(sql)
        elif strategy == 2:
            sql = """
                update test_mean set validate=true where id={0}
            """.format(element_id)
            self.dml_template(sql)

    def get_element_id(self, element_name, number, strategy):
        """从coating，detergent和test_mean表格中用元素的信息查找元素的id"""
        if strategy == 1:
            sql = """
                select c.id
                from coating as c
                join type_coating tc on tc.id = c.id_type_coating
                where tc.ref='{0}' and c.number='{1}'
            """.format(element_name, number)
            return self.dql_template(sql)
        elif strategy == 0:
            sql = """
                select d.id
                from detergent as d
                join type_detergent td on td.id = d.id_type_detergent
                where td.ref='{0}' and d.number='{1}'
            """.format(element_name, number)
            return self.dql_template(sql)
        elif strategy == 2:
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

    def delete_element_attr(self, element_type_name, number, attribute_name, value, unity, strategy):
        """将attribute和元素解绑！用的是字符串"""
        element_id = self.get_element_id(element_type_name, number, strategy)[0][0]
        aid = self.get_attribute_id(attribute_name, value, unity)[0][0]
        if strategy == 1:
            sql = """
                delete from attribute_coating where id_attribute={0} and id_coating={1}
            """.format(aid, element_id)
            self.dml_template(sql)
        elif strategy == 0:
            sql = """
                delete from attribute_detergent where id_attribute={0} and id_detergent={1}
            """.format(aid, element_id)
            self.dml_template(sql)
        elif strategy == 2:
            sql = """
                delete from attribute_test_mean where id_attribute={0} and id_test_mean={1}
            """.format(aid, element_id)
            self.dml_template(sql)

    def model_get_element_attributes(self, type_element, number, strategy=1):
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
            return self.dql_template(sql)

    def model_is_exist_attr(self, attribute_name, unity_id, value):
        """检查attribute是否存在，返回attribute的id"""
        sql = """
            select id from attribute a
            where a.attribute='{0}' and a.id_unity={1} and a.value={2}
        """.format(attribute_name, unity_id, value)
        return self.dql_template(sql)

    def model_create_new_attr(self, attribute_name, unity_id, value):
        """unity_id类型为自然数，函数返回新创建的attribute的id"""
        sql = """
            insert into attribute(attribute, id_unity, value)
            values('{0}', {1}, {2})
        """.format(attribute_name, unity_id, value)
        self.dml_template(sql)
        return self.model_is_exist_attr(attribute_name, unity_id, value)

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


class ParamModel(UnityModel):
    def get_all_params(self) -> list:
        """param查询，table type_param和table type_unity相连接，返回param name， param type unity， param axes
        """
        sql = """
            select
            tp.name, tu.ref, tp.axes
            from type_param as tp
            join type_unity tu on tp.id_unity = tu.id
            order by tp.name
        """
        return self.dql_template(sql)

    def get_params_by_element(self, ele_tup, strategy):
        """type_param_test_mean join type_id_test_mean"""
        if strategy == 2:
            sql = """
            select
            tp.name, tu.ref
            from type_param_test_mean as tptm
            join type_param tp on tptm.id_type_param = tp.id
            join test_mean tm on tptm.id_test_mean = tm.id
            join type_unity tu on tp.id_unity = tu.id
            where tm.type='{0}' and tm.name='{1}' and tm.number='{2}'
            """.format(ele_tup[0], ele_tup[1], ele_tup[2])
            return self.dql_template(sql)

    def create_new_param(self, param: tuple):
        """
        insert param methode
        传入参数param为三元组，param[0]: 对应param_name string类型，param[1]: 对应unity_string string类型， param[2]: axes为任意
        长整型数组，会被自动转化成postgresql的格式，本方法会调用tools_array_to_string工具函数，实现axes任意长数组的格式化，本方法没有返回

        关于重复插入已有param&unity
        在创建新param之前会先使用model_is_unity_exist检查unity是否存在，如果不存在unity会创建该unity
        在创建param的时候同理，调用的是is_exist_param函数
        """
        unity_id = self.model_is_unity_exist(param[1])
        if not unity_id:
            unity_id = self.model_create_new_unity(param[1])
        unity_id = unity_id[0][0]
        if len(param) == 3:
            # 传入的数据包括axes项
            array_list = self.tools_array_to_string(param[2], str_type=[3, 3, 3])
            # 检查param是否已经存在
            ret = self.is_exist_param(param=param)
            if not ret:
                sql = """
                insert into type_param(name, id_unity, axes)
                values('{0}', {1}, '{2}')
                """.format(param[0], unity_id, array_list)
                self.dml_template(sql)
        else:
            ret = self.is_exist_param(param=param)
            if not ret:
                sql = """
                insert into type_param(name, id_unity)
                values('{0}', {1})
                """.format(param[0], unity_id)
                self.dml_template(sql)

    def is_exist_param_link(self, element_id: int, param_id: int, strategy: int) -> list:
        """
        查询type_param_sensor&&type_param_test_mean用于判断param和element是否绑定，strategy策略，strategy=1 针对sensor，
        strategy=2，针对test mean
        方法传入element_id 和 param_id
        方法返回link的id号，类型为元组列表
        """
        if strategy == 1:
            sql = "select id from type_param_sensor" \
                  " where id_ref_sensor={0} and id_type_param={1}".format(element_id, param_id)
            return self.dql_template(sql)
        elif strategy == 2:
            sql = "select id from type_param_test_mean" \
                  " where id_test_mean={0} and id_type_param={1}".format(element_id, param_id)
            return self.dql_template(sql)

    def create_param_link(self, element_id: int, param_id: int, strategy: int):
        if strategy == 2:
            sql = """
                insert into type_param_test_mean(id_test_mean, id_type_param) values ({0}, {1})
            """.format(element_id, param_id)
            self.dml_template(sql)
        elif strategy == 1:
            # param 和 ref相关
            sql = """
                insert into type_param_sensor(id_ref_sensor, id_type_param) values ({0}, {1})
            """.format(element_id, param_id)
            self.dml_template(sql)

    def delete_param_link(self, element_id: int, param_id: int, strategy: int):
        if strategy == 2:
            sql = """
            delete
            from type_param_test_mean where
            id_test_mean = {0} and id_type_param = {1}
            """.format(element_id, param_id)
            return self.dml_template(sql)
        elif strategy == 1:
            sql = """
            delete
            from type_param_sensor where
            id_ref_sensor = {0} and id_type_param = {1}
            """.format(element_id, param_id)
            return self.dml_template(sql)

    def delete_all_param_link(self, element_id: int, strategy: int):
        if strategy == 2:
            sql = """
            delete
            from type_param_test_mean where
            id_test_mean = {0}
            """.format(element_id)
            return self.dml_template(sql)
        elif strategy == 1:
            sql = """
            delete
            from type_param_sensor where
            id_ref_sensor = {0}
            """.format(element_id)
            return self.dml_template(sql)

    def delete_param(self, param: tuple):
        """type_param表被多张param表引用，本方法不包含对param的检查"""
        pass

    def is_exist_param(self, param: tuple) -> list:
        """
        判断param是否存在
        输入参数param为元组，二元组或三元组
        param[0] : param_ref
        param[1] : param_unity_ref
        param[2] : axes，轴参数数组，数组元素为
        param[2]是可选项，为了适配不同的情况
        """
        if len(param) == 1:
            sql = """
                select id from type_param as tp 
                where tp.name='{0}'
                """.format(param[0])
            return self.dql_template(sql)
        unity_id = self.model_is_unity_exist(param[1])
        if not unity_id:
            # 如果不存在该单位，返回空
            return []
        unity_id = unity_id[0][0]
        if len(param) == 3:
            # 传入的数据包含axes项
            array_list = self.tools_array_to_string(param[2], str_type=[3, 3, 3])
            sql = """
            select id from type_param as tp
            where name='{0}' and id_unity={1} and axes='{2}'
            """.format(param[0], unity_id, array_list)
            return self.dql_template(sql)
        elif len(param) == 2:
            # 传入的数据不包括axes项
            sql = """
            select id from type_param as tp
            where name='{0}' and id_unity={1} and axes is null 
            """.format(param[0], unity_id)
            return self.dql_template(sql)


class SensorModel(ParamModel):
    """Class for sensor GUI"""

    def sensor_type(self) -> list:
        """Query table type_sensor, query all sensor types"""
        sql = """select ref from type_sensor order by ref"""
        return self.dql_template(sql)

    def sensor_reference(self, sensor_type: str) -> list:
        """Query table ref_sensor, get sensor ref with type sensor"""
        sql = """
        select distinct rs.ref
        from ref_sensor as rs 
        join type_sensor ts on rs.id_type_sensor = ts.id
        where ts.ref='{0}'
        order by rs.ref
        """.format(sensor_type)
        return self.dql_template(sql)

    def model_get_sensor_ref_serial_tree(self):
        sql = """
        select distinct rs.ref, s.number
        from sensor as s 
        join ref_sensor rs on s.id_ref_sensor = rs.id
        order by rs.ref, s.number
        """
        return self.dql_template(sql)

    def sensor_number(self, sensor_type: str, sensor_ref: str) -> list:
        """Query sensor number by type_sensor and sensor_ref"""
        sql = """
        select s.number
        from sensor as s
        join ref_sensor rs on s.id_ref_sensor = rs.id
        join type_sensor ts on rs.id_type_sensor = ts.id
        where ts.ref='{0}' and rs.ref='{1}'
        order by s.number
        """.format(sensor_type, sensor_ref)
        return self.dql_template(sql)

    def model_sensor_tree(self):
        sql = """
        select ts.ref, rs.ref, s.number
        from sensor as s 
        join ref_sensor rs on s.id_ref_sensor = rs.id
        join type_sensor ts on rs.id_type_sensor = ts.id
        order by ts.ref, rs.ref, s.number
        """
        return self.dql_template(sql)

    def sensor_order(self, sensor_type: str, sensor_ref: str, sensor_num: str):
        """This interface is used for filling <<order>> combobox automatically when sensor number is filled, which
        will connect the table sensor_location and query the latest sensor_location record so that we can obtain the
        latest sensor status, that is, it's in order or not"""
        sql = """
        select sl."order"
        from sensor_location as sl
        where sl.type='{0}' and sl.ref='{1}' and sl.serial_number='{2}'
        order by sl.time desc
        limit 1
        """.format(sensor_type, sensor_ref, sensor_num)
        return self.dql_template(sql)

    def sensor_table(self, sensor_type: str, sensor_ref: str) -> list:
        """This interface is used to query all the records satisfy (sensor_type, sensor_ref) and fills sensor table in
        tab sensor which will shows those order information, calibration records and location information, that is,
        whether it is located in a tank configuration."""
        sql = """
        select t1.sn, t3."order", t2.cid, t3.location
            from
        (select sl.id as slid, sl.type as tp, sl.ref as rf, sl.serial_number as sn, max(sl.time) as time
            from sensor_location as sl
        group by sl.id, sl.type, sl.ref, sl.serial_number) as t1
        join (select ts.ref as tp, rs.ref as rf, s.number as sn, case when c.id is null then false else true end as cid
                  from sensor as s
            join ref_sensor rs on s.id_ref_sensor = rs.id
                     join type_sensor ts on rs.id_type_sensor = ts.id
                     left join calibration c on s.id = c.id_sensor) as t2
        on t1.tp=t2.tp and t1.rf=t2.rf and t1.sn=t2.sn
        join sensor_location as t3
        on t1.slid=t3.id
        where t1.tp='{0}' and t1.rf='{1}'
        order by t1.sn, t3."order", t2.cid, t3.location
        """.format(sensor_type, sensor_ref)
        return self.dql_template(sql)

    def is_exist_sensor_type(self, sensor_type: str) -> list:
        sql = """select id from type_sensor where ref='{0}'""".format(sensor_type)
        return self.dql_template(sql)

    def is_exist_sensor_ref(self, sensor_tup: tuple) -> list:
        """Determine whether there is the tuple of (sensor_type, sensor_ref). return [] if it doesn't exist, return an
        empty list"""
        sql = """
        select rs.id
        from ref_sensor as rs 
        join type_sensor ts on rs.id_type_sensor = ts.id
        where ts.ref='{0}' and rs.ref='{1}'
        """.format(sensor_tup[0], sensor_tup[1])
        return self.dql_template(sql)

    def model_insert_type_sensor(self, type_sensor: str):
        sql = """
        insert into type_sensor(ref) values('{0}')
        """.format(type_sensor)
        self.dml_template(sql)

    def model_insert_ref_sensor(self, sensor_type_id: int, sensor_ref: str):
        """insert a record into the ref_sensor table, the input format is a tuple of two elements (sensor_type,
        sensor_ref), if (sensor_type, sensor_ref) has been already existed, return directly"""
        sql = """
        insert into ref_sensor(id_type_sensor, ref) VALUES ({0}, '{1}')
        """.format(sensor_type_id, sensor_ref)
        self.dml_template(sql)

    def model_insert_sensor(self, sensor_tup: tuple):
        """sensor_tup : (sensor_type, sensor_ref, sensor_number) Set the calibration and validate fields to False
        by default"""
        ret = self.is_exist_sensor_ref(sensor_tup[:2])
        if not ret:
            # create sensor ref
            sensor_type_id = self.is_exist_sensor_type(sensor_tup[0])[0][0]
            self.model_insert_ref_sensor(sensor_type_id=sensor_type_id, sensor_ref=sensor_tup[1])
        ret = self.is_exist_sensor_ref(sensor_tup[:2])
        sensor_ref_id = ret[0][0]
        sql = """
        insert into sensor(id_ref_sensor, number, validate)
        values ({0}, '{1}', False);
        """.format(sensor_ref_id, sensor_tup[2], False, False)
        self.dml_template(sql)

    def model_delete_sensor(self, sensor_type: str, sensor_ref: str, sensor_num: str):
        sensor_ref_id = self.is_exist_sensor_ref((sensor_type, sensor_ref))[0][0]
        sql = """
        delete from sensor where id_ref_sensor={0} and number='{1}'
        """.format(sensor_ref_id, sensor_num)
        self.dml_template(sql)

    def sensor_param(self, sensor_type: str) -> str:
        pass

    def sensor_unity(self, sensor_type: str) -> str:
        return self.model_get_unity()

    def sensor_params_table(self, sensor_tuple: str) -> str:
        """Query table type_param_sensor by (sensor_type, sensor_ref). Input format : sensor_tuple(sensor_type,
        sensor_ref)"""
        sql = """
        select tp.name, tu.ref, tp.axes[1], tp.axes[2], tp.axes[3]
        from type_param_sensor as tps
        join ref_sensor rs on tps.id_ref_sensor = rs.id
        join type_sensor ts on rs.id_type_sensor = ts.id
        join type_param tp on tps.id_type_param = tp.id
        join type_unity tu on tp.id_unity = tu.id
        where ts.ref='{0}' and rs.ref='{1}'
        order by tp.name, tu.ref, tp.axes[1], tp.axes[2], tp.axes[3]
        """.format(sensor_tuple[0], sensor_tuple[1])
        return self.dql_template(sql)

    def is_exist_sensor(self, sensor_tup: tuple):
        """When deleting or adding a sensor, this interface is used to detect whether the sensor exists in database,
        sensor_tup == (sensor_type, sensor_ref, sensor_number) all of these attributes are strings"""
        sql = """
        select s.id
        from sensor as s
        join ref_sensor rs on s.id_ref_sensor = rs.id
        join type_sensor ts on rs.id_type_sensor = ts.id
        where ts.ref='{0}' and rs.ref='{1}' and s.number='{2}'
        """.format(sensor_tup[0], sensor_tup[1], sensor_tup[2])
        return self.dql_template(sql)

    def insert_sensor_location(self, sensor_tup: tuple, order: csc.State, loc: csc.Loc, vali: bool):
        """Important interface for maintaining table sensor_location. This table only provides two interfaces: append
        and read. This interface is used to append records"""
        sql = """
        insert into sensor_location(type, ref, serial_number, "order", location, time, validation) 
        values ('{0}', '{1}', '{2}', '{3}', '{4}', now(), {5})
        """.format(sensor_tup[0], sensor_tup[1], sensor_tup[2], order.value, loc.value, str(vali))
        self.dml_template(sql)

    def model_sensor_history(self, sensor_tup: tuple):
        sql = """
        select to_char(time, 'yyyy') as year, to_char(time, 'Mon') as month, to_char(time, 'dd') as day, 
        to_char(time, 'HH') as hour, to_char(time, 'MI') as minute, to_char(time, 'TZ') as timezone, type, 
        ref, serial_number, "order", location, validation 
        from sensor_location
        where type='{0}' and ref='{1}' and serial_number='{2}'
        """.format(sensor_tup[0], sensor_tup[1], sensor_tup[2])
        return self.dql_template(sql)

    def get_sensor_data(self, test_tup: tuple):
        sql = """
        select tm.type as mean_type, tm.name as mean_name, tm.number mean_number, t.number as test_number,
        ts.ref as type_sensor, rs.ref as ref_sensor, s.number as sensor_number, ds.time, 
        ds.value, tp.name as param_name, tu.ref as unity_name
        from data_sensor as ds
        join test t on ds.id_test = t.id
        join type_param tp on ds.id_type_param = tp.id
        join test_mean tm on t.id_test_mean = tm.id
        join type_unity tu on tp.id_unity = tu.id
        join sensor_coating_config scc on ds.id_sensor_coating_config = scc.id
        join sensor s on scc.id_sensor = s.id
        join ref_sensor rs on s.id_ref_sensor = rs.id
        join type_sensor ts on rs.id_type_sensor = ts.id
        where tm.type = '{0}' and tm.name = '{1}' and tm.number = '{2}' and t.number = '{3}'
        """.format(test_tup[0], test_tup[1], test_tup[2], test_tup[3])
        return self.dql_template(sql)

    def insert_sensor_data_2(self, id_test: int, id_sensor_coating_config: int, id_type_param: int, time, value):
        sql = """
        insert into data_sensor(id_test, id_sensor_coating_config, id_type_param, time, value, validate) 
        values ({0}, {1}, {2}, '{3}', {4}, True)
        """.format(id_test, id_sensor_coating_config, id_type_param, time, value)
        self.dml_template(sql)

    def is_exist_sensor_data_2(self, id_test: int, id_sensor_coating_config: int, id_type_param: int, time, value):
        sql = """
        select id from data_sensor
        where id_test={0} and id_sensor_coating_config={1} and id_type_param={2} and time='{3}' and value={4}
        """.format(id_test, id_sensor_coating_config, id_type_param, time, value)
        return self.dql_template(sql)

    def is_exist_sensor_coating_config(self, pos_id: int, sensor_id: int, tk_config_id: int):
        sql = """
        select scc.id
        from sensor_coating_config as scc
        where scc.id_position_on_tank={0} and scc.id_sensor={1} and scc.id_tank_configuration={2}
        """.format(pos_id, sensor_id, tk_config_id)
        return self.dql_template(sql)

    def is_exist_sensor_coating_config_for_tank_config(self, tk_config_str: str, loc: str):
        sql = """
        select scc.id
        from sensor_coating_config as scc
        join tank_configuration tc on scc.id_tank_configuration = tc.id
        join position_on_tank pot on scc.id_position_on_tank = pot.id
        where tc.ref='{0}' and pot.num_loc='{1}'
        """.format(tk_config_str, loc)
        return self.dql_template(sql)

    def is_exist_sensor_coating_config_reffed(self, sensor_coating_config_id: int):
        """用于查看sensor_coating_config是否被sensor_data表所引用"""
        sql = """
        select ds.id
        from data_sensor as ds
        where ds.id_sensor_coating_config={0}
        """.format(sensor_coating_config_id)
        return self.dql_template(sql)

    def insert_sensor_coating_config(self, pos_id: int, sensor_id: int, tk_config_id: int):
        sql = """
        insert into sensor_coating_config(id_position_on_tank, id_sensor, id_tank_configuration)
        values ({0}, {1}, {2})
        """.format(pos_id, sensor_id, tk_config_id)
        self.dml_template(sql)

    def model_get_all_sensor_num(self):
        sql = """
        select distinct number
        from sensor
        order by number
        """
        return self.dql_template(sql)


class TankModel(Model):
    def tank_type(self):
        """for managers"""
        sql = """select ref from type_tank order by ref"""
        return self.dql_template(sql)

    def is_exist_tank_type(self, tank_type: str) -> list:
        sql = """
        select id from type_tank where ref='{0}'
        """.format(tank_type)
        return self.dql_template(sql)

    def is_exist_tank_number(self, tank_tup: tuple):
        sql = """
        select t.id
        from tank as t 
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}' and t.number='{1}'
        """.format(tank_tup[0], tank_tup[1])
        return self.dql_template(sql)

    def tank_number_validate(self, tk_tup: tuple):
        sql = """
        select t.validate
        from tank as t 
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}' and t.number='{1}'
        """.format(tk_tup[0], tk_tup[1])
        return self.dql_template(sql)

    def is_exist_tank_pos(self, tk_tup: tuple, lc: str):
        sql = """
        select pot.id
        from tank as t 
        join type_tank tt on t.id_type_tank = tt.id
        join position_on_tank pot on t.id = pot.id_tank
        where tt.ref='{0}' and t.number='{1}' and pot.num_loc='{2}'
        """.format(tk_tup[0], tk_tup[1], lc)
        return self.dql_template(sql)

    def is_exist_tank_pos_by_tank_id(self, tk_id, lc: str):
        sql = """
        select pot.id
        from position_on_tank as pot 
        join tank t on pot.id_tank = t.id
        where t.id={0} and pot.num_loc='{1}'
        """.format(tk_id, lc)
        return self.dql_template(sql)

    def delete_tk_pos(self, pk: int):
        sql = """
        delete from position_on_tank
        where id={0}
        """.format(pk)
        self.dml_template(sql)

    def update_tank_pos(self, pk: id, element_type: str, element_pos: str, coord: tuple, met: tuple):
        coord_str = "{" + "{0}, {1}, {2}".format(coord[0], coord[1], coord[2]) + "}"
        met_str = "{{" + \
                  "{0}, {1}, {2}".format(met[0][0], met[0][1], met[0][2]) + "}, {" + \
                  "{0}, {1}, {2}".format(met[1][0], met[1][1], met[1][2]) + "}, {" + \
                  "{0}, {1}, {2}".format(met[2][0], met[2][1], met[2][2]) + "}}"
        sql = """
        update position_on_tank
        set type='{1}',
        num_loc='{2}', coord='{3}', metric='{4}' 
        where id={0}
        """.format(pk, element_type, element_pos,
                   coord_str,
                   met_str)
        self.dml_template(sql)

    def tank_number(self, tank_type: str) -> str:
        """传入tank_type，类型为str，返回tank的number"""
        sql = """
        select t.number
        from tank as t 
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}'
        order by t.number
        """.format(tank_type)
        return self.dql_template(sql)

    def insert_tank_num(self, tank_tup: tuple):
        type_id = self.is_exist_tank_type(tank_type=tank_tup[0])[0][0]
        sql = """
        insert into tank(id_type_tank, number, validate) 
        values ({0}, '{1}', False)
        """.format(type_id, tank_tup[1])
        self.dml_template(sql)

    def tank_pos(self, tank_type: str, tank_number: str) -> list:
        sql = """
        select pot.type, pot.num_loc, pot.coord[1], pot.coord[2], pot.coord[3], pot.metric[1][1], pot.metric[1][2], 
        pot.metric[1][3], pot.metric[2][1], pot.metric[2][2], pot.metric[2][3], pot.metric[3][1], pot.metric[3][2], 
        pot.metric[3][3]
        from tank as t 
        join type_tank tt on t.id_type_tank = tt.id
        join position_on_tank pot on t.id = pot.id_tank
        where tt.ref='{0}' and t.number='{1}'
        order by pot.type, pot.num_loc, pot.coord[1], pot.coord[2], pot.coord[3], pot.metric[1][1], pot.metric[1][2], 
        pot.metric[1][3], pot.metric[2][1], pot.metric[2][2], pot.metric[2][3], pot.metric[3][1], pot.metric[3][2], 
        pot.metric[3][3]
        """.format(tank_type, tank_number)
        return self.dql_template(sql)

    def is_exist_pos(self, tank_tup: tuple, element_type: str, element_pos: str, coord: tuple, met: tuple):
        coord = self.tools_array_to_string(lis=list(coord), str_type=[0, 0, 0])
        met = '{{' + '{0}, {1}, {2}'.format(met[0][0], met[0][1], met[0][2]) + \
              '}, {' + '{0}, {1}, {2}'.format(met[1][0], met[1][1], met[1][2]) + \
              '}, {' + '{0}, {1}, {2}'.format(met[2][0], met[2][1], met[2][2], met[1][0]) + '}}'

        sql = """
        select pot.id
        from position_on_tank pot
        join tank as t on t.id = pot.id_tank
        join type_tank as tt on tt.id = t.id_type_tank
        where tt.ref='{0}' and pot.type='{1}' and pot.num_loc='{2}' 
        and pot.coord='{3}' and pot.metric='{4}' and t.number='{5}'
        """.format(tank_tup[0], element_type, element_pos, coord, met, tank_tup[1])
        return self.dql_template(sql)

    def model_tank_pos_by_pos_type(self, tank_tup: tuple, sc_type: str):
        sql = """
        select distinct pot.num_loc
        from position_on_tank as pot 
        join tank t on pot.id_tank = t.id
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref = '{0}' and t.number='{1}' and pot.type='{2}'
        order by pot.num_loc
        """.format(tank_tup[0], tank_tup[1], sc_type)
        return self.dql_template(sql)

    def insert_tank_position(self, tank_tup: tuple, element_type: str, element_pos: str, coord: tuple, met: tuple):
        ret = self.is_exist_pos(tank_tup=tank_tup, element_type=element_type,
                                element_pos=element_pos, coord=coord, met=met)
        if ret:
            return False

        ret = self.is_exist_tank_number(tank_tup=tank_tup)
        ret = ret[0][0]

        coord = self.tools_array_to_string(lis=list(coord), str_type=[0, 0, 0])

        met = '{{' + '{0}, {1}, {2}'.format(met[0][0], met[0][1], met[0][2]) + \
              '}, {' + '{0}, {1}, {2}'.format(met[1][0], met[1][1], met[1][2]) + \
              '}, {' + '{0}, {1}, {2}'.format(met[2][0], met[2][1], met[2][2], met[1][0]) + '}}'

        sql = """
        insert into position_on_tank(id_tank, num_loc, coord, metric, type)
        values ({0}, '{1}', '{2}', '{3}', '{4}')
        """.format(ret, element_pos, coord, met, element_type)
        self.dml_template(sql)

        return True

    def model_find_ele_on_tank(self, tk_config_tup, ref_info):
        sql = """
        select case when s.id is not NULL and c.id is NULL then s.id
                    when s.id is NULL and c.id is not NULL then c.id
                    else -1
                    end as eid,
                case when s.id is NULL and c.id is not NULL then 1
                    when s.id is not NULL and c.id is NULL then 0
                    else -1
                    end as state

        from sensor_coating_config as scc
        join position_on_tank pot on scc.id_position_on_tank = pot.id
        join tank_configuration tc on scc.id_tank_configuration = tc.id
        left join sensor s on scc.id_sensor = s.id
        left join coating c on scc.id_coating = c.id
        join tank t on pot.id_tank = t.id
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}' and t.number='{1}' and tc.ref='{2}' and pot.num_loc='{3}'
        """.format(tk_config_tup[0], tk_config_tup[1], tk_config_tup[2], ref_info[0])
        return self.dql_template(sql)

    def model_link_ele_and_tk_pos(self, tk_config_tup, ref_info, ele_tup):
        # 获取position信息
        sql = """
        select pot.id, pot.type
        from position_on_tank as pot
        join tank t on pot.id_tank = t.id
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}' and t.number='{1}' and pot.num_loc='{2}'
        """.format(tk_config_tup[0], tk_config_tup[1], ref_info[0])
        ret = self.dql_template(sql)
        pot_id = ret[0][0]

        # 获取config的id
        sql = """
        select tc.id
        from tank_configuration as tc 
        join tank t on tc.tank_type = t.id
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}' and t.number='{1}' and tc.ref='{2}'
        """.format(tk_config_tup[0], tk_config_tup[1], tk_config_tup[2])
        tc_id = self.dql_template(sql)[0][0]

        sql = """
        insert into sensor_coating_config(id_position_on_tank, id_sensor, id_coating, id_tank_configuration) 
        values ({0}, {1}, {2}, {3})
        """.format(pot_id, 'NULL' if ele_tup[1] == 1 else str(ele_tup[0]),
                   'NULL' if ele_tup[1] == 0 else str(ele_tup[0]),
                   tc_id)
        self.dml_template(sql)

    def model_update_ele_state(self, ref: tuple, ele_tup: tuple):
        if ele_tup[1] == 0:
            # 如果为sensor
            # 首先获取sensor的type类型
            sql = """
            select ts.ref, rs.ref, s.number
            from sensor as s 
            join ref_sensor rs on s.id_ref_sensor = rs.id
            join type_sensor ts on rs.id_type_sensor = ts.id
            where s.id={0}
            """.format(ele_tup[0])
            sensor_tup = self.dql_template(sql)[0]

            sql = """
            insert into sensor_location(type, ref, serial_number, "order", location, time, validation) 
            values ('{0}', '{1}', '{2}', '{3}', '{4}', now(), True)
            """.format(sensor_tup[0], sensor_tup[1], sensor_tup[2], ref[3], ref[4])
            self.dml_template(sql)

        elif ele_tup[1] == 1:
            # 如果为coating
            sql = """
            insert into coating_location(id_coating, "order", location, date, validation) 
            values ({0}, '{1}', '{2}', now(), True)
            """.format(ele_tup[0], ref[3], ref[4])
            self.dml_template(sql)

    def vali_tank(self, tk_tup: tuple):
        ret = self.is_exist_tank_number(tank_tup=tk_tup)
        if not ret:
            return
        ret = ret[0][0]
        sql = """
        update tank
        set validate=True
        where id={0}
        """.format(ret)
        self.dml_template(sql)

    def model_tank_config(self):
        sql = """
        select distinct tc.ref
        from tank_configuration as tc 
        where tc.validate is TRUE
        order by tc.ref
        """
        return self.dql_template(sql)

    def is_exist_tank_config(self, tank_config: str):
        sql = """
        select id
        from tank_configuration
        where ref='{0}'
        """.format(tank_config)
        return self.dql_template(sql)

    def is_tank_config_validated(self, tank_config_tup: tuple):
        sql = """
        select tc.validate
        from tank_configuration as tc 
        join tank t on tc.tank_type = t.id
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}' and t.number='{1}' and tc.ref='{2}'
        """.format(tank_config_tup[0], tank_config_tup[1], tank_config_tup[2])
        return self.dql_template(sql)

    def model_validate_tk_config(self, tk_config_tup: tuple):
        sql = """
        update tank_configuration
        set validate=True
        where ref='{0}'
        """.format(tk_config_tup[2])
        self.dml_template(sql)

    def model_clone_tank_config(self, fro: str, to: str) -> tuple:
        # 查询被拷贝的config_id
        sql = """
        select tank_type
        from tank_configuration
        where ref='{0}'
        """.format(fro)
        tank_id = self.dql_template(sql)[0][0]

        # 新建新的config
        sql = """
        insert into tank_configuration(ref, date, validate, tank_type) values ('{0}', now(), False, {1})
        """.format(to, tank_id)
        self.dml_template(sql)

        # 返回新config的id
        sql = """
        select id
        from tank_configuration
        where ref = '{0}'
        """.format(to)
        new_id = self.dql_template(sql)[0][0]

        # 旧的config的id
        sql = """
        select id
        from tank_configuration
        where ref = '{0}'
        """.format(fro)
        old_id = self.dql_template(sql)[0][0]

        # 循环插入
        sql = """
        select scc.id_position_on_tank, scc.id_sensor, scc.id_coating
        from sensor_coating_config as scc
        where scc.id_tank_configuration={0}
        """.format(old_id)
        mat = self.dql_template(sql)

        count = 0
        for item in mat:
            sql = """
            insert into sensor_coating_config(id_position_on_tank, id_sensor, id_coating, id_tank_configuration) 
            values ({0}, {1}, {2}, {3})
            """.format(item[0],
                       'NULL' if item[1] is None else item[1],
                       'NULL' if item[2] is None else item[2],
                       new_id)
            self.dml_template(sql)
            count = count + 1

        return new_id, count

    def model_get_tank_id_by_tank_config(self, tank_config: str):
        sql = """
        select t.id
        from tank_configuration as tc 
        join tank t on tc.tank_type = t.id
        join type_tank tt on t.id_type_tank = tt.id
        where tc.ref = '{0}'
        """.format(tank_config)
        return self.dql_template(sql)

    def model_insert_tk_pos_without_axis(self, tk_id: int, lc: str):
        sql = """
        insert into position_on_tank(id_tank, num_loc) values ({0}, '{1}')
        """.format(tk_id, lc)
        self.dml_template(sql)

    def model_get_tk_config_tree(self):
        sql = """
        select tt.ref, t.number, tc.ref, tc.date
        from tank_configuration as tc 
        join tank t on tc.tank_type = t.id
        join type_tank tt on t.id_type_tank = tt.id
        order by tt.ref, t.number, tc.ref, tc.date
        """
        return self.dql_template(sql)

    def model_get_tank_loc(self, tank_tup: tuple):
        sql = """
        select distinct num_loc
        from position_on_tank
        join tank t on position_on_tank.id_tank = t.id
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}' and t.number='{1}'
        order by num_loc
        """.format(tank_tup[0], tank_tup[1])
        return self.dql_template(sql)

    def model_tk_config_table(self, tk_config_tup: tuple):
        sql = """
        select
        distinct pot2.num_loc, tc2.ref, c2.number, cl2."order", cl2.location
        from sensor_coating_config as scc2
        join coating c2 on scc2.id_coating = c2.id
        join type_coating tc2 on c2.id_type_coating = tc2.id
        join position_on_tank pot2 on scc2.id_position_on_tank = pot2.id
        join tank_configuration tc3 on scc2.id_tank_configuration = tc3.id
        join tank as t3 on tc3.tank_type = t3.id
        join type_tank tt2 on t3.id_type_tank = tt2.id
        join coating_location as cl2 on c2.id = cl2.id_coating
        join
        (select cl.id_coating as coating_id, max(cl.id) as latest_id
        from sensor_coating_config as scc
        join coating c on scc.id_coating = c.id
        join type_coating tc on c.id_type_coating = tc.id
        join position_on_tank pot on scc.id_position_on_tank = pot.id
        join tank_configuration t on scc.id_tank_configuration = t.id
        join tank t2 on t.tank_type = t2.id
        join type_tank tt on t2.id_type_tank = tt.id
        join coating_location cl on c.id = cl.id_coating
        where tt.ref='{0}' and t2.number='{1}' and t.ref='{2}'
        group by cl.id_coating) as t1 on t1.coating_id=c2.id and cl2.id=t1.latest_id
        """.format(tk_config_tup[0], tk_config_tup[1], tk_config_tup[2])
        mat1 = self.dql_template(sql)

        sql = """
        select
        t1.sensor_loc, t1.sensor_ref, t1.sensor_num, t2.sor, t2.slo
            from
        (select
        pot.num_loc as sensor_loc,
        rs.ref as sensor_ref,
        s.number as sensor_num,
        concat(ts.ref, '_', rs.ref, '_', s.number) as sensor_str,
        tt.ref as tank_type, t.number as tank_num, tc.ref as tank_config
            from sensor_coating_config as scc
        join sensor s on scc.id_sensor = s.id
        join ref_sensor rs on s.id_ref_sensor = rs.id
        join type_sensor as ts on rs.id_type_sensor = ts.id
        join position_on_tank pot on scc.id_position_on_tank = pot.id
        join tank_configuration tc on scc.id_tank_configuration = tc.id
        join tank t on tc.tank_type = t.id
        join type_tank tt on t.id_type_tank = tt.id) as t1
        join (select concat(sl.type, '_', sl.ref, '_', sl.serial_number) as sensor_str,
                     sl."order" as sor,
                     sl.location as slo
                  from sensor_location as sl
                      join (select max(slx.id) as latest_id
                            from sensor_location as slx
                            group by slx.type, slx.ref, slx.serial_number) as tx
                  on tx.latest_id=sl.id) as t2 on t2.sensor_str=t1.sensor_str
        where t1.tank_type='{0}' and t1.tank_num='{1}' and t1.tank_config='{2}'
        order by
            t1.sensor_loc, t1.sensor_ref, t1.sensor_num, t2.sor, t2.slo
        """.format(tk_config_tup[0], tk_config_tup[1], tk_config_tup[2])
        print(sql)
        mat2 = self.dql_template(sql)
        mat = mat1 + mat2
        return mat

    def model_delete_tk_config_row(self, tk_config_tup: tuple, loc_str: str):
        tk_config_id = self.is_exist_tank_config(tk_config_tup[2])[0][0]
        tk_id = self.is_exist_tank_number(tk_config_tup[:2])[0][0]
        pos_id = self.is_exist_tank_pos_by_tank_id(tk_id=tk_id, lc=loc_str)[0][0]
        sql = """
        delete from sensor_coating_config where id_position_on_tank={0} and id_tank_configuration={1}
        """.format(pos_id, tk_config_id)
        self.dml_template(sql)


class AcqModel(Model):
    def model_acq_config(self):
        sql = """
        select distinct ac.ref
        from acquisition_config as ac
        where ac.validate is True
        order by ac.ref
        """
        return self.dql_template(sql)

    def model_is_exist_acq_config(self, config_ref):
        sql = """
        select id
        from acquisition_config
        where ref='{0}'
        """.format(config_ref)
        return self.dql_template(sql)


class CondIniModel(Model):
    def get_air(self):
        sql = """
        select name, runway, alt
        from airfield
        order by name, runway, alt
        """
        return self.dql_template(sql)


class LoginModel(RightsModel):
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


class MenuModel(RightsModel):
    pass


class ManagementModel(RightsModel):
    def model_get_means_type(self):
        """返回means的type字段信息"""
        sql = """
            select distinct type
            from test_mean
            order by type asc
        """
        return self.dql_template(sql)

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
        self.dml_template(sql)

    def model_insert_user_right(self, uid, element_type, element_id, role_id):
        column_name = ""
        if element_type != 10 and element_type != 11:
            column_name = 'id_' + self.field_name[element_type]
        else:
            column_name = self.field_name[element_type]
        sql = """
            insert into user_right(id_account, role, {0}) values({1}, {2}, {3})
        """.format(column_name, uid, role_id, element_id)
        self.dml_template(sql)


class ItemsToBeTestedModel(InsectModel, AttributeModel, ElementModel, RightsModel):
    def model_get_coating_type_id_by_name(self, coating_type):
        """根据coating type string 查找type id"""
        sql = """
            select id
            from type_coating
            where ref = '{0}'
        """.format(coating_type)
        return self.dql_template(sql)

    def model_get_number(self, element_type, strategy=True):
        """根据coating name查找所有的number"""
        if strategy:
            sql = """
            select c.number
            from coating as c
            join type_coating as tc on c.id_type_coating = tc.id
            where tc.ref = '{0}'
            order by c.number
            """.format(element_type)
            return self.dql_template(sql)
        elif strategy is False:
            sql = """
            select d.number
            from detergent d
            join type_detergent td on d.id_type_detergent = td.id
            where td.ref='{0}'
            order by d.number
            """.format(element_type)
            return self.dql_template(sql)

    def model_create_new_element(self, element_id, number, strategy=True):
        """创建新的（coating，number）"""
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


class ListOfTestMeansModel(RightsModel, AttributeModel, TankModel, ElementModel, EjectorModel, SensorModel,
                           CameraModel):
    pass


class ListOfConfigurationModel(TankModel, SensorModel, ElementModel, RightsModel):
    def model_get_serial_number_for_coating_and_sensor(self, ref: str) -> list:
        lis = []

        sql = """
        select number
        from coating
        join type_coating tc on coating.id_type_coating = tc.id
        where tc.ref='{0}'
        order by number
        """.format(ref)
        lis1 = self.dql_template(sql)
        if lis1:
            for item in lis1:
                lis.append(item[0])

        sql = """
        select s.number
        from sensor as s 
        join ref_sensor rs on s.id_ref_sensor = rs.id
        join type_sensor ts on rs.id_type_sensor = ts.id
        where rs.ref='{0}'
        order by s.number
        """.format(ref)

        lis2 = self.dql_template(sql)
        if lis2:
            for item in lis2:
                lis.append(item[0])

        return lis

    def model_get_element_id(self, element_tup: tuple) -> tuple:
        sql = """
        select s.id
        from sensor s 
        join ref_sensor rs on s.id_ref_sensor = rs.id
        join type_sensor ts on rs.id_type_sensor = ts.id
        where rs.ref='{0}' and s.number='{1}'
        """.format(element_tup[0], element_tup[1])
        sid = self.dql_template(sql)
        if sid:
            return sid[0][0], 0

        sql = """
        select c.id
        from coating as c 
        join type_coating tc on c.id_type_coating = tc.id
        where tc.ref='{0}' and c.number='{1}'
        """.format(element_tup[0], element_tup[1])
        return self.dql_template(sql)[0][0], 1

    def model_get_ref_by_loc(self, loc: str, tk_config_tup: tuple):
        sql = """
        select pot.type
        from position_on_tank as pot
        join tank t on pot.id_tank = t.id
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}' and t.number='{1}' and pot.num_loc='{2}'
        """.format(tk_config_tup[0], tk_config_tup[1], loc)
        pot_type = self.dql_template(sql)[0][0]

        if pot_type == 'Coating':
            sql = """
            select tc.ref
            from type_coating as tc 
            order by tc.ref
            """
            return self.dql_template(sql), pot_type
        else:
            sql = """
            select rs.ref
            from ref_sensor as rs 
            join type_sensor ts on rs.id_type_sensor = ts.id
            where ts.ref='{0}'
            order by rs.ref
            """.format(pot_type)
            return self.dql_template(sql), pot_type


class TestModel(AttributeModel, ManagementModel, TankModel, AcqModel, CameraModel, ParamModel):
    def model_get_test_number(self, mean_tup: tuple):
        ret = self.get_element_id(element_name=mean_tup[0], number=mean_tup[1:], strategy=2)
        if not ret:
            # if mean not exist
            return []
        mean_id = ret[0][0]
        sql = """
        select distinct t.number
        from test as t 
        where id_test_mean={0}
        order by t.number
        """.format(mean_id)
        ret = self.dql_template(sql)
        rs = []
        for i in ret:
            vec = []
            for j in i:
                vec.append(str(j))
            rs.append(vec)
        return rs

    def model_validate_test(self, test_tup: tuple):
        means_id = self.get_element_id(element_name=test_tup[0], number=test_tup[1:3], strategy=2)[0][0]
        sql = """
        update test
        set validate=True
        where id_test_mean={0} and number='{1}'
        """.format(means_id, test_tup[3])
        self.dml_template(sql)

    def model_get_test_type_state(self, test_tup: tuple) -> list:
        sql = """
        select t.type as test_type, a.uname as test_driver, 
        t.date as date, t.time_begin, t.time_end, 
        tc.ref as tank_config, ac.ref as acq_config, cc.ref as came_config, 
        ci.cond_init as condition_inital, 
        p.pilot as pilo, p2.pilot as co_pilot, 
        a2.name as airfield, a2.runway, a2.alt as air_alt, 
        t.achievement, t.validate
        from test as t 
        left join account a on a.id = t.id_test_driver
        left join test_mean tm on t.id_test_mean = tm.id
        left join tank_configuration tc on t.id_tank_conf = tc.id
        left join acquisition_config ac on t.id_acqui_conf = ac.id
        left join config_camera cc on t.id_camera_conf = cc.id
        left join cond_init ci on t.id_cond_init = ci.id
        left join airfield a2 on ci.id_airfield = a2.id
        left join pilot p on t.id_pilot = p.id
        left join pilot p2 on t.id_copilot = p2.id
        where tm.type='{0}' and tm.name='{1}' and tm.number='{2}' and t.number='{3}'
        """.format(test_tup[0], test_tup[1], test_tup[2], test_tup[3])
        return self.dql_template(sql)

    def model_get_test_type(self):
        sql = """
        select distinct t.type 
        from test as t 
        order by t.type
        """
        return self.dql_template(sql)

    def model_test_driver(self):
        sql = """
        select distinct a.uname
        from user_right as ur 
        join account a on ur.id_account = a.id
        where ur.id_test_team is not null and ur.id_test_team <= 5
        order by a.uname
        """
        return self.dql_template(sql)

    def model_get_all_pilot(self):
        sql = """
        select distinct p.pilot
        from pilot as p
        order by p.pilot
        """
        return self.dql_template(sql)

    def model_get_pilot(self):
        # sql = """
        # select distinct p.pilot
        # from test as t
        # join pilot p on t.id_pilot = p.id
        # order by p.pilot
        # """
        # return self.dql_template(sql)
        return self.model_get_all_pilot()

    def model_get_copilot(self):
        # sql = """
        # select distinct p.pilot
        # from test as t
        # join pilot p on t.id_copilot = p.id
        # order by p.pilot
        # """
        # return self.dql_template(sql)
        return self.model_get_all_pilot()

    def get_pilot_id(self, uname):
        sql = """
        select p.id
        from pilot as p 
        where p.pilot='{0}'
        """.format(uname)
        return self.dql_template(sql)

    def insert_pilot(self, uname):
        sql = """
        insert into pilot(pilot) values ('{0}')
        """.format(uname)
        self.dml_template(sql)

    def model_is_test_exist(self, test_tup: tuple) -> list:
        sql = """
        select t.id
        from test as t 
        join test_mean tm on t.id_test_mean = tm.id
        where tm.type='{0}' and tm.name='{1}' and tm.number='{2}' and t.number='{3}'
        """.format(test_tup[0], test_tup[1], test_tup[2], test_tup[3])
        return self.dql_template(sql)

    def model_is_test_validated(self, test_tup: tuple) -> list:
        sql = """
        select t.validate
        from test as t 
        join test_mean tm on t.id_test_mean = tm.id
        where tm.type='{0}' and tm.name='{1}' and tm.number='{2}' and t.number='{3}'
        """.format(test_tup[0], test_tup[1], test_tup[2], test_tup[3])
        return self.dql_template(sql)

    def get_cond_id(self, test_tup: tuple):
        sql = """
        select id_cond_init
        from test as t 
        join test_mean tm on t.id_test_mean = tm.id
        where tm.type='{0}' and tm.name='{1}' and tm.number='{2}' and t.number='{3}'
        """.format(test_tup[0], test_tup[1], test_tup[2], test_tup[3])
        return self.dql_template(sql)

    def model_update_test(self, test_identification, test_configuration, initial_condition):
        """
        我们希望在这个函数中实现对现有的test记录更新的功能，注意不是insert而仅仅是更新

              栏位       |          类型          | 校对规则 |  可空的  |               预设
        -----------------+------------------------+----------+----------+----------------------------------
         id              | integer                |          | not null | nextval('test_id_seq'::regclass)
         id_test_mean    | integer                |          |          | id_test_name (marked)
         type            | character varying(20)  |          |          | test_identification[2]
         number          | character varying(20)  |          |          | test_number
         id_test_driver  | integer                |          |          | driver_id
         date            | date                   |          |          | test_identification[6]
         time_begin      | time without time zone |          |          | test_identification[7]
         time_end        | time without time zone |          |          | test_identification[8]
         id_tank_conf    | integer                |          |          | tank_config_id
         id_acqui_conf   | integer                |          |          | aquisition_config_id
         id_camera_conf  | integer                |          |          | camera_config_id
         id_ejector_conf | integer                |          |          | NULL
         id_cond_init    | integer                |          |          | we change in table <<cond_init>> instead
         id_pilot        | integer                |          |          | pilot_id
         id_copilot      | integer                |          |          | copilot_id
         validate        | boolean                |          |          | dont change
         achievement     | double precision       |          |          | test_identification[-1]
        """

        # 这俩是必填项，没商量的
        id_test_mean = self.get_ele_id_by_ref(table_number=0, ref_tup=test_identification[0])[0][0]
        test_number = test_identification[1][3]

        if test_identification[3] == "":
            driver_uid = None
        else:
            driver_uid = self.model_get_uid_by_uname(test_identification[3])[0][0]

        if test_configuration[0] == "":
            tank_config_id = None
        else:
            tank_config_id = self.is_exist_tank_config(test_configuration[0])[0][0]

        if test_configuration[2] == "":
            aquisition_config_id = None
        else:
            aquisition_config_id = self.model_is_exist_acq_config(test_configuration[2])[0][0]

        if test_configuration[1] == "":
            camera_config_id = None
        else:
            camera_config_id = self.model_is_camera_config_exist(ref=test_configuration[1])[0][0]

        if test_identification[4] == "":
            pilot_id = None
        else:
            pilot_id = self.get_pilot_id(test_identification[4])
            if not pilot_id:
                self.insert_pilot(test_identification[4])
            pilot_id = self.get_pilot_id(test_identification[4])[0][0]

        if test_identification[5] == "":
            copilot_id = None
        else:
            copilot_id = self.get_pilot_id(test_identification[5])
            if not copilot_id:
                self.insert_pilot(test_identification[5])
            copilot_id = self.get_pilot_id(test_identification[5])[0][0]

        condition_id = self.get_cond_id(test_identification[1])[0][0]
        self.update_initial_condition(condition_initial_id=condition_id, condition_initial=initial_condition)

        update_str = self.tools_update_with_none(type=test_identification[2], id_test_driver=driver_uid,
                                                 date=test_identification[6], time_begin=test_identification[7],
                                                 time_end=test_identification[8], id_tank_conf=tank_config_id,
                                                 id_acqui_conf=aquisition_config_id, id_camera_conf=camera_config_id,
                                                 id_pilot=pilot_id, id_copilot=copilot_id,
                                                 achievement=test_identification[-1],
                                                 str_type=["type", "date", "time_begin", "time_end"])

        sql = "update test set " + update_str + " where id_test_mean={0} and number='{1}'".format(id_test_mean,
                                                                                                  test_number)
        self.dml_template(sql)

    def update_initial_condition(self, condition_initial_id: int, condition_initial: tuple):
        # 更新json项
        sql = """
        update cond_init
        set cond_init='{1}'
        where id = {0}
        """.format(condition_initial_id, str(condition_initial[3]).replace("'", '"'))
        print(sql)
        self.dml_template(sql)

        # 更新airfield项
        sql = """
        select id_airfield
        from cond_init
        where id={0}
        """.format(condition_initial_id)
        air_field_id = self.dql_template(sql)[0][0]

        # 更新airfield
        alt_str = condition_initial[2]
        if alt_str == '':
            alt_str = 'NULL'

        sql = """
        update
        airfield
        set name='{1}', runway='{2}', alt={3}
        where id={0}
        """.format(air_field_id, condition_initial[0], condition_initial[1], alt_str)
        self.dml_template(sql)

        # 更新完毕

    def is_exist_condition_initial(self, condition_initial: tuple):
        sql = """
        select ci.id
        from cond_init as ci
        join airfield a on ci.id_airfield = a.id
        where ci.cond_init='{0}' and a.name='{1}' and a.runway='{2}' and a.alt={3}
        """.format(condition_initial[3], condition_initial[0], condition_initial[1], condition_initial[2])
        return self.dql_template(sql)

    def model_insert_test(self, test_tup: tuple):
        # 标识airfield和cond的随机数
        cond_tag, air_tag = str(int(random.random()) % 1000), str(int(random.random()) % 1000)

        # create new cond_initial
        sql = """
        insert into airfield(name, runway, alt) 
        values ('{0}', '-1', -1)
        """.format(air_tag)
        self.dml_template(sql)

        sql = """
        select id
        from airfield where name='{0}'
        """.format(air_tag)
        airfield_id = self.dql_template(sql)[0][0]

        sql = """
        insert into cond_init(cond_init, id_airfield) 
        values ('["", "", "", "", "", "", "", ""]', {0})
        """.format(airfield_id)
        self.dml_template(sql)

        sql = """
        select cond_init.id
        from cond_init
        where id_airfield={0} 
        """.format(airfield_id)
        cond_id = self.dql_template(sql)[0][0]

        means_id = self.get_element_id(element_name=test_tup[0], number=test_tup[1:3], strategy=2)[0][0]
        sql = """
        insert into test(id_test_mean, number, 
        date, time_begin, time_end, id_cond_init, validate) 
        values ({0}, '{1}', '1900-01-01', '00:00:00', '00:00:00', {2}, False)
        """.format(means_id, test_tup[3], cond_id)
        self.dml_template(sql)

        sql = """
        update airfield set name=NULL, runway=NULL, alt=NULL where id={0}
        """.format(airfield_id)
        self.dml_template(sql)

    def is_vol_data_exist(self, test_id: int, value_tup: tuple) -> list:
        param_id = self.is_exist_param(param=(value_tup[0],))[0][0]
        sql = """
        select dv.id
        from data_vol as dv
        where dv.id_test={0} and dv.time = '{1}' and dv.value = {2} and dv.id_type_param = {3}
        """.format(test_id, value_tup[1], value_tup[2], param_id)
        return self.dql_template(sql)

    def model_insert_data_vol(self, test_id: int, value_tup: tuple):
        """value_tup: (param_str, time, value)"""
        # we don't insert those rows already exist in database
        is_exist = self.is_vol_data_exist(test_id, value_tup)
        if is_exist:
            return False

        # validate = True if random.random() > 0.5 else False
        print("#INSERT " + str(value_tup))

        param_id = self.is_exist_param(param=(value_tup[0],))[0][0]
        sql = """
        insert into data_vol(id_test, id_type_param, "time", "value", validate) 
        values({0}, {1}, '{2}', {3}, True)
        """.format(test_id, param_id, value_tup[1], value_tup[2])

        self.dml_template(sql)
        return True

    def model_is_param_correct(self, test_tup: tuple, param_name: str) -> bool:
        """判断目前准备插入的单位是否存在于数据库中"""
        sql = """
        select distinct tp.name
        from type_param_test_mean
        join test_mean tm on type_param_test_mean.id_test_mean = tm.id
        join type_param tp on type_param_test_mean.id_type_param = tp.id
        where tm.type='{0}' and tm.name='{1}' and tm.number='{2}'
        order by tp.name
        """.format(test_tup[0], test_tup[1], test_tup[2])
        ret = self.dql_template(sql)
        if not ret:
            return False
        else:
            for item in ret:
                if item[0] == param_name:
                    return True
            return False

    def ops_count_table_data_vol(self, test_tup: tuple):
        """获取data_vol表的行数，单位类型个数"""
        test_id = self.model_is_test_exist(test_tup=test_tup)[0][0]
        sql = """
        select count(*) from data_vol where id_test={0}
        """.format(test_id)
        table_row = self.dql_template(sql)[0][0]

        sql = """
        select distinct id_type_param
        from data_vol
        where id_test={0}
        """.format(test_id)
        lis = self.dql_template(sql)
        param_type_number = len(lis)

        return table_row, param_type_number

    def ops_time_begin_time_end_data_vol(self, test_tup: tuple):
        test_id = self.model_is_test_exist(test_tup=test_tup)[0][0]
        sql = """
        select
        tp.name as param, 1, min(dv.time) as time_begin, max(dv.time) as time_end
        from data_vol as dv
        join type_param tp on dv.id_type_param = tp.id
        where dv.id_test={0}
        group by tp.name
        """.format(test_id)
        return self.dql_template(sql)

    def ops_is_data_vol_validate(self, test_tup: tuple) -> list:
        test_id = self.model_is_test_exist(test_tup=test_tup)[0][0]
        sql = """
        select
        distinct tp.name as param_not_validated
        from data_vol as dv
        join type_param tp on dv.id_type_param = tp.id
        where dv.id_test={0} and dv.validate=False
        group by tp.name
        """.format(test_id)
        return self.dql_template(sql)


class TestExecutionModel(ElementModel, TestModel, InsectModel, CondIniModel, SensorModel):
    def get_vol_data(self, test_tup: tuple):
        sql = """
        select tm.type as mean_type, tm.name as mean_name, tm.number mean_number, t.number as test_number, 
        dv.time as time, dv.value, tp.name, tu.ref
        from data_vol as dv
        join test t on dv.id_test = t.id
        join test_mean tm on t.id_test_mean = tm.id
        join type_param tp on dv.id_type_param = tp.id
        join type_unity tu on tp.id_unity = tu.id
        where tm.type = '{0}' and tm.name = '{1}' and tm.number = '{2}' and t.number = '{3}'
        """.format(test_tup[0], test_tup[1], test_tup[2], test_tup[3])
        return self.dql_template(sql)

    def model_get_target_list(self, means_tup: tuple):
        """获取和某一个test_mean绑定的所有单位"""
        sql = """
        select distinct tp.name
        from type_param_test_mean tptm
        join test_mean tm on tptm.id_test_mean = tm.id
        join type_param tp on tptm.id_type_param = tp.id
        where tm.type='{0}' and tm.name='{1}' and tm.number='{2}'
        order by tp.name
        """.format(means_tup[0], means_tup[1], means_tup[2])
        return self.dql_template(sql)

    def model_get_coatings_by_tk_config(self, txt):
        sql = """
        select distinct t.ref, c.number
        from sensor_coating_config as scc
        join coating c on scc.id_coating = c.id
        join tank_configuration tc on scc.id_tank_configuration = tc.id
        join type_coating t on c.id_type_coating = t.id
        where tc.ref='{0}'
        order by t.ref, c.number
        """.format(txt)
        return self.dql_template(sql)


if __name__ == '__main__':
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='postgres', pd='123456', port='5432')
    unittest_db.connect()
    model = TestExecutionModel(db_object=unittest_db)
    print(model.get_all_params()[-1][0] is not None)
