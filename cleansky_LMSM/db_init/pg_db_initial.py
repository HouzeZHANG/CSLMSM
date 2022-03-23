"""
Annotation 17/03/2022:
The CleanSky project database initialization file has been modified according to the file:
<<Liste IHM annotes precisant table, requete, fonction et sa description>>

Database : PostgreSQL
Version : PostgreSQL 14.2, compiled by Visual C++ build 1914, 64-bit
"""

import psycopg2

drop_table = []
create_table = []

drop_user_table = """DROP TABLE IF EXISTS account;"""
user_table = """CREATE TABLE account (
                    id serial PRIMARY KEY,
                    uname varchar(20) UNIQUE,
                    orga varchar(20),
                    fname varchar(20),
                    lname varchar(20),
                    tel varchar(20),
                    email varchar(255),
                    password varchar
);"""

drop_table.append(drop_user_table)
create_table.append(user_table)

drop_test_mean_table = """DROP TABLE IF EXISTS test_mean;"""
test_mean_table = """CREATE TABLE test_mean (
                               id serial PRIMARY KEY,
                               type varchar(20),
                               name varchar(20),
                               number varchar(20) 
);"""

drop_table.append(drop_test_mean_table)
create_table.append(test_mean_table)

drop_type_coating_table = """DROP TABLE IF EXISTS type_coating;"""
type_coating_table = """CREATE TABLE type_coating (
                               id serial PRIMARY KEY,
                               ref varchar(20) UNIQUE
);"""

drop_table.append(drop_type_coating_table)
create_table.append(type_coating_table)

# The table that needs to be added which are mentioned in the requirements documentation
"""
create teams for A/C Fight team 
or Wind Tunnel team
"""
drop_test_team_table = """DROP TABLE IF EXISTS test_team;"""
test_team = """CREATE TABLE test_team (
                    id serial PRIMARY KEY,
                    ref varchar(20) UNIQUE
);"""
drop_table.append(drop_test_team_table)
create_table.append(test_team)

drop_type_detergent_table = """DROP TABLE IF EXISTS type_detergent;"""
type_detergent_table = """CREATE TABLE type_detergent (
                               id serial PRIMARY KEY,
                               ref varchar(20) UNIQUE
);"""

drop_table.append(drop_type_detergent_table)
create_table.append(type_detergent_table)

drop_type_tank_table = """DROP TABLE IF EXISTS type_tank;"""
type_tank_table = """CREATE TABLE type_tank (
                               id serial PRIMARY KEY,
                               ref varchar(20) UNIQUE
);"""

drop_table.append(drop_type_tank_table)
create_table.append(type_tank_table)

drop_type_sensor_table = """DROP TABLE IF EXISTS type_sensor;"""
type_sensor_table = """CREATE TABLE type_sensor (
                               id serial PRIMARY KEY,
                               ref varchar(20) UNIQUE
);"""
drop_table.append(drop_type_sensor_table)
create_table.append(type_sensor_table)

drop_type_ejector_table = """DROP TABLE IF EXISTS type_ejector;"""
type_ejector_table = """CREATE TABLE type_ejector (
                               id serial PRIMARY KEY,
                               ref varchar(20) UNIQUE
);"""

drop_table.append(drop_type_ejector_table)
create_table.append(type_ejector_table)

drop_type_camera_table = """DROP TABLE IF EXISTS type_camera;"""
type_camera_table = """CREATE TABLE type_camera (
                               id serial PRIMARY KEY,
                               ref varchar(20) UNIQUE
);"""

drop_table.append(drop_type_camera_table)
create_table.append(type_camera_table)

drop_type_test_point_table = """DROP TABLE IF EXISTS type_test_point;"""
type_test_point_table = """CREATE TABLE type_test_point (
                               id serial PRIMARY KEY,
                               ref varchar(20) UNIQUE,
                               create_by varchar(20),
                               state varchar(20)
);"""

drop_table.append(drop_type_test_point_table)
create_table.append(type_test_point_table)

drop_type_intrinsic_value_table = """DROP TABLE IF EXISTS type_intrinsic_value;"""
type_intrinsic_value_table = """CREATE TABLE type_intrinsic_value (
                               id serial PRIMARY KEY,
                               ref varchar(20) UNIQUE, 
                               create_by varchar(20),
                               state varchar(20)
);"""

drop_table.append(drop_type_intrinsic_value_table)
create_table.append(type_intrinsic_value_table)

"""
更正
需要添加一个字段以记录test_team
----
type_role
id
role varchar(20)

user_right
id_type
5
"""

drop_type_role_table = """DROP TABLE IF EXISTS type_role;"""
type_role_table = """CREATE TABLE type_role(
                               id serial PRIMARY KEY,
                               ref varchar(20) UNIQUE
);"""

drop_table.append(drop_type_role_table)
create_table.append(type_role_table)


drop_user_right_table = """DROP TABLE IF EXISTS user_right;"""
user_right_table = """CREATE TABLE user_right (
                               id serial PRIMARY KEY,
                               id_account int REFERENCES account(id) ON DELETE CASCADE,
                               role int REFERENCES type_role(id),
                               id_test_mean int REFERENCES test_mean(id),
                               id_type_coating int REFERENCES type_coating(id),
                               id_type_detergent int REFERENCES type_detergent(id),
                               id_type_tank int REFERENCES type_tank(id),
                               id_type_sensor int REFERENCES type_sensor(id),
                               id_type_ejector int REFERENCES type_ejector(id),
                               id_type_camera int REFERENCES type_camera(id),
                               id_type_test_point int REFERENCES type_test_point(id),
                               id_type_intrinsic_value int REFERENCES type_intrinsic_value(id),
                               id_test_team int REFERENCES test_team(id),
                               insect boolean,
                               acqui_system boolean
);"""

drop_table.append(drop_user_right_table)
create_table.append(user_right_table)

"""
22/03/2022添加
type_unity
id pk
ref unique

table attribute unity_id
table type_param unity_id
"""

drop_type_unity_table = """DROP TABLE IF EXISTS type_unity;"""
type_unity = """CREATE TABLE type_unity(
                            id serial PRIMARY KEY,
                            ref varchar(20) UNIQUE
);"""

drop_table.append(drop_type_unity_table)
create_table.append(type_unity)


drop_attribute_table = """DROP TABLE IF EXISTS attribute;"""
attribute_table = """CREATE TABLE attribute(
                            id serial PRIMARY KEY,
                            attribute varchar(20),
                            id_unity int REFERENCES type_unity(id),
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
                        name varchar(20),
                        id_unity int REFERENCES type_unity(id),
                        axes int[3]
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
            number varchar(20), 
            validate boolean
);"""

drop_table.append(drop_table_tank)
create_table.append(tank)

drop_position_on_tank_table = """DROP TABLE IF EXISTS position_on_tank;"""
position_on_tank = """CREATE TABLE position_on_tank(
            id serial PRIMARY KEY,
            id_tank int REFERENCES tank(id),
            num_loc varchar(20),
            ref varchar(20),
            coord float[3],
            metric float[3][3],
            type varchar(20)
);"""

drop_table.append(drop_position_on_tank_table)
create_table.append(position_on_tank)

drop_coating_table = """DROP TABLE IF EXISTS coating;"""
coating = """CREATE TABLE coating(
            id serial PRIMARY KEY,
            id_type_coating int REFERENCES type_coating(id),
            number varchar(20),
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
            number varchar(20),
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

"""
type and number
"""
drop_sensor_table = """DROP TABLE IF EXISTS sensor;"""
sensor = """CREATE TABLE sensor(
                id serial PRIMARY KEY,
                id_type_sensor int REFERENCES type_sensor(id),
                type varchar(20),
                number varchar(20),
                validate boolean,
                calibration boolean
);"""

drop_table.append(drop_sensor_table)
create_table.append(sensor)

drop_calibration_table = """DROP TABLE IF EXISTS calibration;"""
calibration = """CREATE TABLE calibration(
                id serial PRIMARY KEY,
                id_sensor int REFERENCES sensor(id),
                id_type_param int REFERENCES type_param(id),
                value_mesure float,
                value_true float
);"""

drop_table.append(drop_calibration_table)
create_table.append(calibration)

drop_type_param_sensor_table = """DROP TABLE IF EXISTS type_param_sensor;"""
type_param_sensor = """CREATE TABLE type_param_sensor(
                id serial PRIMARY KEY,
                id_type_sensor int REFERENCES type_sensor(id),
                id_type_param int REFERENCES type_param(id),
                validate boolean
);"""

drop_table.append(drop_type_param_sensor_table)
create_table.append(type_param_sensor)

drop_tank_configuration_table = """DROP TABLE IF EXISTS tank_configuration;"""
tank_configuration = """CREATE TABLE tank_configuration (
                 id serial PRIMARY KEY,
                 ref varchar(20) UNIQUE,
                 date date,
                 validate boolean,
                 tank_type int REFERENCES  tank(id)
);"""

drop_table.append(drop_tank_configuration_table)
create_table.append(tank_configuration)

drop_sensor_coating_config_table = """DROP TABLE IF EXISTS sensor_coating_config;"""
sensor_coating_config = """CREATE TABLE sensor_coating_config (
                 id serial PRIMARY KEY,
                 id_position_on_tank int REFERENCES position_on_tank(id),
                 id_sensor int REFERENCES sensor(id),
                 id_coating int REFERENCES coating(id),
                 id_tank_configuration int REFERENCES tank_configuration(id)
);"""

drop_table.append(drop_sensor_coating_config_table)
create_table.append(sensor_coating_config)

drop_hardware_table = """DROP TABLE IF EXISTS hardware;"""
hardware = """CREATE TABLE hardware(
                id serial PRIMARY KEY,
                ref varchar(20),
                number varchar(20)
);"""

drop_table.append(drop_hardware_table)
create_table.append(hardware)

drop_software_table = """DROP TABLE IF EXISTS software;"""
software = """CREATE TABLE software(
                id serial PRIMARY KEY,
                ref varchar(20),
                release varchar(20)
);"""

drop_table.append(drop_software_table)
create_table.append(software)

drop_hardware_software_table = """DROP TABLE IF EXISTS hardware_software;"""
hardware_software = """CREATE TABLE hardware_software(
                id serial PRIMARY KEY,
                id_hardware int REFERENCES hardware(id),
                id_software int REFERENCES software(id)
);"""

drop_table.append(drop_hardware_software_table)
create_table.append(hardware_software)

drop_software_value_table = """DROP TABLE IF EXISTS software_value;"""
software_value = """CREATE TABLE software_value(
                id serial PRIMARY KEY,
                ref varchar(20),
                release varchar(20)
);"""

drop_table.append(drop_software_value_table)
create_table.append(software_value)

drop_software_value_software_table = """DROP TABLE IF EXISTS software_value_software;"""
software_value_software = """CREATE TABLE software_value_software(
                id serial PRIMARY KEY,
                id_software int REFERENCES software(id),
                id_software_value int REFERENCES software_value(id)
);"""

drop_table.append(drop_software_value_software_table)
create_table.append(software_value_software)

drop_acquisition_config_table = """DROP TABLE IF EXISTS acquisition_config;"""
acquisition_config = """CREATE TABLE acquisition_config (
                id serial PRIMARY KEY,
                ref varchar(20) UNIQUE,
                date date, 
                validate boolean
);"""

drop_table.append(drop_acquisition_config_table)
create_table.append(acquisition_config)

drop_config_on_acqui_table = """DROP TABLE IF EXISTS config_on_acqui;"""
config_on_acqui = """CREATE TABLE config_on_acqui (
                id serial PRIMARY KEY,
                id_hardware int REFERENCES hardware(id),
                id_software int REFERENCES software(id),
                id_software_value int REFERENCES software_value(id),
                id_acquisition_config int REFERENCES acquisition_config(id)
);"""

drop_table.append(drop_config_on_acqui_table)
create_table.append(config_on_acqui)

drop_camera_table = """DROP TABLE IF EXISTS camera;"""
camera = """CREATE TABLE camera (
                id serial PRIMARY KEY,
                id_type_camera int REFERENCES type_camera(id),
                number varchar(20),
                s_min float,
                s_max float,
                axe float,
                h_aperture float,
                w_aperture float
);"""

drop_table.append(drop_camera_table)
create_table.append(camera)

drop_config_camera_table = """DROP TABLE IF EXISTS config_camera;"""
config_camera = """CREATE TABLE config_camera(
                  id serial PRIMARY KEY,
                  ref varchar(20) UNIQUE,
                  type_camera int REFERENCES camera(id),
                  date date,
                  validate boolean
);"""

drop_table.append(drop_config_camera_table)
create_table.append(config_camera)

drop_camera_in_config_table = """DROP TABLE IF EXISTS camera_in_config;"""
camera_in_config = """CREATE TABLE camera_in_config(
                    id serial PRIMARY KEY,
                    id_config_camera int REFERENCES config_camera(id),
                    id_test_mean int REFERENCES test_mean(id),
                    d float,
                    h_axe float,
                    v_axe float,
                    s float,
                    lens float
);"""

drop_table.append(drop_camera_in_config_table)
create_table.append(camera_in_config)

drop_ejector_table = """DROP TABLE IF EXISTS ejector;"""
ejector = """CREATE TABLE ejector(
                id serial PRIMARY KEY,
                id_type_ejector int REFERENCES type_ejector(id),
                number varchar(20),
                v_min float,
                v_max float,
                e_axe varchar(20),
                ins_vol float,
                nb_type int 
);"""

drop_table.append(drop_ejector_table)
create_table.append(ejector)

drop_ejector_config_table = """DROP TABLE IF EXISTS ejector_config;"""
ejector_config = """CREATE TABLE ejector_config(
                 id serial PRIMARY KEY,
                 ref varchar(20) UNIQUE,
                 type_ejector int REFERENCES ejector(id),
                 date date,
                 validation boolean
);"""

drop_table.append(drop_ejector_config_table)
create_table.append(ejector_config)

drop_ejector_in_config_table = """DROP TABLE IF EXISTS ejector_in_config;"""
ejector_in_config = """CREATE TABLE ejector_in_config(
                 id serial PRIMARY KEY,
                 id_ejector_config int REFERENCES ejector_config(id),
                 d float,
                 h_axe float,
                 v_axe float
);"""

drop_table.append(drop_ejector_in_config_table)
create_table.append(ejector_in_config)

drop_airfield_table = """DROP TABLE IF EXISTS airfield;"""
airfield = """CREATE TABLE airfield (
                 id serial PRIMARY KEY,
                 name varchar(20),
                 runway varchar(20),
                 alt float
);"""

drop_table.append(drop_airfield_table)
create_table.append(airfield)

drop_cond_init_table = """DROP TABLE IF EXISTS cond_init;"""
cond_init = """CREATE TABLE cond_init (
                 id serial PRIMARY KEY,
                 cond_init JSON,
                 id_airfield int REFERENCES airfield(id)
);"""

drop_table.append(drop_cond_init_table)
create_table.append(cond_init)

drop_insect_table = """DROP TABLE IF EXISTS insect;"""
insect = """CREATE TABLE insect (
                 id serial PRIMARY KEY,
                 name varchar(20),
                 masse float,
                 alt_min float,
                 alt_max float,
                 length float,
                 width float,
                 thickness float,
                 hemolymphe varchar(20),
                 validate boolean
);"""

drop_table.append(drop_insect_table)
create_table.append(insect)

drop_insect_in_cond_init_table = """DROP TABLE IF EXISTS insect_in_cond_init;"""
insect_in_cond_init = """CREATE TABLE insect_in_cond_init (
                 id serial PRIMARY KEY,
                 id_cond_init int REFERENCES cond_init(id),
                 id_insect int REFERENCES insect(id),
                 validate boolean
);"""

drop_table.append(drop_insect_in_cond_init_table)
create_table.append(insect_in_cond_init)

drop_quantite_table = """DROP TABLE IF EXISTS quantite;"""
quantite = """CREATE TABLE quantite (
                 id serial PRIMARY KEY,
                 id_ejector_in_config int REFERENCES ejector_in_config(id),
                 id_cond_init int REFERENCES cond_init(id),
                 id_insect int REFERENCES insect(id),
                 qnt float,
                 validate boolean
);"""

drop_table.append(drop_quantite_table)
create_table.append(quantite)

drop_velocity_speed_table = """DROP TABLE IF EXISTS velocity_speed;"""
velocity_speed = """CREATE TABLE velocity_speed (
                 id serial PRIMARY KEY,
                 id_ejector_in_config int REFERENCES ejector_in_config(id),
                 id_cond_init int REFERENCES cond_init(id),
                 speed float, 
                 validate boolean
);"""

drop_table.append(drop_velocity_speed_table)
create_table.append(velocity_speed)

drop_pilot_table = """DROP TABLE IF EXISTS pilot;"""
pilot = """CREATE TABLE pilot (
                 id serial PRIMARY KEY,
                 pilot varchar(20)
);"""

drop_table.append(drop_pilot_table)
create_table.append(pilot)

drop_test_table = """DROP TABLE IF EXISTS test;"""
test = """CREATE TABLE test(
                 id serial PRIMARY KEY,
                 id_test_mean int REFERENCES test_mean(id),
                 type varchar(20),
                 number int,
                 index varchar(5),
                 date date,
                 time_begin time,
                 time_end time,
                 id_tank_conf int REFERENCES tank_configuration(id),
                 id_acqui_conf int REFERENCES acquisition_config(id),
                 id_camera_conf int REFERENCES config_camera(id),
                 id_ejector_conf int REFERENCES ejector_config(id),
                 id_cond_init int REFERENCES cond_init(id),
                 id_pilot int REFERENCES pilot(id),
                 validate boolean,
                 archievement float
);"""

drop_table.append(drop_test_table)
create_table.append(test)

"""
22/03/2022增加
----
type_document
id pk
type_doc unique
document remplace type de table document par type_document(id)
"""

drop_type_document_table = """DROP TABLE IF EXISTS type_document;"""
type_document = """CREATE TABLE type_document (
                 id serial PRIMARY KEY,
                 ref varchar(20) UNIQUE
);"""

drop_table.append(drop_type_document_table)
create_table.append(type_document)


drop_document_table = """DROP TABLE IF EXISTS document;"""
document = """CREATE TABLE document (
                 id serial PRIMARY KEY,
                 type int REFERENCES type_document(id),
                 ref varchar(20),
                 number varchar(20),
                 link varchar(255), 
                 validate boolean
);"""

drop_table.append(drop_document_table)
create_table.append(document)

drop_data_sensor_table = """DROP TABLE IF EXISTS data_sensor;"""
data_sensor = """CREATE TABLE data_sensor (
                    id serial PRIMARY KEY,
                    id_test int REFERENCES test(id),
                    id_sensor_coating_config int REFERENCES sensor_coating_config(id),
                    id_type_param int REFERENCES type_param(id),
                    time time,
                    value float,
                    validate boolean
);"""

drop_table.append(drop_data_sensor_table)
create_table.append(data_sensor)

drop_data_vol_table = """DROP TABLE IF EXISTS data_vol;"""
data_vol = """CREATE TABLE data_vol(
                    id serial PRIMARY KEY,
                    id_test int REFERENCES test(id),
                    id_type_param int REFERENCES type_param(id),
                    time time,
                    value float,
                    validate boolean
);"""

drop_table.append(drop_data_vol_table)
create_table.append(data_vol)

drop_photo_table = """DROP TABLE IF EXISTS photo;"""
photo = """CREATE TABLE photo(
                id serial PRIMARY KEY,
                id_test int REFERENCES test(id),
                name varchar(20),
                longitude float,
                latitude float,
                altitude_m float,
                altitude_feet float,
                GTM timestamp,
                duration float,
                distance float,
                incidence float,
                speed varchar(20),
                iso varchar(20),
                quantite varchar(20),
                poids float,
                validate boolean
);"""

drop_table.append(drop_photo_table)
create_table.append(photo)

drop_document_test_table = """DROP TABLE IF EXISTS document_test;"""
document_test = """CREATE TABLE document_test(
                 id serial PRIMARY KEY,
                 id_test int REFERENCES test(id),
                 id_document int REFERENCES document(id),
                 validate boolean
);"""

drop_table.append(drop_document_test_table)
create_table.append(document_test)

# drop_test_point_table = """DROP TABLE IF EXISTS test_point;"""
# test_point = """CREATE TABLE test_point (
#                     id serial PRIMARY KEY,
#                     id_type_test_point int REFERENCES type_test_point(id),
#                     create_by varchar(20),
#                     state varchar(20)
# );"""
# drop_table.append(drop_test_point_table)
# create_table.append(test_point)

drop_param_test_point_table = """DROP TABLE IF EXISTS param_test_point;"""
param_test_point = """CREATE TABLE param_test_point (
                    id serial PRIMARY KEY,
                    id_type_test_point int REFERENCES type_test_point(id),
                    id_type_param int REFERENCES type_param(id)
);"""

drop_table.append(drop_param_test_point_table)
create_table.append(param_test_point)

drop_test_point_table = """DROP TABLE IF EXISTS test_point;"""
test_point = """CREATE TABLE test_point (
                    id serial PRIMARY KEY,
                    id_type_test_point int REFERENCES type_test_point(id),
                    id_test int REFERENCES test(id),
                    time_begin time,
                    time_end time,
                    link varchar(255),
                    confident varchar(20),
                    remark varchar(255),
                    issue int,
                    validate boolean
);"""

drop_table.append(drop_test_point_table)
create_table.append(test_point)

drop_test_point_value_table = """DROP TABLE IF EXISTS test_point_value;"""
test_point_value = """CREATE TABLE test_point_value (
                    id serial PRIMARY KEY,
                    id_test_point int REFERENCES test_point(id),
                    id_type_param int REFERENCES type_param(id),
                    value float
);"""

drop_table.append(drop_test_point_value_table)
create_table.append(test_point_value)

drop_param_intrinsic_value_table = """DROP TABLE IF EXISTS param_intrinsic_value;"""
param_intrinsic_value = """CREATE TABLE param_intrinsic_value (
                    id serial PRIMARY KEY,
                    id_type_intrinsic_value int REFERENCES type_intrinsic_value(id),
                    id_type_param int REFERENCES type_param(id)
);"""

drop_table.append(drop_param_intrinsic_value_table)
create_table.append(param_intrinsic_value)

drop_intrinsic_value_table = """DROP TABLE IF EXISTS intrinsic_value;"""
intrinsic_value = """CREATE TABLE intrinsic_value (
                    id serial PRIMARY KEY,
                    id_type_intrinsic_value int REFERENCES type_intrinsic_value(id),
                    id_test int REFERENCES test(id),
                    time_begin time,
                    time_end time,
                    link varchar(255),
                    confident varchar(20),
                    remark varchar(255)
);"""

drop_table.append(drop_intrinsic_value_table)
create_table.append(intrinsic_value)

drop_intrinsic_value_value_table = """DROP TABLE IF EXISTS intrinsic_value_value;"""
intrinsic_value_value = """CREATE TABLE intrinsic_value_value (
                    id serial PRIMARY KEY,
                    id_intrinsic_value int REFERENCES intrinsic_value(id),
                    id_type_param int REFERENCES type_param(id),
                    value float
);"""

drop_table.append(drop_intrinsic_value_value_table)
create_table.append(intrinsic_value_value)




drop_sensor_location_table = """DROP TABLE IF EXISTS sensor_location;"""
sensor_location = """CREATE TABLE sensor_location (
                    id serial PRIMARY KEY,
                    id_sensor serial REFERENCES sensor(id),
                    "order" varchar(20),
                    location varchar(20),
                    date date,
                    validation boolean
);"""

drop_table.append(drop_sensor_location_table)
create_table.append(sensor_location)

drop_coating_location_table = """DROP TABLE IF EXISTS coating_location;"""
coating_location = """CREATE TABLE coating_location (
                    id serial PRIMARY KEY,
                    id_coating int REFERENCES coating(id),
                    "order" varchar(20) DEFAULT 'good',
                    location varchar(20),
                    date date,
                    validation boolean
);"""

drop_table.append(drop_coating_location_table)
create_table.append(coating_location)

drop_def_test_point_table = """DROP TABLE IF EXISTS def_test_point;"""
def_test_point = """CREATE TABLE def_test_point (
                    id serial PRIMARY KEY,
                    id_type_test_point int REFERENCES type_test_point(id),
                    coating boolean,
                    detergent boolean,
                    create_by varchar(20),
                    validation boolean
);"""

drop_table.append(drop_def_test_point_table)
create_table.append(def_test_point)

# type de role
# type de document
# type de unity

try:
    host = 'localhost'
    bd = 'testdb'
    username = 'dbuser'
    password = '123456'

    conn = psycopg2.connect(host=host, dbname=bd, user=username, password=password)
    # print('connect success')
    cur = conn.cursor()
    drop_table.reverse()
    for j, i in enumerate(drop_table):
        print(i, j)
        cur.execute(i)
        conn.commit()
        print(f'done delete table {j}')
    for i, j in enumerate(create_table):
        print(i, j)
        cur.execute(j)
        conn.commit()
        print('done table {}'.format(i))



    print("initialize successfully")
except:
    print('connect fail')
