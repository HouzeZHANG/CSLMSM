import cleansky_LMSM.db_init.pg_db_initial_root_account
import cleansky_LMSM.db_init.pg_db_initial as pg_db_initial

# try:
#     sql = """
#     INSERT INTO account(orga, uname, password)
#     VALUES ('orga1', 'tu1', '12345678');
#     """
#     pg_db_initial.cur.execute(sql)
#     pg_db_initial.conn.commit()
#
#     sql = """
#     INSERT INTO account(orga, uname, password)
#     VALUES ('orga1', 'tu2', '12345678');
#     """
#     pg_db_initial.cur.execute(sql)
#     pg_db_initial.conn.commit()
#
# except:
#     print("fail")


try:
    """
    COATING INITIAL
    """
    sql = """
    INSERT INTO type_coating(ref)
    VALUES ('CHOPIN');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
        INSERT INTO type_coating(ref)
        VALUES ('COVID-19');
        """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
        INSERT INTO type_coating(ref)
        VALUES ('STELLAR.WP5.CID.COAT');
        """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    """
    DETERGENT INITIAL
    """
    sql = """
    INSERT INTO type_detergent(ref)
    VALUES ('SOPURA.STELLAR');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
        INSERT INTO type_detergent(ref)
        VALUES ('VACINNE');
        """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    """
    TEST MEANS INTIAL
    """
    sql = """INSERT INTO test_mean(type, name, number, validate) 
            VALUES ('Aircraft', 'A320', '1258', False);
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """INSERT INTO test_mean(type, name, number, validate) 
                VALUES ('Aircraft', 'SONACA 200', '12', False);
        """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """INSERT INTO test_mean(type, name, number, validate) 
                VALUES ('Aircraft', 'SONACA 200', '25', True);
            """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """INSERT INTO test_mean(type, name, number, validate) 
                VALUES ('Wind tunnel', 'CWT', '1', False);
            """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """INSERT INTO test_mean(type, name, number, validate) 
                VALUES ('Wind tunnel', 'VKI', 'L1-A', True);
            """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    """
    TANK INITIAL
    """
    sql = """
    INSERT INTO type_tank(ref)
    VALUES ('T_Snonaca 200');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
    INSERT INTO type_tank(ref)
    VALUES ('Slat A320');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    """
    SENSOR INITIAL
    """
    sql = """
    INSERT INTO type_sensor(ref)
    VALUES ('Barometric');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
    INSERT INTO type_sensor(ref)
    VALUES ('Accelerometer');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()


    """
    CAMERA INITIAL
    """
    sql = """
    INSERT INTO type_camera(ref)
    VALUES ('UV7076');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()


    """
    EJECTOR INITIAL
    """
    sql = """
    INSERT INTO type_ejector(ref)
    VALUES ('Chopin ejector');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    """
    TEAM INITIAL
    """
    sql = """
    INSERT INTO test_team(ref)
    VALUES ('Flight team');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
    INSERT INTO test_team(ref)
    VALUES ('Wind Tunnel team');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    """
    TEST POINT INITIAL
    """
    sql = """
    INSERT INTO type_test_point(ref)
    VALUES ('Cleanability');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
    INSERT INTO type_test_point(ref)
    VALUES ('Climb-out');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
    INSERT INTO type_test_point(ref)
    VALUES ('Insect Residues');
    """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    # """
    # INTRINSIC VALUE INITIAL
    # """
    # sql = """
    # INSERT INTO type_test_point(ref)
    # VALUES ('Cleanability');
    # """
    # pg_db_initial.cur.execute(sql)
    # pg_db_initial.conn.commit()


    print("initial config success")
except:
    print("fail")


try:
    sql = """
        INSERT INTO account(orga, uname, password, fname, lname)
        VALUES ('orga_1', 'validator', '0000', 'fname1', 'lname1');
        """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
        INSERT INTO user_right(id_account, role, id_test_mean)
        VALUES (3, 2, 1);
        """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
            INSERT INTO account(orga, uname, password, fname, lname)
            VALUES ('orga_1', 'creator', '0000', 'fname2', 'lname2');
            INSERT INTO account(orga, uname, password, fname, lname)
            VALUES ('orga_1', 'reader', '0000', 'fname2', 'lname2');
            """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
        INSERT INTO user_right(id_account, role, insect)
        VALUES (3, 4, true);
        INSERT INTO user_right(id_account, role, insect)
        values (4, 5, false);
        INSERT INTO user_right(id_account, role, acqui_system)
        values (3, 5, false);
        INSERT INTO user_right(id_account, role, id_test_mean)
        values (4, 2, 2);
        INSERT INTO user_right(id_account, role, id_type_coating)
        values (3, 3, 1);
        INSERT INTO user_right(id_account, role, id_type_coating)
        values (4, 4, 1);
        INSERT INTO user_right(id_account, role, id_type_coating)
        values (5, 5, 1);
        """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
        INSERT INTO account(uname, password)
        VALUES ('nobody', '0000');
        
        INSERT INTO user_right(id_account, role)
        VALUES (6, 6);
        """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    print("test_management initial success")
except:
    print("test_management initial fail")
