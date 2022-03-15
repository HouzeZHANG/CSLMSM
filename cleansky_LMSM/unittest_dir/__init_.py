import cleansky_LMSM.common.database as db

unittest_db = db.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
