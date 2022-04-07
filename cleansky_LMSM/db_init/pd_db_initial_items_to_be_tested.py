import pg_db_initial
import cleansky_LMSM.db_init.pg_db_initial_test_management


try:
    sql = """
        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (1, 'CH-1', true);
        
        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (1, 'CH-2', true);

        INSERT INTO type_unity(ref)
        values ('%');
        
        INSERT INTO attribute(attribute, id_unity, value)
        values ('Hydrochloroquine', 1, 85);
        
        INSERT INTO attribute(attribute, id_unity, value)
        values ('Aspirine', 1, 10);
        
        INSERT INTO attribute(attribute, id_unity, value)
        values ('Arsonic', 1, 5);
        
        INSERT INTO attribute_coating(id_coating, id_attribute, validate)
        values (1, 1, true);
        
        INSERT INTO attribute_coating(id_coating, id_attribute, validate)
        values (1, 2, true);
        
        INSERT INTO attribute_coating(id_coating, id_attribute, validate)
        values (1, 3, true);

        """
    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    print("test items to be tested initial success")
except:
    print("test items to be tested initial fail")
