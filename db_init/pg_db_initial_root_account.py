import db_init.pg_db_initial as pg_db_initial
try:
    sql = """
    INSERT INTO account(orga, uname, password) 
    VALUES ('root', 'root', '123456');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()
    sql = """
    INSERT INTO account(orga, uname, password) 
    VALUES ('group_manager', 'manager', '123456');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """INSERT INTO type_role(id, ref) VALUES (1, 'manager');"""
    sql += """INSERT INTO type_role(id, ref) VALUES (2, 'administrator');"""
    sql += """INSERT INTO type_role(id, ref) VALUES (3, 'valideur');"""
    sql += """INSERT INTO type_role(id, ref) VALUES (4, 'creator');"""
    sql += """INSERT INTO type_role(id, ref) VALUES (5, 'reader');"""
    sql += """INSERT INTO type_role(id, ref) VALUES (6, 'none');"""
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """INSERT INTO user_right(id_account, role) VALUES (1, 1);"""
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()
    sql = """INSERT INTO user_right(id_account, role) VALUES (2, 1);"""
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()
    print("root initial success")

except:
    print("root initial fail")

