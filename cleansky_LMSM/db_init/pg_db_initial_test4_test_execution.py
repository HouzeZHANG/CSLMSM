import cleansky_LMSM.db_init.pg_db_initial as pg_db_initial
import cleansky_LMSM.db_init.pg_db_initial_test3_lists_of_test_means

try:
    sql = """
        insert into account(uname, password) 
        VALUES ('Bob', '0000');
        insert into account(uname, password) 
        VALUES ('Jack', '0000');
        insert into account(uname, password) 
        VALUES ('Alice', '0000');
        insert into account(uname, password) 
        VALUES ('Steven', '0000');
        insert into account(uname, password) 
        VALUES ('Rose', '0000');
        
        insert into user_right(id_account, role, id_test_team) 
        values (7, 4, 1);
        insert into user_right(id_account, role, id_test_team) 
        values (8, 4, 1);
        insert into user_right(id_account, role, id_test_team) 
        values (9, 4, 1);
        insert into user_right(id_account, role, id_test_team) 
        values (10, 4, 2);
        insert into user_right(id_account, role, id_test_team) 
        values (7, 4, 2);
        insert into user_right(id_account, role, id_test_team) 
        values (8, 4, 2);
        
        insert into pilot(pilot) values ('Zara');
        insert into pilot(pilot) values ('Hermes');
        
        insert into tank(id_type_tank, number, validate) VALUES (1, 't1', True);
        insert into type_camera(ref) values ('came1');
        insert into camera(id_type_camera, number) values (1, '12');
        insert into tank_configuration(ref, validate, tank_type) values ('tank_config_1', True, 1);
        insert into tank_configuration(ref, validate, tank_type) values ('tank_config_2', True, 1);
        insert into acquisition_config(ref, validate) values ('acq_1', True);
        insert into acquisition_config(ref, validate) values ('acq_2', True);
        insert into config_camera(ref, type_camera, validate) values ('camera_config_1', 1, True);
        insert into config_camera(ref, type_camera, validate) values ('camera_config_2', 1, True);
        insert into airfield(name, runway, alt) values ('Aix', 'Ron', 1300);
        insert into airfield(name, runway, alt) values ('Paris', 'Louvre', 0);
        insert into airfield(name, runway, alt) values ('Shanghai', 'Bund', 10);
        insert into cond_init(cond_init, id_airfield)
        values ('["1_", "2_", "3_", "4_", "5_", "6_", "7_", "8_"]', 1);
        
        insert into test(id_test_mean, type, number, id_test_driver, date, time_begin, time_end, id_tank_conf, 
        id_acqui_conf, id_camera_conf, id_cond_init, id_pilot, id_copilot, validate, achievement) 
        VALUES (2, 'Flight', '158', 9, '2022-5-25', '08:00:00', '21:00:00', 1, 1, 1, 1, 1, 2, false, 0.75);
        
        insert into sensor_coating_config(id_sensor) 
        values (1);
        insert into data_sensor(id_test, id_sensor_coating_config, id_type_param, time, value, validate) 
        values (1, 1, 1, '14:21:12.1222', 100, True);
        insert into data_sensor(id_test, id_sensor_coating_config, id_type_param, time, value, validate) 
        values (1, 1, 1, now(), 120, True);
        
        insert into data_vol(id_test, id_type_param, time, value, validate) 
        values (1, 1, now(), 999, true);
        """

    pg_db_initial.cur.execute(sql)
    pg_db_initial.conn.commit()

    print("test3 initial")
except TypeError:
    print("test 3 initial fail")
