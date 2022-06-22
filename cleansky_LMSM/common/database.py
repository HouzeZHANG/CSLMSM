from abc import ABC, abstractmethod
import psycopg2


class DataBase(ABC):
    def __init__(self, host='localhost', database=None, user=None, pd=None, port='5432'):
        self.__host = host
        self.__database = database
        self.__user = user
        self.__pd = pd
        self.__port = port

        # Params saves those params mentioned before
        self.__params = None

        self.__connect = None

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def db_close(self):
        pass

    @abstractmethod
    def get_connect_state(self):
        pass

    def set_connect(self, connect):
        self.__connect = connect

    def get_connect(self):
        return self.__connect

    def set_pd(self, pd):
        self.__pd = pd

    def get_pd(self):
        return self.__pd

    def set_user(self, user):
        self.__user = user

    def get_user(self):
        return self.__user

    def set_host(self, host):
        self.__host = host

    def get_host(self):
        return self.__host

    def set_database(self, database):
        self.__database = database

    def get_database(self):
        return self.__database

    def set_port(self, port):
        self.__port = port

    def get_port(self):
        return self.__port

    def set_params(self):
        pass

    def get_params(self):
        pass

    def read_config_file(self):
        """By configuration file"""
        pass

    def __repr__(self):
        pass


class PostgreDB(DataBase):
    def db_close(self):
        self.get_connect().close()

    def __repr__(self):
        return "[PostgreSQL Database Object]\n[DB name] - " + self.get_database() + "\n[User] - " + self.get_user()

    def read_config_file(self):
        # wait for add
        pass

    def connect(self):
        try:
            print("\nConnecting to the PostgreSQL database...\n")
            if self.get_params() is None:
                self.set_connect(psycopg2.connect(host=self.get_host(),
                                                  dbname=self.get_database(),
                                                  user=self.get_user(),
                                                  password=self.get_pd(),
                                                  port=self.get_port()))
                print("Connect success...\n")
                # should add else for connect by params
                cursor = self.get_connect().cursor()

                print("PG version :")
                cursor.execute('select version()')
                db_version = cursor.fetchone()
                print(db_version[0]+'\n')
                cursor.close()

                # 自提交取消
                if self.get_connect().autocommit is True:
                    self.get_connect().autocommit = False

        except (Exception, psycopg2.DatabaseError) as error:
            # wait for modify
            print("error")

    def get_connect_state(self):
        pass


if __name__ == '__main__':
    unittest_db = PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()
