# import cleansky_LMSM.common.controller as controller
# import cleansky_LMSM.common.database as database
#
# if __name__ == '__main__':
#     unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
#     unittest_db.connect()
#     obj = controller.LoginController(db_object=unittest_db)
#     obj.run_view()


import test_dir.unittest_dir.test_Model as tmodel


if __name__ == '__main__':
    myobj = tmodel.TestModel()
    myobj.test_dml_template()