import cleansky_LMSM.db_init.pg_db_initial as pg_db_initial
import cleansky_LMSM.db_init.pg_db_initial_test2_items_to_be_tested

try:
    sql = """
        INSERT INTO type_unity(ref)
        VALUES ('ft');
        INSERT INTO type_unity(ref)
        VALUES ('kt');
        INSERT INTO type_unity(ref)
        VALUES ('deg');
        
        INSERT INTO attribute (attribute, id_unity, value)
        VALUES ('Altitude', 4, 3000);
        INSERT INTO attribute (attribute, id_unity, value)
        VALUES ('Max Speed', 5, 120);
        INSERT INTO attribute (attribute, id_unity, value)
        VALUES ('Wing setting', 6, 1.5);
        
        INSERT INTO attribute_test_mean(id_test_mean, id_attribute)
        VALUES(2, 9);
        INSERT INTO attribute_test_mean(id_test_mean, id_attribute)
        VALUES(2, 10);
        INSERT INTO attribute_test_mean(id_test_mean, id_attribute)
        VALUES(2, 11);
        
        INSERT INTO type_unity(ref)
        values('hh:mm:ss');
        
        INSERT INTO type_unity(ref)
        values('hh:mm');
        
        INSERT INTO type_unity(ref)
        values('ft Baro');
        
        INSERT INTO type_unity(ref)
        values('degrees');
        
        INSERT INTO type_unity(ref)
        values('ftmsl');
        
        INSERT INTO type_param(name, id_unity)
        values('Ld Time', 7);
        
        INSERT INTO type_param(name, id_unity)
        values('Ld Time', 7);
        INSERT INTO type_param(name, id_unity)
        values('UTCOfst', 8);
        INSERT INTO type_param(name, id_unity)
        values('AltB', 9);
        INSERT INTO type_param(name, id_unity)
        values('Latitude', 10);
        INSERT INTO type_param(name, id_unity)
        values('Longitude', 10);
        INSERT INTO type_param(name, id_unity)
        values('AltMSL', 11);
        INSERT INTO type_param(name, id_unity)
        values('IAS', 5);
        INSERT INTO type_param(name, id_unity)
        values('Pitch', 6);
        INSERT INTO type_param(name, id_unity)
        values('Roll', 6);
        
        INSERT INTO type_param_test_mean(id_test_mean, id_type_param)
        values(2, 1);
        INSERT INTO type_param_test_mean(id_test_mean, id_type_param)
        values(2, 2);
        INSERT INTO type_param_test_mean(id_test_mean, id_type_param)
        values(2, 3);
        INSERT INTO type_param_test_mean(id_test_mean, id_type_param)
        values(2, 4);
        INSERT INTO type_param_test_mean(id_test_mean, id_type_param)
        values(2, 5);
        INSERT INTO type_param_test_mean(id_test_mean, id_type_param)
        values(2, 6);
        INSERT INTO type_param_test_mean(id_test_mean, id_type_param)
        values(2, 7);
        INSERT INTO type_param_test_mean(id_test_mean, id_type_param)
        values(2, 8);
        INSERT INTO type_param_test_mean(id_test_mean, id_type_param)
        values(2, 8);
        """

    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    print("test3 initial")
except:
    print("test 3 initial fail")
