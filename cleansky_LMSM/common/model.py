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
        except Exception:
            print(error_info)

    def dql_template(self, dql, error_info='dql error'):
        """dql模板方法；如果没查到数据，返回空表[]；如果查到数据，以元组列表的形式返回数据：[(1, 2, 3), (4, 5, 6)]"""
        result = []
        try:
            cursor = self.get_db().get_connect().cursor()
            cursor.execute(dql)
            result = cursor.fetchall()
            cursor.close()
            # logging.info('dql success')
        except Exception:
            # logging.error(error_info)
            print(error_info + dql)
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

    def model_get_role_ref(self, role_id):
        """通过id获取特定权限的ref"""
        sql = """select ref from type_role where id = {0}""".format(role_id)
        return self.dql_template(sql)

    def model_get_role_id(self, role_ref):
        """通过ref获取特定权限的ref"""
        sql = """select id from type_role where ref='{0}'""".format(role_ref)
        return self.dql_template(sql)

    def model_get_simple_ele(self, table_name, ele_id):
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
        info.append(self.model_get_role_ref(lis[0])[0][0])
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
    def tools_array_to_string(lis: list, str_type: list) -> str:
        """
        lis传递待插入数据数组，
        str_type传递01编码的等长串，0代表不需要添加双引号，1代表为字符型数据，需要添加双引号
        用于配置PostgreSQL中用于insert语句的字符串，便于转换数组
        """
        index, array_string = 0, ''
        while index < len(lis):
            if str_type[index] == 1:
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

    def test_means_str_by_uid(self, uid):
        """用uid获取他所拥有权限的test_means的字符串信息"""
        sql = """
            select tm.type, tm.name, tm.number
            from user_right as ur
            join test_mean tm on ur.id_test_mean = tm.id
            where id_account = '{0}'
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
        """
        param查询
        table type_param和table type_unity相连接，返回param name， param type unity， param axes
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
            array_list = self.tools_array_to_string(param[2], str_type=[0, 0, 0])
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
                  " where id_type_sensor={0} and id_type_param={1}".format(element_id, param_id)
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
            return self.dml_template(sql)
        elif strategy == 1:
            sql = """
                insert into type_param_sensor(id_type_sensor, id_type_param) values ({0}, {1})
            """.format(element_id, param_id)
            return self.dml_template(sql)

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
            id_type_sensor = {0} and id_type_param = {1}
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
            id_type_sensor = {0}
            """.format(element_id)
            return self.dml_template(sql)

    def delete_param(self, param: tuple):
        """type_param表被多张param表引用，本方法不包含对param的检查"""
        pass

    def is_exist_param(self, param: tuple) -> list:
        unity_id = self.model_is_unity_exist(param[1])
        if not unity_id:
            # 如果连单位都没有，说明肯定不存在该param
            return []
        unity_id = unity_id[0][0]
        if len(param) == 3:
            array_list = self.tools_array_to_string(param[2], str_type=[0, 0, 0])
            sql = """
            select id from type_param as tp
            where name='{0}' and id_unity={1} and axes='{2}'
            """.format(param[0], unity_id, array_list)
            return self.dql_template(sql)
        else:
            # 传入的数据不包括axes项
            sql = """
            select id from type_param as tp
            where name='{0}' and id_unity={1} and axes is null 
            """.format(param[0], unity_id)
            return self.dql_template(sql)


class SensorModel(ParamModel):
    def sensor_type(self) -> list:
        sql = """select ref from type_sensor order by asc"""
        return self.dql_template(sql)

    def sensor_reference(self, sensor_type: str) -> list:
        """
        用sensor type获得reference
        """
        sql = """
        select s.type
        from sensor as s 
        join type_sensor ts on ts.id = s.id_type_sensor
        where ts.ref='{0}'
        """.format(sensor_type)
        return self.dql_template(sql)

    def sensor_number(self, sensor_type: str, sensor_ref: str) -> list:
        sql = """
        select s.number
            from sensor as s
        join type_sensor ts on ts.id = s.id_type_sensor
        where ts.ref='{0}' and s.type='{1}'
        """.format(sensor_type, sensor_ref)
        return self.dql_template(sql)

    def sensor_order_and_config(self, sensor_type: str, sensor_ref: str, sensor_num: str):
        """数据库关键字作为字段"""
        sql = """
        select s."order", s.calibration
            from sensor as s
        join type_sensor ts on s.id_type_sensor = ts.id
        where
            ts.ref='{0}' and s.type='{1}' and s.number='{2}'
        """.format(sensor_type, sensor_ref, sensor_num)
        return self.dql_template(sql)

    def sensor_table(self, sensor_type: str, sensor_ref: str) -> list:
        sql = """
        select s.number, s.order, s.calibration
            from sensor as s
        join type_sensor ts on ts.id = s.id_type_sensor
        where ts.ref='{0}' and s.type='{1}'
        """.format(sensor_type, sensor_ref)
        return self.dql_template(sql)

    def sensor_insert(self, **kwargs):
        pass

    def sensor_delete(self, sensor_type: str, sensor_ref: str, sensor_num: str):
        pass

    def sensor_param(self, sensor_type: str) -> str:
        return self.get_all_params()

    def sensor_unity(self, sensor_type: str) -> str:
        return self.model_get_unity()

    def sensor_params_table(self, sensor_type: str) -> str:
        sql = """
        select tp.name, tu.ref, tp.axes
            from type_param_sensor as tps
        join type_sensor ts on tps.id_type_sensor = ts.id
        join type_param tp on tps.id_type_param = tp.id
        join type_unity tu on tp.id_unity = tu.id
        where ts.ref='{0}'
        """.format(sensor_type)
        return self.dql_template(sql)


class TankModel(Model):
    def tank_type(self):
        sql = """select ref from type_tank order by ref asc"""
        return self.dql_template(sql)

    def tank_number(self, type_id):
        sql = """
        select number, validate
        from tank where id_type_tank == {0}
        order by number asc 
        """.format(type_id)
        return self.dql_template(sql)

    def tank_pos(self, tank_type: str, tank_num: str) -> str:
        sql = """
        select pot.ref
            from position_on_tank as pot
        join tank t on pot.id_tank = t.id
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}' and t.number='{1}'
        """.format(tank_type, tank_num)
        return self.dql_template(sql)

    def tank_point_id(self, tank_type: str, tank_num: str) -> str:
        sql = """
        select pot.num_loc
            from position_on_tank as pot
        join tank t on pot.id_tank = t.id
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}' and t.number='{1}'
        """.format(tank_type, tank_num)
        return self.dql_template(sql)

    def tank_tank_table(self, tank_type: str, tank_num: str) -> str:
        sql = """
        select pot.type, pot.ref, pot.num_loc, pot.coord, pot.metric
            from position_on_tank as pot
        join tank t on pot.id_tank = t.id
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}' and t.number='{1}'
        """.format(tank_type, tank_num)
        return self.dql_template(sql)

    def insert_pos(self, **kwargs):
        pass

    def delete_pos(self, **kwargs):
        pass

    def is_tank_validate(self, tank_type: str, tank_number: str) -> list:
        sql = """
        select t.validate
            from tank as t 
        join type_tank tt on t.id_type_tank = tt.id
        where tt.ref='{0}' and t.number='{1}'
        """.format(tank_type, tank_number)
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
            insert into user_right(id_account, role, {0})
            values({1}, {2}, {3})
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


if __name__ == '__main__':
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()

    model = EjectorModel(db_object=unittest_db)
    # print(model.tools_array_to_string(lis=['x', 'y', 'z'], str_type=[1, 0, 1]))
    model = ParamModel(db_object=unittest_db)
    model.create_new_param(param=('abc', 1, [1, 2, 3]))

    model.model_commit()
