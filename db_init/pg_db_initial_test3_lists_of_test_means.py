import db_init.pg_db_initial as pg_db_initial
import db_init.pg_db_initial_test2_items_to_be_tested

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
        values('ftmsl');
        
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
        values('AltMSL', 5);
        INSERT INTO type_param(name, id_unity)
        values('IAS', 5);
        INSERT INTO type_param(name, id_unity)
        values('Pitch', 6);
        INSERT INTO type_param(name, id_unity)
        values('Roll', 6);
        
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
        
        insert into ref_sensor(id_type_sensor, ref) VALUES (1, 'LIS3DH');
        insert into type_unity (ref) values ('g');
        
        insert into type_param(name, id_unity, axes) 
        values ('Gama x', 9, '{1, 0, 0}');
        insert into type_param(name, id_unity, axes) 
        values ('Gama y', 9, '{0, 1, 0}');
        insert into type_param(name, id_unity, axes) 
        values ('Gama z', 9, '{0, 0, 1}');
        
        insert into type_param_sensor (id_ref_sensor, id_type_param) values (1, 10);
        insert into type_param_sensor (id_ref_sensor, id_type_param) values (1, 11);
        insert into type_param_sensor (id_ref_sensor, id_type_param) values (1, 12);
        
        insert into sensor(id_ref_sensor, number, validate) 
        values (1, '001', True);
        
        insert into sensor(id_ref_sensor, number, validate) 
        values (1, '002', True);
        
        insert into sensor_location(type, ref, serial_number, "order", location, time, validation) 
        values ('Barometric', 'LIS3DH', '001', 'order', 'in store', now(), True);
        
        insert into sensor_location(type, ref, serial_number, "order", location, time, validation) 
        values ('Barometric', 'LIS3DH', '002', 'order', 'in store', now(), True);
        
        insert into tank(id_type_tank, number, validate) values (2, 'tk_00', False);
        insert into tank(id_type_tank, number, validate) values (2, 'tk_01', False);
        
        insert into tank_configuration(ref, date, validate, tank_type) values ('tk_config_01', now(), True, 2);
        insert into tank_configuration(ref, date, validate, tank_type) values ('tk_config_02', now(), False, 2);
        
        insert into position_on_tank(id_tank, num_loc, coord, metric, type) 
        values (2, '99-99', '{158.3, 1029, 100.0}', '{{1.3,2.4,5.5}, {11,23,79},{111,222,333}}', 'Barometric');
        insert into position_on_tank(id_tank, num_loc, coord, metric, type) 
        values (2, '100-100', '{158.3, 119, 120}', '{{1.3,2.4,7}, {11,23,79},{111,222,333}}', 'Barometric');
        insert into position_on_tank(id_tank, num_loc, coord, metric, type) 
        values (2, '101-102', '{158.3, 1029, 100.0}', '{{1.3,2.4,5.5}, {11,23,79},{111,222,333}}', 'Barometric');
        insert into position_on_tank(id_tank, num_loc, coord, metric, type) 
        values (2, '102-103', '{158.3, 119, 120}', '{{1.3,2.4,7}, {11,23,79},{111,222,333}}', 'Barometric');
        
        
        insert into position_on_tank(id_tank, num_loc, coord, metric, type) 
        values (2, '999-999', '{158.3, 119, 120}', '{{1.3,2.4,7}, {11,23,79},{111,222,333}}', 'Coating');
        
        insert into position_on_tank(id_tank, num_loc, coord, metric, type) 
        values (2, '555-555', '{158.3, 119, 120}', '{{1.3,2.4,7}, {11,23,79},{111,222,333}}', 'Accelerometer');
        insert into position_on_tank(id_tank, num_loc, coord, metric, type) 
        values (2, '444-444', '{158.3, 119, 120}', '{{1.3,2.4,7}, {11,23,79},{111,222,333}}', 'Accelerometer');
        
        insert into sensor_coating_config(id_position_on_tank, id_sensor, id_tank_configuration) 
        values (1, 1, 2);
        insert into sensor_coating_config(id_position_on_tank, id_sensor, id_tank_configuration) 
        values (2, 2, 2);
        insert into sensor_coating_config(id_position_on_tank, id_coating, id_tank_configuration) 
        values (5, 1, 2);
        
        insert into sensor_coating_config(id_position_on_tank, id_sensor, id_tank_configuration) 
        values (1, 1, 1);
        insert into sensor_coating_config(id_position_on_tank, id_sensor, id_tank_configuration) 
        values (2, 2, 1);
        insert into sensor_coating_config(id_position_on_tank, id_coating, id_tank_configuration) 
        values (5, 3, 1);
        
        insert into ref_sensor(id_type_sensor, ref) values (2, 'AccS1');
        insert into ref_sensor(id_type_sensor, ref) values (2, 'AccS2');
        insert into ref_sensor(id_type_sensor, ref) values (2, 'AccS3');
        
        insert into sensor(id_ref_sensor, number, validate) values (2, '0942H', True);
        insert into sensor(id_ref_sensor, number, validate) values (2, '0943H', True);
        
        insert into sensor_location(type, ref, serial_number, "order", location, time, validation) 
        values ('Accelerometer', 'AccS1', '0942H', 'order', 'in store', now(), True);
        
        insert into sensor_location(type, ref, serial_number, "order", location, time, validation) 
        values ('Accelerometer', 'AccS1', '0943H', 'order', 'in store', now(), True);
        
        insert into sensor_location(type, ref, serial_number, "order", location, time, validation) 
        values ('Accelerometer', 'AccS1', '0943H', 'order', 'in enum_config', now(), True);
        
        insert into sensor_location(type, ref, serial_number, "order", location, time, validation) 
        values ('Accelerometer', 'AccS1', '0943H', 'order', 'in enum_config', now(), True);
        
        insert into sensor_coating_config(id_position_on_tank, id_sensor, id_tank_configuration) 
        values (6, 3, 2);
        insert into sensor_coating_config(id_position_on_tank, id_sensor, id_tank_configuration) 
        values (7, 4, 2);
        
        insert into coating_location(id_coating, "order", location, date, validation) 
        values (1, 'order', 'in enum_config', now(), True);
        insert into coating_location(id_coating, "order", location, date, validation) 
        values (3, 'order', 'in enum_config', now(), True);
        """

    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    print("test3 initial")
except TypeError:
    print("test 3 initial fail")
