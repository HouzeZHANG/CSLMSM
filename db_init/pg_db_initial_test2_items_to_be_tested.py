import db_init.pg_db_initial as pg_db_initial

try:
    sql = """
        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (1, 'CH-1', true);
        
        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (1, 'CH-2', false);

        INSERT INTO type_unity(ref)
        values ('%');
        
        INSERT INTO type_unity(ref)
        VALUES ('');
        
        INSERT INTO type_unity(ref)
        VALUES ('cm');
        
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
        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (2, '1-Root', true);

        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (2, '2-Middle Root', true);

        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (2, '3-Middle End', true);
        
        INSERT INTO coating(id_type_coating, number, validate)
        VALUES (2, '4-End', true);

        INSERT INTO attribute(attribute, value, id_unity)
        values ('Substrate', 19, 3);

        INSERT INTO attribute(attribute, value, id_unity)
        values ('Coating Type', 75, 3);
        
        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (2, 4);
        
        INSERT INTO attribute_coating(id_coating, id_attribute)
        values (2, 5);
        """

    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    sql = """
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

    sql = """
        insert into insect(name, masse, alt_min, alt_max, length, width, thickness, hemolymphe)
        values ('Beattle', 0.05, 1500, 2000, 5, 0.75, 1.2, '');
        insert into insect(name, masse, alt_min, alt_max, length, width, thickness, hemolymphe)
        values ('Bombyx', 0.05, 3500, 4250, 7, 1.05, 1.3, '');
        insert into insect(name, masse, alt_min, alt_max, length, width, thickness, hemolymphe)
        values ('Butterfly', 0.05, 1000, 1500, 3.5, 0.5, 0.9, '');
        insert into insect(name, masse, alt_min, alt_max, length, width, thickness, hemolymphe)
        values ('Fly', 0.5, 1400, 1800, 10.5, 2.5, 1.9, '');
        insert into insect(name, masse, alt_min, alt_max, length, width, thickness, hemolymphe)
        values ('Mosquito', 0.07, 10, 50, 1.35, 0.5, 0.8, '');
        insert into insect(name, masse, alt_min, alt_max, length, width, thickness, hemolymphe)
        values ('Spider', 0.1, 4500, 5000, 8.35, 3.5, 2.8, '');
        """

    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    print("test items to be tested initial success")
except:
    print("test items to be tested initial fail")
