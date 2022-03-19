from test_dir.unittest_config import *


class TestModel:
    def test_get_field_list(self):
        class GetFieldSample:
            self.name = 'class_name'

            @staticmethod
            def fun_1(a, b, c):
                return locals()

            @classmethod
            def fun_2(self, a, b, c):
                self.name = "class_name_2"
                return locals()

            @classmethod
            def fun_5(self, a, b, c=None):
                self.name = "class_name_2"
                return locals()

            @staticmethod
            def fun_6(a, b, c=None):
                return locals()

            @staticmethod
            def fun_3():
                return locals()

            @classmethod
            def fun_4(self):
                return locals()

        obj = GetFieldSample()
        assert model.Model.tools_get_field_str_insert(GetFieldSample.fun_1(a=1, b=2, c=3)) == ('a, b, c', "'1', '2', '3'")
        assert model.Model.tools_get_field_str_insert(obj.fun_2(a=1, b=2, c=3)) == ('a, b, c', "'1', '2', '3'")
        assert model.Model.tools_get_field_str_insert(obj.fun_2(a=1, b=2, c=None)) == ('a, b', "'1', '2'")
        assert model.Model.tools_get_field_str_insert(GetFieldSample.fun_3()) == ('', '')
        assert model.Model.tools_get_field_str_insert(GetFieldSample.fun_5(a=1, b=2)) == ('a, b', "'1', '2'")
        assert model.Model.tools_get_field_str_insert(obj.fun_6(a=1, b=2)) == ('a, b', "'1', '2'")

    def test_tools_get_field_str_update(self):
        class GetFieldSample:
            self.name = 'class_name'

            @staticmethod
            def fun_1(a, b, c):
                return locals()

            @classmethod
            def fun_2(self, a, b, c):
                self.name = "class_name_2"
                return locals()

            @classmethod
            def fun_5(self, a, b, c=None):
                self.name = "class_name_2"
                return locals()

            @staticmethod
            def fun_6(a, b, c=None):
                return locals()

            @staticmethod
            def fun_3():
                return locals()

            @classmethod
            def fun_4(self):
                return locals()

        obj = GetFieldSample()
        assert model.Model.tools_get_field_str_update(GetFieldSample.fun_1(a=1, b=2, c=3)) == 'a = 1, b = 2, c = 3'
        assert model.Model.tools_get_field_str_update(obj.fun_2(a=1, b=2, c=3)) == 'a = 1, b = 2, c = 3'
        assert model.Model.tools_get_field_str_update(obj.fun_2(a=1, b=2, c=None)) == 'a = 1, b = 2'
        assert model.Model.tools_get_field_str_update(GetFieldSample.fun_3()) == ''
        assert model.Model.tools_get_field_str_update(GetFieldSample.fun_5(a=1, b=2)) == 'a = 1, b = 2'
        assert model.Model.tools_get_field_str_update(obj.fun_6(a=1, b=2)) == 'a = 1, b = 2'

    def test_dql_template(self):
        """
        检查dql模板方法的正确性
        在数据库中默认设置一个root账户,其userid为1，这是在数据库配置文件中设定好的
        """
        my_model = model.Model(db_object=db_test_object)
        dql = """
        select id from account where uname='root'
        """
        assert my_model.dql_template(dql=dql) == [(1,)]

    def test_dml_template(self):
        """
        检查dml模板方法的正确性
        插入insert_test用户，dql查询该用户的是否存在于account中，随后删除该用户，再次查询
        """
        my_model = model.Model(db_object=db_test_object)
        dml = """
        insert into account (uname)
        values ('insert_test')
        """
        my_model.dml_template(dml=dml)
        dql = """
        select uname from account where uname='insert_test'
        """
        print(my_model.dql_template(dql=dql))
        assert my_model.dql_template(dql=dql) == [('insert_test',)]
        dml = """
        delete from account
        where
        uname='insert_test'
        """
        my_model.dml_template(dml=dml)
        dql = """
        select uname from account where uname='insert_test'
        """
        print(my_model.dql_template(dql=dql))
        assert my_model.dql_template(dql=dql) == []


class TestLoginModel:
    def test_login_success_1(self):
        """
        尝试登录root用户
        """
        my_model = model.LoginModel(db_object=db_test_object)
        assert my_model.model_login('root', '123456') == [(1, 'root', 'root', None, None, None,
                                                           None, '123456', 1, 1, 'manager', None, None, None,
                                                           None, None, None, None, None, None, None, None)]

    def test_login_failed_1(self):
        """
        without password
        """
        my_model = model.LoginModel(db_object=db_test_object)
        assert my_model.model_login('root', '') == []

    def test_login_failed_2(self):
        """
        without password and username
        """
        my_model = model.LoginModel(db_object=db_test_object)
        assert my_model.model_login('', '') == []

    def test_login_failed_3(self):
        """
        without username
        """
        my_model = model.LoginModel(db_object=db_test_object)
        assert my_model.model_login('', '123456') == []


class TestManagementModel:
    def test_get_organisation(self):
        """
        organisation which name is root should be included in the result of this method
        """
        my_model = model.ManagementModel(db_object=db_test_object)
        assert ('root',) in my_model.model_get_orga()

    def test_get_list_of_users(self):
        my_model = model.ManagementModel(db_object=db_test_object)
        assert ('root', 'root', None, None, None, None) in my_model.model_get_list_of_users()

    def test_get_administrator(self):
        pass

    def test_get_username_and_organisation(self):
        pass

    def test_get_first_name_and_lastname(self):
        my_model = model.ManagementModel(db_object=db_test_object)
        my_model.model_insert_table_account(uname='test_sample', fname='firstname', lname='his_lastname')
        assert my_model.model_get_first_name_and_lastname('test_sample') == [('firstname', 'his_lastname')]
        my_model.model_delete_user(uname='test_sample')

    def get_firstname(self):
        pass

    def test_insert_table_account_1(self):
        my_model = model.ManagementModel(db_object=db_test_object)
        my_model.model_insert_table_account(uname='test_account')
        sql = """
        select uname
        from account
        where uname='test_account'
        """
        assert my_model.dql_template(sql) == [('test_account',)]
        my_model.model_delete_user('test_account')
        assert my_model.dql_template(sql) == []

    def test_create_new_user(self):
        pass

    def test_insert_table_user_right(self):
        pass

    def test_get_user_id(self):
        pass

    def test_delete_user(self):
        pass

    def test_update_user(self):
        pass

    def test_get_user_info(self):
        pass


if __name__ == '__main__':
    obj = TestModel()
    obj.test_dml_template()
