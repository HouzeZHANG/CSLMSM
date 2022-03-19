"""
https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/
"""
import cleansky_LMSM.common.database as database


class Model:
    def __init__(self, db_object=None, transaction_mode=None):
        self.__transaction_mode = transaction_mode
        self.__db = db_object
        self.__controller = None

    def set_controller(self, controller_obj):
        self.__controller = controller_obj

    def get_db(self):
        return self.__db

    # little tools
    @staticmethod
    def tools_get_field_str_insert(locals_dict):
        """
        preparation for insert sql sentences
        input: locals()
        output: tuple of two strs where stock field name and values

        exemple:
        locals() --> {'a':1}
        return --> ['a'],['1']
        """
        field_str, value_str = "", ""
        if locals_dict is None:
            return "", ""
        for key in locals_dict.keys():
            if key != 'self' and locals_dict[key] is not None:
                field_str += (key + ', ')
                value_str += ("'" + str(locals_dict[key]) + "', ")
        field_str = field_str[:-2]
        value_str = value_str[:-2]
        return field_str, value_str

    # @staticmethod
    # def tools_get_field_str_insert(locals_dict):
    #     if locals_dict is None:
    #         return "", ""
    #     key_list = list(map(lambda x: (x+', '), list(locals_dict)))
    #     key_str = "".join(key_list)
    #     values_list = list(map(lambda x: (str(x)+', '), list(locals_dict.values())))
    #     values_str = "".join(values_list)
    #     return key_str[:-2], values_str[:-2]

    @staticmethod
    def tools_get_field_str_update(locals_dict):
        field_str = ""
        if locals_dict is None:
            return ""
        for key in locals_dict.keys():
            if key != 'self' and locals_dict[key] is not None:
                field_str += (key + ' = ' + str(locals_dict[key]) + ', ')
        field_str = field_str[:-2]
        return field_str

    # dcl interface
    def model_start_transaction(self):
        pass

    def model_roll_back(self):
        pass

    def model_submit(self):
        pass

    # sql template pattern
    def dcl_template(self, dcl, error_info='dcl error'):
        pass

    def dql_template(self, dql, error_info='dql error'):
        result = []
        try:
            cursor = self.get_db().get_connect().cursor()
            cursor.execute(dql)
            result = cursor.fetchall()
            cursor.close()
        except Exception:
            print(error_info)
        return result

    def dml_template(self, dml, error_info='dml error'):
        try:
            cursor = self.get_db().get_connect().cursor()
            print('1')
            cursor.execute(dml)
            print('2')
            self.get_db().get_connect().commit()
            print('3')
            cursor.close()
        except Exception:
            print(error_info)


class LoginModel(Model):
    def model_login(self, username, password):
        """
        Obtain user information and permission information
        if our username not exists in table account or the password is wrong, return []
        """
        sql = """
                select *
                from account as a
                join user_right ur on a.id = ur.id_account
                where
                a.uname = '{0}' and a.password = '{1}'
        """.format(username, password)
        return self.dql_template(dql=sql)


class ManagementModel(Model):
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
                a.uname, a.orga, a.fname, a.lname, a.tel, a.email
                from
                account as a
                order by
                a.uname asc
        """
        return self.dql_template(dql=sql)

    def model_get_administrator(self):
        """The query displays the List of administrator"""
        sql = """
                select
                a.orga, a.uname, a.email, a.tel
                from
                account as a
                join
                    user_right ur on a.id = ur.id_account
                where ur.role = 'administrator'
                order by
                a.orga asc, a.uname asc
        """
        return self.dql_template(dql=sql)

    def model_get_username_and_lastname(self, organisation):
        """by page 3 <les listes dependants>"""
        sql = """
                select
                uname,lname
                from
                account
                where orga='{0}'
        """.format(organisation)
        return self.dql_template(dql=sql)

    def model_get_first_name_and_lastname(self, username):
        """by page 3 <les listes dependants>"""
        sql = """
                select
                fname,lname
                from
                account
                where uname = '{0}'
        """.format(username)
        return self.dql_template(dql=sql)

    def model_get_firstname(self, lastname):
        """by page 3 <les listes depandants>"""
        sql = """
                select
                lname
                from
                account
                where lname = '{0}'
        """.format(lastname)
        return self.dql_template(dql=sql)

    def model_create_new_user(self, uname, orga=None, fname=None, lname=None, tel=None,
                              email=None, password=None):
        self.model_insert_table_account(uname=uname, orga=orga, fname=fname, lname=lname,
                                        tel=tel, email=email, password=password)
        self.model_insert_table_user_right(id_account=self.model_get_user_id(uname=uname)[0][0])

    def model_insert_table_account(self, uname, orga=None, fname=None, lname=None,
                                   tel=None, email=None, password=None):
        """by page 5"""
        tup = Model.tools_get_field_str_insert(locals())
        sql = """
                insert into account ({0})
                values ({1})
        """.format(tup[0], tup[1])
        print(sql)
        self.dml_template(dml=sql)

    def model_insert_table_user_right(self, id_account, role=None):
        tup = Model.tools_get_field_str_insert(locals())
        sql = """
                insert into user_right({0})
                values ('{1}')
        """.format(tup[0], tup[1])
        self.dml_template(dml=sql)

    def model_get_user_id(self, uname):
        sql = """
                select id from account where uname = '{0}'
        """.format(uname)
        return self.dql_template(dql=sql)

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
        print(sql)
        self.dml_template(sql)

    def model_get_user_info(self, uname):
        """
        by page 5 le choix d'un utilisateur...
        user's right also include
        if not exist, return None
        """
        sql = """
                select *
                from account as a
                join user_right ur on a.id = ur.id_account
                where uname = '{0}'
        """.format(uname)
        return self.dql_template(dql=sql)


if __name__ == '__main__':
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()

    obj = ManagementModel(db_object=unittest_db)
    obj.model_insert_table_account(uname='accountx', tel='???')
