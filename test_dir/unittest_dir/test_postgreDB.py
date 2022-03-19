import unittest
import cleansky_LMSM.common.database as database


class TestPostgreBD():
    def t_connect_by_local_host(self):
        unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
        unittest_db.connect()

    def t_connect_by_ip(self):
        unittest_db = database.PostgreDB(host='', database='testdb', user='dbuser', pd=123456, port='5432')
        unittest_db.connect()


if __name__ == '__main__':
    # unittest.main()
    test1 = TestPostgreBD()
    test1.t_connect_by_local_host()
    test1.t_connect_by_ip()
