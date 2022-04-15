import cleansky_LMSM.db_init.pg_db_initial as pg_db_initial
import cleansky_LMSM.db_init.pg_db_initial_test1_management


try:
    sql = """
        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (1, 'CH-1', true);
        
        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (1, 'CH-2', false);

        INSERT INTO type_unity(ref)
        values ('%');
        
        INSERT INTO attribute(attribute, id_unity, value)
        values ('Hydrochloroquine', 1, 85);
        
        INSERT INTO attribute(attribute, id_unity, value)
        values ('Aspirine', 1, 10);
        
        INSERT INTO attribute(attribute, id_unity, value)
        values ('Arsonic', 1, 5);
        
        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (1, 1);
        
        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (1, 2);
        
        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (1, 3);
        """

    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
        INSERT INTO type_unity(id, ref)
        VALUES (3, '');
        
        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (3, '1-Root', true);

        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (3, '2-Middle Root', true);

        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (3, '3-Middle End', true);
        
        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (3, '4-End', true);

        INSERT INTO attribute(attribute, value, id_unity)
        values ('Substrate', 19, 3);

        INSERT INTO attribute(attribute, value, id_unity)
        values ('Coating Type', 75, 3);
        
        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (3, 4);
        
        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (3, 5);
        """

    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
        INSERT INTO type_unity(id, ref)
        VALUES (2, 'cm');

        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (1, 'n1', true);

        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (1, 'n2', true);

        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (1, 'n3', true);

        INSERT INTO attribute(attribute, value, id_unity)
        values ('a1', 10, 2);
        
        INSERT INTO attribute(attribute, value, id_unity)
        values ('a2', 20, 2);
        
        INSERT INTO attribute(attribute, value, id_unity)
        values ('a3', 30, 2);
        
        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (7, 6);
        
        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (7, 7);
        
        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (8, 8);
        """

    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
        INSERT INTO insect(name , masse, )
        VALUES (2, 'cm');

        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (1, 'n1', true);

        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (1, 'n2', true);

        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (1, 'n3', true);

        INSERT INTO attribute(attribute, value, id_unity)
        values ('a1', 10, 2);

        INSERT INTO attribute(attribute, value, id_unity)
        values ('a2', 20, 2);

        INSERT INTO attribute(attribute, value, id_unity)
        values ('a3', 30, 2);

        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (7, 6);

        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (7, 7);

        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (8, 8);
        """

    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    print("test items to be tested initial success")
except:
    print("test items to be tested initial fail")
