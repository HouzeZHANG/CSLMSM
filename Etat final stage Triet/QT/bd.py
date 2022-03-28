import psycopg2

drop_table = []
create_table = []

drop_user_table = """DROP TABLE IF EXISTS account;"""
user_table = """CREATE TABLE account (
                    id serial PRIMARY KEY,
                    uname varchar(50) UNIQUE,
                    orga varchar(50),
                    fname varchar(50),
                    lname varchar(50),
                    tel varchar(10),
                    email varchar(50),
                    password varchar
);"""

drop_table.append(drop_user_table)
create_table.append(user_table)

drop_test_mean_table = """DROP TABLE IF EXISTS test_mean;"""
test_mean_table = """CREATE TABLE test_mean (
                               id serial PRIMARY KEY,
                               type varchar,
                               name varchar,
                               number int 
);"""

drop_table.append(drop_test_mean_table)
create_table.append(test_mean_table)

drop_type_coating_table = """DROP TABLE IF EXISTS type_coating;"""
type_coating_table = """CREATE TABLE type_coating (
                               id serial PRIMARY KEY,
                               ref varchar UNIQUE
);"""

drop_table.append(drop_type_coating_table)
create_table.append(type_coating_table)

drop_type_detergent_table = """DROP TABLE IF EXISTS type_detergent;"""
type_detergent_table = """CREATE TABLE type_detergent (
                               id serial PRIMARY KEY,
                               ref varchar UNIQUE
);"""

drop_table.append(drop_type_detergent_table)
create_table.append(type_detergent_table)

drop_type_tank_table = """DROP TABLE IF EXISTS type_tank;"""
type_tank_table = """CREATE TABLE type_tank (
                               id serial PRIMARY KEY,
                               ref varchar UNIQUE
);"""

drop_table.append(drop_type_tank_table)
create_table.append(type_tank_table)

drop_type_sensor_table = """DROP TABLE IF EXISTS type_sensor;"""
type_sensor_table = """CREATE TABLE type_sensor (
                               id serial PRIMARY KEY,
                               ref varchar UNIQUE
);"""

drop_table.append(drop_type_sensor_table)
create_table.append(type_sensor_table)

drop_type_ejector_table = """DROP TABLE IF EXISTS type_ejector;"""
type_ejector_table = """CREATE TABLE type_ejector (
                               id serial PRIMARY KEY,
                               ref varchar UNIQUE
);"""

drop_table.append(drop_type_ejector_table)
create_table.append(type_ejector_table)

drop_type_camera_table = """DROP TABLE IF EXISTS type_camera;"""
type_camera_table = """CREATE TABLE type_camera (
                               id serial PRIMARY KEY,
                               ref varchar UNIQUE
);"""

drop_table.append(drop_type_camera_table)
create_table.append(type_camera_table)

drop_type_test_point_table = """DROP TABLE IF EXISTS type_test_point;"""
type_test_point_table = """CREATE TABLE type_test_point (
                               id serial PRIMARY KEY,
                               ref varchar

);"""

drop_table.append(drop_type_test_point_table)
create_table.append(type_test_point_table)

drop_type_intrinsic_value_table = """DROP TABLE IF EXISTS type_intrinsic_value;"""
type_intrinsic_value_table = """CREATE TABLE type_intrinsic_value (
                               id serial PRIMARY KEY,
                               ref varchar
);"""

drop_table.append(drop_type_intrinsic_value_table)
create_table.append(type_intrinsic_value_table)

drop_user_right_table = """DROP TABLE IF EXISTS user_right;"""
user_right_table = """CREATE TABLE user_right (
                               id serial PRIMARY KEY,
                               id_account int REFERENCES account(id) ON DELETE CASCADE,
                               role varchar,
                               id_test_mean int REFERENCES test_mean(id),
                               id_type_coating int REFERENCES type_coating(id),
                               id_type_detergent int REFERENCES type_detergent(id),
                               id_type_tank int REFERENCES type_tank(id),
                               id_type_sensor int REFERENCES type_sensor(id),
                               id_type_ejector int REFERENCES type_ejector(id),
                               id_type_camera int REFERENCES type_camera(id),
                               id_type_test_point int REFERENCES type_test_point(id),
                               id_type_intrinsic_value int REFERENCES type_intrinsic_value(id),
                               insect boolean,
                               acqui_system boolean
);"""
drop_table.append(drop_user_right_table)
create_table.append(user_right_table)

drop_attribute_table = """DROP TABLE IF EXISTS attribute;"""
attribute_table = """CREATE TABLE attribute(
                            id serial PRIMARY KEY,
                            attribute varchar,
                            unity varchar,
                            value float
);"""
drop_table.append(drop_attribute_table)
create_table.append(attribute_table)

drop_attribute_test_mean_table = """DROP TABLE IF EXISTS attribute_test_mean;"""
attribute_test_mean_table = """CREATE TABLE attribute_test_mean(
                            id serial PRIMARY KEY,
                            id_test_mean int REFERENCES test_mean(id),
                            id_attribute int REFERENCES attribute(id),
                            validate boolean
);"""

drop_table.append(drop_attribute_test_mean_table)
create_table.append(attribute_test_mean_table)

drop_type_param_table = """DROP TABLE IF EXISTS type_param;"""
type_param_table = """CREATE TABLE type_param(
                        id serial PRIMARY KEY,
                        name varchar,
                        unity varchar
);"""
drop_table.append(drop_type_param_table)
create_table.append(type_param_table)

drop_type_pram_test_mean_table = """DROP TABLE IF EXISTS type_param_test_mean;"""
type_param_test_mean = """CREATE TABLE type_param_test_mean(
                        id serial PRIMARY KEY,
                        id_test_mean int REFERENCES test_mean(id),
                        id_type_param int REFERENCES type_param(id), 
                        validate boolean
);"""
drop_table.append(drop_type_pram_test_mean_table)
create_table.append(type_param_test_mean)

drop_table_tank = """DROP TABLE IF EXISTS tank;"""
tank = """CREATE TABLE tank (
            id serial PRIMARY KEY,
            id_type_tank int REFERENCES type_tank(id),
            number int, 
            validate boolean
);"""
drop_table.append(drop_table_tank)
create_table.append(tank)

drop_position_on_tank_table = """DROP TABLE IF EXISTS position_on_tank;"""
position_on_tank = """CREATE TABLE position_on_tank(
            id serial PRIMARY KEY,
            id_tank int REFERENCES tank(id),
            num_loc varchar,
            ref varchar,
            coord int[3],
            metric int[3][3], 
            validate boolean
);"""

drop_table.append(drop_position_on_tank_table)
create_table.append(position_on_tank)

drop_coating_table = """DROP TABLE IF EXISTS coating;"""
coating = """CREATE TABLE coating(
            id serial PRIMARY KEY,
            id_type_coating int REFERENCES type_coating(id),
            number int,
            validate boolean
);"""
drop_table.append(drop_coating_table)
create_table.append(coating)

drop_attribute_coating_table = """DROP TABLE IF EXISTS attribute_coating;"""
attribute_coating = """CREATE TABLE attribute_coating(
            id serial PRIMARY KEY,
            id_coating int REFERENCES coating(id),
            id_attribute int REFERENCES attribute(id),
            validate boolean
);"""
drop_table.append(drop_attribute_coating_table)
create_table.append(attribute_coating)

drop_detergent_table = """DROP TABLE IF EXISTS detergent;"""
detergent = """CREATE TABLE detergent(
            id serial PRIMARY KEY,
            id_type_detergent int REFERENCES type_detergent(id),
            number int,
            validate boolean
);"""
drop_table.append(drop_detergent_table)
create_table.append(detergent)

drop_attribute_detergent_table = """DROP TABLE IF EXISTS attribute_detergent;"""
attribute_detergent = """CREATE TABLE attribute_detergent(
            id serial PRIMARY KEY,
            id_detergent int REFERENCES detergent(id),
            id_attribute int REFERENCES attribute(id),
            validate boolean
);"""
drop_table.append(drop_attribute_detergent_table)
create_table.append(attribute_detergent)

try :
    host = 'localhost'
    bd = 'lmsm'
    username = 'iventre'
    password = 'lmsm'
    conn = psycopg2.connect(host = host, dbname = bd, user = username, password = password)
    print('connect success')
    cur = conn.cursor()
    drop_table.reverse()
    for j, i in enumerate(drop_table) :
        cur.execute(i)
        conn.commit()
        print(f'done delete table {j}')
    for i, j in enumerate(create_table) :
        cur.execute(j)
        conn.commit()
        print('done table {}'.format(i))
    sql = """INSERT INTO account(orga, uname, fname, lname, tel, email, password) VALUES ('lmsm', 'nguyvan', 'Van Triet', 'Nguyen', '0698593783', 'vantriet.nguyen93@gmail.com', crypt('Nvt120698', gen_salt('bf', 8)));"""
    cur.execute(sql)
    conn.commit()
    sql = """INSERT INTO user_right(id_account, role) VALUES (1, 'manager');"""
    cur.execute(sql)
    conn.commit()
except :
    print('connect fail')