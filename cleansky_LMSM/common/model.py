"""
https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/
"""
import database


class Model:
    def __init__(self, db_object=None):
        self.__db = db_object
        self.__controller = None

    def set_controller(self, controller_obj):
        self.__controller = controller_obj

    def get_db(self):
        return self.__db


class LoginModel(Model):
    def model_login(self, username, password):
        ls = []
        try:
            cursor = self.get_db().get_connect().cursor()
            sql = """
               select * from account where account.uname = '{0}' and account.password = '{1}'
            """.format(username, password)
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            for data in result:
                ls.append(data[0])
            cursor.close()
        except Exception:
            print("login SQL error")
        # return ls


class ManagementModel(Model):
    def model_get_orga(self):
        """Returns a de-redo record of the orga field in the Account table directly as a Python list data structure"""
        ls = []
        try:
            cursor = self.get_db().get_connect().cursor()
            sql = """
                select
                distinct a.orga
                from
                account as a
                order by
                a.orga asc
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            for data in result:
                ls.append(data[0])
            cursor.close()
        except Exception:
            print("model get_orga error")
        # return ls

    def model_get_list_of_users(self):
        """The query displays the List of users table"""
        ls = []
        try:
            cursor = self.get_db().get_connect().cursor()
            sql = """select
                        a.uname, a.orga, a.fname, a.lname, a.tel, a.email
                        from
                        account as a
                        order by
                        a.uname asc
                    """
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            for data in result:
                ls.append(data[0])
            cursor.close()
        except Exception:
            print("model get_list_of_users error")
        # return ls

    def model_get_administrator(self):
        """The query displays the List of administrator"""
        ls = []
        try:
            cursor = self.get_db().get_connect().cursor()
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
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            for data in result:
                ls.append(data[0])
            cursor.close()
        except Exception:
            print("model get_list_of_administrator error")
        # return ls


if __name__ == '__main__':
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()
    loginModel = LoginModel(db_object=unittest_db)
    loginModel.model_login('zhanghouze', '0000')

    managementModel = ManagementModel(db_object=unittest_db)
    print(managementModel.model_get_orga())
    print(managementModel.model_get_list_of_users())
    print(managementModel.model_get_administrator())
