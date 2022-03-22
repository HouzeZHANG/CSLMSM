import pg_db_initial

try:
    sql = """
    INSERT INTO account(orga, uname, password) 
    VALUES ('orga1', 'tu1', '12345678');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """INSERT INTO user_right(id_account, role) VALUES (2, 5);"""
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
    INSERT INTO account(orga, uname, password)
    VALUES ('orga1', 'tu2', '12345678');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """INSERT INTO user_right(id_account, role) VALUES (3, 4);"""
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    # sql = """
    # INSERT INTO account(orga, uname, password)
    # VALUES ('root', 'root', '123456');
    # """
    # pg_db_initial.cur.execute(sql)
    # pg_db_initial.conn.commit()
    #
    # sql = """INSERT INTO user_right(id_account, role) VALUES (1, 'manager');"""
    # pg_db_initial.cur.execute(sql)
    # pg_db_initial.conn.commit()

except:
    print("fail")