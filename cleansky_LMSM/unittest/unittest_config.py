import cleansky_LMSM.common.database as database

# 初始化数据库

db_test_object = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
db_test_object.connect()
