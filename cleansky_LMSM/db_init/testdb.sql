--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4
-- Dumped by pg_dump version 14.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.account (
    id integer NOT NULL,
    uname character varying(20),
    orga character varying(20),
    fname character varying(20),
    lname character varying(20),
    tel character varying(20),
    email character varying(255),
    password character varying
);


ALTER TABLE public.account OWNER TO postgres;

--
-- Name: account_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.account_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.account_id_seq OWNER TO postgres;

--
-- Name: account_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.account_id_seq OWNED BY public.account.id;


--
-- Name: acquisition_config; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.acquisition_config (
    id integer NOT NULL,
    ref character varying(20),
    date date,
    validate boolean
);


ALTER TABLE public.acquisition_config OWNER TO postgres;

--
-- Name: acquisition_config_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.acquisition_config_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.acquisition_config_id_seq OWNER TO postgres;

--
-- Name: acquisition_config_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.acquisition_config_id_seq OWNED BY public.acquisition_config.id;


--
-- Name: airfield; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.airfield (
    id integer NOT NULL,
    name character varying(20),
    runway character varying(20),
    alt double precision
);


ALTER TABLE public.airfield OWNER TO postgres;

--
-- Name: airfield_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.airfield_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.airfield_id_seq OWNER TO postgres;

--
-- Name: airfield_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.airfield_id_seq OWNED BY public.airfield.id;


--
-- Name: attribute; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attribute (
    id integer NOT NULL,
    attribute character varying(20),
    id_unity integer,
    value double precision
);


ALTER TABLE public.attribute OWNER TO postgres;

--
-- Name: attribute_coating; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attribute_coating (
    id integer NOT NULL,
    id_coating integer,
    id_attribute integer
);


ALTER TABLE public.attribute_coating OWNER TO postgres;

--
-- Name: attribute_coating_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.attribute_coating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.attribute_coating_id_seq OWNER TO postgres;

--
-- Name: attribute_coating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.attribute_coating_id_seq OWNED BY public.attribute_coating.id;


--
-- Name: attribute_detergent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attribute_detergent (
    id integer NOT NULL,
    id_detergent integer,
    id_attribute integer
);


ALTER TABLE public.attribute_detergent OWNER TO postgres;

--
-- Name: attribute_detergent_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.attribute_detergent_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.attribute_detergent_id_seq OWNER TO postgres;

--
-- Name: attribute_detergent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.attribute_detergent_id_seq OWNED BY public.attribute_detergent.id;


--
-- Name: attribute_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.attribute_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.attribute_id_seq OWNER TO postgres;

--
-- Name: attribute_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.attribute_id_seq OWNED BY public.attribute.id;


--
-- Name: attribute_test_mean; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.attribute_test_mean (
    id integer NOT NULL,
    id_test_mean integer,
    id_attribute integer
);


ALTER TABLE public.attribute_test_mean OWNER TO postgres;

--
-- Name: attribute_test_mean_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.attribute_test_mean_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.attribute_test_mean_id_seq OWNER TO postgres;

--
-- Name: attribute_test_mean_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.attribute_test_mean_id_seq OWNED BY public.attribute_test_mean.id;


--
-- Name: calibration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.calibration (
    id integer NOT NULL,
    id_sensor integer,
    id_type_param integer,
    id_type_versus integer,
    value_mesure double precision,
    value_true double precision,
    value_versus double precision
);


ALTER TABLE public.calibration OWNER TO postgres;

--
-- Name: calibration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.calibration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.calibration_id_seq OWNER TO postgres;

--
-- Name: calibration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.calibration_id_seq OWNED BY public.calibration.id;


--
-- Name: camera; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.camera (
    id integer NOT NULL,
    id_type_camera integer,
    number character varying(20),
    s_min double precision,
    s_max double precision,
    axe double precision,
    h_aperture double precision,
    w_aperture double precision
);


ALTER TABLE public.camera OWNER TO postgres;

--
-- Name: camera_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.camera_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.camera_id_seq OWNER TO postgres;

--
-- Name: camera_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.camera_id_seq OWNED BY public.camera.id;


--
-- Name: camera_in_config; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.camera_in_config (
    id integer NOT NULL,
    id_config_camera integer,
    id_test_mean integer,
    d double precision,
    h_axe double precision,
    v_axe double precision,
    s double precision,
    lens double precision
);


ALTER TABLE public.camera_in_config OWNER TO postgres;

--
-- Name: camera_in_config_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.camera_in_config_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.camera_in_config_id_seq OWNER TO postgres;

--
-- Name: camera_in_config_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.camera_in_config_id_seq OWNED BY public.camera_in_config.id;


--
-- Name: coating; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.coating (
    id integer NOT NULL,
    id_type_coating integer,
    number character varying(20),
    validate boolean
);


ALTER TABLE public.coating OWNER TO postgres;

--
-- Name: coating_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.coating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.coating_id_seq OWNER TO postgres;

--
-- Name: coating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.coating_id_seq OWNED BY public.coating.id;


--
-- Name: coating_location; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.coating_location (
    id integer NOT NULL,
    id_coating integer,
    "order" character varying(20) DEFAULT 'good'::character varying,
    location character varying(20),
    date date,
    validation boolean
);


ALTER TABLE public.coating_location OWNER TO postgres;

--
-- Name: coating_location_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.coating_location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.coating_location_id_seq OWNER TO postgres;

--
-- Name: coating_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.coating_location_id_seq OWNED BY public.coating_location.id;


--
-- Name: cond_init; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cond_init (
    id integer NOT NULL,
    cond_init json,
    id_airfield integer
);


ALTER TABLE public.cond_init OWNER TO postgres;

--
-- Name: cond_init_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cond_init_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cond_init_id_seq OWNER TO postgres;

--
-- Name: cond_init_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cond_init_id_seq OWNED BY public.cond_init.id;


--
-- Name: config_camera; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.config_camera (
    id integer NOT NULL,
    ref character varying(20),
    type_camera integer,
    date date,
    validate boolean
);


ALTER TABLE public.config_camera OWNER TO postgres;

--
-- Name: config_camera_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.config_camera_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.config_camera_id_seq OWNER TO postgres;

--
-- Name: config_camera_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.config_camera_id_seq OWNED BY public.config_camera.id;


--
-- Name: config_on_acqui; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.config_on_acqui (
    id integer NOT NULL,
    id_hardware integer,
    id_software integer,
    id_software_value integer,
    id_acquisition_config integer
);


ALTER TABLE public.config_on_acqui OWNER TO postgres;

--
-- Name: config_on_acqui_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.config_on_acqui_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.config_on_acqui_id_seq OWNER TO postgres;

--
-- Name: config_on_acqui_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.config_on_acqui_id_seq OWNED BY public.config_on_acqui.id;


--
-- Name: data_sensor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data_sensor (
    id integer NOT NULL,
    id_test integer,
    id_sensor_coating_config integer,
    id_type_param integer,
    "time" time without time zone,
    value double precision,
    validate boolean
);


ALTER TABLE public.data_sensor OWNER TO postgres;

--
-- Name: data_sensor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.data_sensor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_sensor_id_seq OWNER TO postgres;

--
-- Name: data_sensor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.data_sensor_id_seq OWNED BY public.data_sensor.id;


--
-- Name: data_vol; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.data_vol (
    id integer NOT NULL,
    id_test integer,
    id_type_param integer,
    "time" time without time zone,
    value double precision,
    validate boolean
);


ALTER TABLE public.data_vol OWNER TO postgres;

--
-- Name: data_vol_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.data_vol_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_vol_id_seq OWNER TO postgres;

--
-- Name: data_vol_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.data_vol_id_seq OWNED BY public.data_vol.id;


--
-- Name: def_test_point; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.def_test_point (
    id integer NOT NULL,
    id_type_test_point integer,
    coating boolean,
    detergent boolean,
    create_by character varying(20),
    validation boolean
);


ALTER TABLE public.def_test_point OWNER TO postgres;

--
-- Name: def_test_point_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.def_test_point_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.def_test_point_id_seq OWNER TO postgres;

--
-- Name: def_test_point_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.def_test_point_id_seq OWNED BY public.def_test_point.id;


--
-- Name: detergent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.detergent (
    id integer NOT NULL,
    id_type_detergent integer,
    number character varying(20),
    validate boolean
);


ALTER TABLE public.detergent OWNER TO postgres;

--
-- Name: detergent_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.detergent_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.detergent_id_seq OWNER TO postgres;

--
-- Name: detergent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.detergent_id_seq OWNED BY public.detergent.id;


--
-- Name: document; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.document (
    id integer NOT NULL,
    type integer,
    ref character varying(20),
    number character varying(20),
    link character varying(255),
    validate boolean
);


ALTER TABLE public.document OWNER TO postgres;

--
-- Name: document_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.document_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.document_id_seq OWNER TO postgres;

--
-- Name: document_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.document_id_seq OWNED BY public.document.id;


--
-- Name: document_test; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.document_test (
    id integer NOT NULL,
    id_test integer,
    id_document integer,
    validate boolean
);


ALTER TABLE public.document_test OWNER TO postgres;

--
-- Name: document_test_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.document_test_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.document_test_id_seq OWNER TO postgres;

--
-- Name: document_test_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.document_test_id_seq OWNED BY public.document_test.id;


--
-- Name: ejector; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ejector (
    id integer NOT NULL,
    id_type_ejector integer,
    number character varying(20),
    v_min double precision,
    v_max double precision,
    e_axe character varying(20),
    ins_vol double precision,
    nb_type integer
);


ALTER TABLE public.ejector OWNER TO postgres;

--
-- Name: ejector_config; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ejector_config (
    id integer NOT NULL,
    ref character varying(20),
    type_ejector integer,
    date date,
    validation boolean
);


ALTER TABLE public.ejector_config OWNER TO postgres;

--
-- Name: ejector_config_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ejector_config_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ejector_config_id_seq OWNER TO postgres;

--
-- Name: ejector_config_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ejector_config_id_seq OWNED BY public.ejector_config.id;


--
-- Name: ejector_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ejector_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ejector_id_seq OWNER TO postgres;

--
-- Name: ejector_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ejector_id_seq OWNED BY public.ejector.id;


--
-- Name: ejector_in_config; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ejector_in_config (
    id integer NOT NULL,
    id_ejector_config integer,
    d double precision,
    h_axe double precision,
    v_axe double precision
);


ALTER TABLE public.ejector_in_config OWNER TO postgres;

--
-- Name: ejector_in_config_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ejector_in_config_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ejector_in_config_id_seq OWNER TO postgres;

--
-- Name: ejector_in_config_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ejector_in_config_id_seq OWNED BY public.ejector_in_config.id;


--
-- Name: hardware; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hardware (
    id integer NOT NULL,
    ref character varying(20),
    number character varying(20)
);


ALTER TABLE public.hardware OWNER TO postgres;

--
-- Name: hardware_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.hardware_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hardware_id_seq OWNER TO postgres;

--
-- Name: hardware_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.hardware_id_seq OWNED BY public.hardware.id;


--
-- Name: hardware_software; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hardware_software (
    id integer NOT NULL,
    id_hardware integer,
    id_software integer
);


ALTER TABLE public.hardware_software OWNER TO postgres;

--
-- Name: hardware_software_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.hardware_software_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hardware_software_id_seq OWNER TO postgres;

--
-- Name: hardware_software_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.hardware_software_id_seq OWNED BY public.hardware_software.id;


--
-- Name: insect; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.insect (
    id integer NOT NULL,
    name character varying(20),
    masse double precision,
    alt_min double precision,
    alt_max double precision,
    length double precision,
    width double precision,
    thickness double precision,
    hemolymphe character varying(20)
);


ALTER TABLE public.insect OWNER TO postgres;

--
-- Name: insect_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.insect_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.insect_id_seq OWNER TO postgres;

--
-- Name: insect_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.insect_id_seq OWNED BY public.insect.id;


--
-- Name: insect_in_cond_init; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.insect_in_cond_init (
    id integer NOT NULL,
    id_cond_init integer,
    id_insect integer,
    validate boolean
);


ALTER TABLE public.insect_in_cond_init OWNER TO postgres;

--
-- Name: insect_in_cond_init_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.insect_in_cond_init_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.insect_in_cond_init_id_seq OWNER TO postgres;

--
-- Name: insect_in_cond_init_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.insect_in_cond_init_id_seq OWNED BY public.insect_in_cond_init.id;


--
-- Name: intrinsic_value; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.intrinsic_value (
    id integer NOT NULL,
    id_type_intrinsic_value integer,
    id_test integer,
    time_begin time without time zone,
    time_end time without time zone,
    link character varying(255),
    confident character varying(20),
    remark character varying(255)
);


ALTER TABLE public.intrinsic_value OWNER TO postgres;

--
-- Name: intrinsic_value_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.intrinsic_value_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.intrinsic_value_id_seq OWNER TO postgres;

--
-- Name: intrinsic_value_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.intrinsic_value_id_seq OWNED BY public.intrinsic_value.id;


--
-- Name: intrinsic_value_value; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.intrinsic_value_value (
    id integer NOT NULL,
    id_intrinsic_value integer,
    id_type_param integer,
    value double precision
);


ALTER TABLE public.intrinsic_value_value OWNER TO postgres;

--
-- Name: intrinsic_value_value_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.intrinsic_value_value_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.intrinsic_value_value_id_seq OWNER TO postgres;

--
-- Name: intrinsic_value_value_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.intrinsic_value_value_id_seq OWNED BY public.intrinsic_value_value.id;


--
-- Name: param_intrinsic_value; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.param_intrinsic_value (
    id integer NOT NULL,
    id_type_intrinsic_value integer,
    id_type_param integer
);


ALTER TABLE public.param_intrinsic_value OWNER TO postgres;

--
-- Name: param_intrinsic_value_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.param_intrinsic_value_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.param_intrinsic_value_id_seq OWNER TO postgres;

--
-- Name: param_intrinsic_value_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.param_intrinsic_value_id_seq OWNED BY public.param_intrinsic_value.id;


--
-- Name: param_test_point; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.param_test_point (
    id integer NOT NULL,
    id_type_test_point integer,
    id_type_param integer
);


ALTER TABLE public.param_test_point OWNER TO postgres;

--
-- Name: param_test_point_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.param_test_point_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.param_test_point_id_seq OWNER TO postgres;

--
-- Name: param_test_point_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.param_test_point_id_seq OWNED BY public.param_test_point.id;


--
-- Name: photo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.photo (
    id integer NOT NULL,
    id_test integer,
    name character varying(20),
    longitude double precision,
    latitude double precision,
    altitude_m double precision,
    altitude_feet double precision,
    gtm timestamp without time zone,
    duration double precision,
    distance double precision,
    incidence double precision,
    speed character varying(20),
    iso character varying(20),
    quantite character varying(20),
    poids double precision,
    validate boolean
);


ALTER TABLE public.photo OWNER TO postgres;

--
-- Name: photo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.photo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.photo_id_seq OWNER TO postgres;

--
-- Name: photo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.photo_id_seq OWNED BY public.photo.id;


--
-- Name: pilot; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pilot (
    id integer NOT NULL,
    pilot character varying(20)
);


ALTER TABLE public.pilot OWNER TO postgres;

--
-- Name: pilot_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pilot_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pilot_id_seq OWNER TO postgres;

--
-- Name: pilot_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pilot_id_seq OWNED BY public.pilot.id;


--
-- Name: position_on_tank; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.position_on_tank (
    id integer NOT NULL,
    id_tank integer,
    num_loc character varying(20),
    coord double precision[],
    metric double precision[],
    type character varying(20)
);


ALTER TABLE public.position_on_tank OWNER TO postgres;

--
-- Name: position_on_tank_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.position_on_tank_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.position_on_tank_id_seq OWNER TO postgres;

--
-- Name: position_on_tank_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.position_on_tank_id_seq OWNED BY public.position_on_tank.id;


--
-- Name: quantite; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.quantite (
    id integer NOT NULL,
    id_ejector_in_config integer,
    id_cond_init integer,
    id_insect integer,
    qnt double precision,
    validate boolean
);


ALTER TABLE public.quantite OWNER TO postgres;

--
-- Name: quantite_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.quantite_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.quantite_id_seq OWNER TO postgres;

--
-- Name: quantite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.quantite_id_seq OWNED BY public.quantite.id;


--
-- Name: ref_sensor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ref_sensor (
    id integer NOT NULL,
    id_type_sensor integer,
    ref character varying(20)
);


ALTER TABLE public.ref_sensor OWNER TO postgres;

--
-- Name: ref_sensor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ref_sensor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ref_sensor_id_seq OWNER TO postgres;

--
-- Name: ref_sensor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ref_sensor_id_seq OWNED BY public.ref_sensor.id;


--
-- Name: sensor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sensor (
    id integer NOT NULL,
    id_ref_sensor integer,
    number character varying(20),
    validate boolean
);


ALTER TABLE public.sensor OWNER TO postgres;

--
-- Name: sensor_coating_config; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sensor_coating_config (
    id integer NOT NULL,
    id_position_on_tank integer,
    id_sensor integer,
    id_coating integer,
    id_tank_configuration integer
);


ALTER TABLE public.sensor_coating_config OWNER TO postgres;

--
-- Name: sensor_coating_config_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sensor_coating_config_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sensor_coating_config_id_seq OWNER TO postgres;

--
-- Name: sensor_coating_config_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sensor_coating_config_id_seq OWNED BY public.sensor_coating_config.id;


--
-- Name: sensor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sensor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sensor_id_seq OWNER TO postgres;

--
-- Name: sensor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sensor_id_seq OWNED BY public.sensor.id;


--
-- Name: sensor_location; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sensor_location (
    id integer NOT NULL,
    type character varying(20),
    ref character varying(20),
    serial_number character varying(20),
    "order" character varying(20),
    location character varying(20),
    "time" timestamp with time zone,
    validation boolean
);


ALTER TABLE public.sensor_location OWNER TO postgres;

--
-- Name: sensor_location_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sensor_location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sensor_location_id_seq OWNER TO postgres;

--
-- Name: sensor_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sensor_location_id_seq OWNED BY public.sensor_location.id;


--
-- Name: software; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.software (
    id integer NOT NULL,
    ref character varying(20),
    release character varying(20)
);


ALTER TABLE public.software OWNER TO postgres;

--
-- Name: software_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.software_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.software_id_seq OWNER TO postgres;

--
-- Name: software_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.software_id_seq OWNED BY public.software.id;


--
-- Name: software_value; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.software_value (
    id integer NOT NULL,
    ref character varying(20),
    release character varying(20)
);


ALTER TABLE public.software_value OWNER TO postgres;

--
-- Name: software_value_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.software_value_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.software_value_id_seq OWNER TO postgres;

--
-- Name: software_value_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.software_value_id_seq OWNED BY public.software_value.id;


--
-- Name: software_value_software; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.software_value_software (
    id integer NOT NULL,
    id_software integer,
    id_software_value integer
);


ALTER TABLE public.software_value_software OWNER TO postgres;

--
-- Name: software_value_software_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.software_value_software_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.software_value_software_id_seq OWNER TO postgres;

--
-- Name: software_value_software_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.software_value_software_id_seq OWNED BY public.software_value_software.id;


--
-- Name: tank; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tank (
    id integer NOT NULL,
    id_type_tank integer,
    number character varying(20),
    validate boolean
);


ALTER TABLE public.tank OWNER TO postgres;

--
-- Name: tank_configuration; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tank_configuration (
    id integer NOT NULL,
    ref character varying(20),
    date date,
    validate boolean,
    tank_type integer
);


ALTER TABLE public.tank_configuration OWNER TO postgres;

--
-- Name: tank_configuration_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tank_configuration_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tank_configuration_id_seq OWNER TO postgres;

--
-- Name: tank_configuration_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tank_configuration_id_seq OWNED BY public.tank_configuration.id;


--
-- Name: tank_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tank_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tank_id_seq OWNER TO postgres;

--
-- Name: tank_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tank_id_seq OWNED BY public.tank.id;


--
-- Name: test; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.test (
    id integer NOT NULL,
    id_test_mean integer,
    type character varying(20),
    number character varying(20),
    id_test_driver integer,
    date date,
    time_begin time without time zone,
    time_end time without time zone,
    id_tank_conf integer,
    id_acqui_conf integer,
    id_camera_conf integer,
    id_ejector_conf integer,
    id_cond_init integer,
    id_pilot integer,
    id_copilot integer,
    validate boolean,
    achievement double precision
);


ALTER TABLE public.test OWNER TO postgres;

--
-- Name: test_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.test_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.test_id_seq OWNER TO postgres;

--
-- Name: test_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.test_id_seq OWNED BY public.test.id;


--
-- Name: test_mean; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.test_mean (
    id integer NOT NULL,
    type character varying(20),
    name character varying(20),
    number character varying(20),
    validate boolean
);


ALTER TABLE public.test_mean OWNER TO postgres;

--
-- Name: test_mean_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.test_mean_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.test_mean_id_seq OWNER TO postgres;

--
-- Name: test_mean_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.test_mean_id_seq OWNED BY public.test_mean.id;


--
-- Name: test_point; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.test_point (
    id integer NOT NULL,
    id_type_test_point integer,
    id_test integer,
    time_begin time without time zone,
    time_end time without time zone,
    link character varying(255),
    confident character varying(20),
    remark character varying(255),
    issue integer,
    validate boolean
);


ALTER TABLE public.test_point OWNER TO postgres;

--
-- Name: test_point_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.test_point_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.test_point_id_seq OWNER TO postgres;

--
-- Name: test_point_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.test_point_id_seq OWNED BY public.test_point.id;


--
-- Name: test_point_value; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.test_point_value (
    id integer NOT NULL,
    id_test_point integer,
    id_type_param integer,
    value double precision
);


ALTER TABLE public.test_point_value OWNER TO postgres;

--
-- Name: test_point_value_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.test_point_value_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.test_point_value_id_seq OWNER TO postgres;

--
-- Name: test_point_value_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.test_point_value_id_seq OWNED BY public.test_point_value.id;


--
-- Name: test_team; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.test_team (
    id integer NOT NULL,
    ref character varying(20)
);


ALTER TABLE public.test_team OWNER TO postgres;

--
-- Name: test_team_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.test_team_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.test_team_id_seq OWNER TO postgres;

--
-- Name: test_team_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.test_team_id_seq OWNED BY public.test_team.id;


--
-- Name: type_camera; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_camera (
    id integer NOT NULL,
    ref character varying(20)
);


ALTER TABLE public.type_camera OWNER TO postgres;

--
-- Name: type_camera_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_camera_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_camera_id_seq OWNER TO postgres;

--
-- Name: type_camera_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_camera_id_seq OWNED BY public.type_camera.id;


--
-- Name: type_coating; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_coating (
    id integer NOT NULL,
    ref character varying(20)
);


ALTER TABLE public.type_coating OWNER TO postgres;

--
-- Name: type_coating_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_coating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_coating_id_seq OWNER TO postgres;

--
-- Name: type_coating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_coating_id_seq OWNED BY public.type_coating.id;


--
-- Name: type_detergent; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_detergent (
    id integer NOT NULL,
    ref character varying(20)
);


ALTER TABLE public.type_detergent OWNER TO postgres;

--
-- Name: type_detergent_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_detergent_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_detergent_id_seq OWNER TO postgres;

--
-- Name: type_detergent_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_detergent_id_seq OWNED BY public.type_detergent.id;


--
-- Name: type_document; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_document (
    id integer NOT NULL,
    ref character varying(20)
);


ALTER TABLE public.type_document OWNER TO postgres;

--
-- Name: type_document_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_document_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_document_id_seq OWNER TO postgres;

--
-- Name: type_document_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_document_id_seq OWNED BY public.type_document.id;


--
-- Name: type_ejector; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_ejector (
    id integer NOT NULL,
    ref character varying(20)
);


ALTER TABLE public.type_ejector OWNER TO postgres;

--
-- Name: type_ejector_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_ejector_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_ejector_id_seq OWNER TO postgres;

--
-- Name: type_ejector_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_ejector_id_seq OWNED BY public.type_ejector.id;


--
-- Name: type_intrinsic_value; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_intrinsic_value (
    id integer NOT NULL,
    ref character varying(20),
    create_by character varying(20),
    state character varying(20)
);


ALTER TABLE public.type_intrinsic_value OWNER TO postgres;

--
-- Name: type_intrinsic_value_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_intrinsic_value_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_intrinsic_value_id_seq OWNER TO postgres;

--
-- Name: type_intrinsic_value_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_intrinsic_value_id_seq OWNED BY public.type_intrinsic_value.id;


--
-- Name: type_param; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_param (
    id integer NOT NULL,
    name character varying(20),
    id_unity integer,
    axes integer[]
);


ALTER TABLE public.type_param OWNER TO postgres;

--
-- Name: type_param_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_param_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_param_id_seq OWNER TO postgres;

--
-- Name: type_param_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_param_id_seq OWNED BY public.type_param.id;


--
-- Name: type_param_sensor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_param_sensor (
    id integer NOT NULL,
    id_ref_sensor integer,
    id_type_param integer
);


ALTER TABLE public.type_param_sensor OWNER TO postgres;

--
-- Name: type_param_sensor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_param_sensor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_param_sensor_id_seq OWNER TO postgres;

--
-- Name: type_param_sensor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_param_sensor_id_seq OWNED BY public.type_param_sensor.id;


--
-- Name: type_param_test_mean; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_param_test_mean (
    id integer NOT NULL,
    id_test_mean integer,
    id_type_param integer
);


ALTER TABLE public.type_param_test_mean OWNER TO postgres;

--
-- Name: type_param_test_mean_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_param_test_mean_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_param_test_mean_id_seq OWNER TO postgres;

--
-- Name: type_param_test_mean_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_param_test_mean_id_seq OWNED BY public.type_param_test_mean.id;


--
-- Name: type_role; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_role (
    id integer NOT NULL,
    ref character varying(20)
);


ALTER TABLE public.type_role OWNER TO postgres;

--
-- Name: type_role_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_role_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_role_id_seq OWNER TO postgres;

--
-- Name: type_role_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_role_id_seq OWNED BY public.type_role.id;


--
-- Name: type_sensor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_sensor (
    id integer NOT NULL,
    ref character varying(20)
);


ALTER TABLE public.type_sensor OWNER TO postgres;

--
-- Name: type_sensor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_sensor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_sensor_id_seq OWNER TO postgres;

--
-- Name: type_sensor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_sensor_id_seq OWNED BY public.type_sensor.id;


--
-- Name: type_tank; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_tank (
    id integer NOT NULL,
    ref character varying(20)
);


ALTER TABLE public.type_tank OWNER TO postgres;

--
-- Name: type_tank_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_tank_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_tank_id_seq OWNER TO postgres;

--
-- Name: type_tank_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_tank_id_seq OWNED BY public.type_tank.id;


--
-- Name: type_test_point; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_test_point (
    id integer NOT NULL,
    ref character varying(20),
    create_by character varying(20),
    state character varying(20)
);


ALTER TABLE public.type_test_point OWNER TO postgres;

--
-- Name: type_test_point_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_test_point_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_test_point_id_seq OWNER TO postgres;

--
-- Name: type_test_point_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_test_point_id_seq OWNED BY public.type_test_point.id;


--
-- Name: type_unity; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.type_unity (
    id integer NOT NULL,
    ref character varying(20)
);


ALTER TABLE public.type_unity OWNER TO postgres;

--
-- Name: type_unity_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.type_unity_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.type_unity_id_seq OWNER TO postgres;

--
-- Name: type_unity_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.type_unity_id_seq OWNED BY public.type_unity.id;


--
-- Name: user_right; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_right (
    id integer NOT NULL,
    id_account integer,
    role integer,
    id_test_mean integer,
    id_type_coating integer,
    id_type_detergent integer,
    id_type_tank integer,
    id_type_sensor integer,
    id_type_ejector integer,
    id_type_camera integer,
    id_type_test_point integer,
    id_type_intrinsic_value integer,
    id_test_team integer,
    insect boolean,
    acqui_system boolean
);


ALTER TABLE public.user_right OWNER TO postgres;

--
-- Name: user_right_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_right_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_right_id_seq OWNER TO postgres;

--
-- Name: user_right_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_right_id_seq OWNED BY public.user_right.id;


--
-- Name: velocity_speed; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.velocity_speed (
    id integer NOT NULL,
    id_ejector_in_config integer,
    id_cond_init integer,
    speed double precision,
    validate boolean
);


ALTER TABLE public.velocity_speed OWNER TO postgres;

--
-- Name: velocity_speed_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.velocity_speed_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.velocity_speed_id_seq OWNER TO postgres;

--
-- Name: velocity_speed_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.velocity_speed_id_seq OWNED BY public.velocity_speed.id;


--
-- Name: account id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account ALTER COLUMN id SET DEFAULT nextval('public.account_id_seq'::regclass);


--
-- Name: acquisition_config id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acquisition_config ALTER COLUMN id SET DEFAULT nextval('public.acquisition_config_id_seq'::regclass);


--
-- Name: airfield id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.airfield ALTER COLUMN id SET DEFAULT nextval('public.airfield_id_seq'::regclass);


--
-- Name: attribute id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute ALTER COLUMN id SET DEFAULT nextval('public.attribute_id_seq'::regclass);


--
-- Name: attribute_coating id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_coating ALTER COLUMN id SET DEFAULT nextval('public.attribute_coating_id_seq'::regclass);


--
-- Name: attribute_detergent id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_detergent ALTER COLUMN id SET DEFAULT nextval('public.attribute_detergent_id_seq'::regclass);


--
-- Name: attribute_test_mean id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_test_mean ALTER COLUMN id SET DEFAULT nextval('public.attribute_test_mean_id_seq'::regclass);


--
-- Name: calibration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.calibration ALTER COLUMN id SET DEFAULT nextval('public.calibration_id_seq'::regclass);


--
-- Name: camera id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.camera ALTER COLUMN id SET DEFAULT nextval('public.camera_id_seq'::regclass);


--
-- Name: camera_in_config id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.camera_in_config ALTER COLUMN id SET DEFAULT nextval('public.camera_in_config_id_seq'::regclass);


--
-- Name: coating id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coating ALTER COLUMN id SET DEFAULT nextval('public.coating_id_seq'::regclass);


--
-- Name: coating_location id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coating_location ALTER COLUMN id SET DEFAULT nextval('public.coating_location_id_seq'::regclass);


--
-- Name: cond_init id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cond_init ALTER COLUMN id SET DEFAULT nextval('public.cond_init_id_seq'::regclass);


--
-- Name: config_camera id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.config_camera ALTER COLUMN id SET DEFAULT nextval('public.config_camera_id_seq'::regclass);


--
-- Name: config_on_acqui id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.config_on_acqui ALTER COLUMN id SET DEFAULT nextval('public.config_on_acqui_id_seq'::regclass);


--
-- Name: data_sensor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_sensor ALTER COLUMN id SET DEFAULT nextval('public.data_sensor_id_seq'::regclass);


--
-- Name: data_vol id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_vol ALTER COLUMN id SET DEFAULT nextval('public.data_vol_id_seq'::regclass);


--
-- Name: def_test_point id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.def_test_point ALTER COLUMN id SET DEFAULT nextval('public.def_test_point_id_seq'::regclass);


--
-- Name: detergent id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detergent ALTER COLUMN id SET DEFAULT nextval('public.detergent_id_seq'::regclass);


--
-- Name: document id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.document ALTER COLUMN id SET DEFAULT nextval('public.document_id_seq'::regclass);


--
-- Name: document_test id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.document_test ALTER COLUMN id SET DEFAULT nextval('public.document_test_id_seq'::regclass);


--
-- Name: ejector id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ejector ALTER COLUMN id SET DEFAULT nextval('public.ejector_id_seq'::regclass);


--
-- Name: ejector_config id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ejector_config ALTER COLUMN id SET DEFAULT nextval('public.ejector_config_id_seq'::regclass);


--
-- Name: ejector_in_config id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ejector_in_config ALTER COLUMN id SET DEFAULT nextval('public.ejector_in_config_id_seq'::regclass);


--
-- Name: hardware id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hardware ALTER COLUMN id SET DEFAULT nextval('public.hardware_id_seq'::regclass);


--
-- Name: hardware_software id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hardware_software ALTER COLUMN id SET DEFAULT nextval('public.hardware_software_id_seq'::regclass);


--
-- Name: insect id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.insect ALTER COLUMN id SET DEFAULT nextval('public.insect_id_seq'::regclass);


--
-- Name: insect_in_cond_init id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.insect_in_cond_init ALTER COLUMN id SET DEFAULT nextval('public.insect_in_cond_init_id_seq'::regclass);


--
-- Name: intrinsic_value id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.intrinsic_value ALTER COLUMN id SET DEFAULT nextval('public.intrinsic_value_id_seq'::regclass);


--
-- Name: intrinsic_value_value id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.intrinsic_value_value ALTER COLUMN id SET DEFAULT nextval('public.intrinsic_value_value_id_seq'::regclass);


--
-- Name: param_intrinsic_value id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.param_intrinsic_value ALTER COLUMN id SET DEFAULT nextval('public.param_intrinsic_value_id_seq'::regclass);


--
-- Name: param_test_point id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.param_test_point ALTER COLUMN id SET DEFAULT nextval('public.param_test_point_id_seq'::regclass);


--
-- Name: photo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.photo ALTER COLUMN id SET DEFAULT nextval('public.photo_id_seq'::regclass);


--
-- Name: pilot id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pilot ALTER COLUMN id SET DEFAULT nextval('public.pilot_id_seq'::regclass);


--
-- Name: position_on_tank id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.position_on_tank ALTER COLUMN id SET DEFAULT nextval('public.position_on_tank_id_seq'::regclass);


--
-- Name: quantite id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quantite ALTER COLUMN id SET DEFAULT nextval('public.quantite_id_seq'::regclass);


--
-- Name: ref_sensor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ref_sensor ALTER COLUMN id SET DEFAULT nextval('public.ref_sensor_id_seq'::regclass);


--
-- Name: sensor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor ALTER COLUMN id SET DEFAULT nextval('public.sensor_id_seq'::regclass);


--
-- Name: sensor_coating_config id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor_coating_config ALTER COLUMN id SET DEFAULT nextval('public.sensor_coating_config_id_seq'::regclass);


--
-- Name: sensor_location id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor_location ALTER COLUMN id SET DEFAULT nextval('public.sensor_location_id_seq'::regclass);


--
-- Name: software id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.software ALTER COLUMN id SET DEFAULT nextval('public.software_id_seq'::regclass);


--
-- Name: software_value id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.software_value ALTER COLUMN id SET DEFAULT nextval('public.software_value_id_seq'::regclass);


--
-- Name: software_value_software id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.software_value_software ALTER COLUMN id SET DEFAULT nextval('public.software_value_software_id_seq'::regclass);


--
-- Name: tank id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tank ALTER COLUMN id SET DEFAULT nextval('public.tank_id_seq'::regclass);


--
-- Name: tank_configuration id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tank_configuration ALTER COLUMN id SET DEFAULT nextval('public.tank_configuration_id_seq'::regclass);


--
-- Name: test id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test ALTER COLUMN id SET DEFAULT nextval('public.test_id_seq'::regclass);


--
-- Name: test_mean id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_mean ALTER COLUMN id SET DEFAULT nextval('public.test_mean_id_seq'::regclass);


--
-- Name: test_point id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_point ALTER COLUMN id SET DEFAULT nextval('public.test_point_id_seq'::regclass);


--
-- Name: test_point_value id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_point_value ALTER COLUMN id SET DEFAULT nextval('public.test_point_value_id_seq'::regclass);


--
-- Name: test_team id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_team ALTER COLUMN id SET DEFAULT nextval('public.test_team_id_seq'::regclass);


--
-- Name: type_camera id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_camera ALTER COLUMN id SET DEFAULT nextval('public.type_camera_id_seq'::regclass);


--
-- Name: type_coating id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_coating ALTER COLUMN id SET DEFAULT nextval('public.type_coating_id_seq'::regclass);


--
-- Name: type_detergent id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_detergent ALTER COLUMN id SET DEFAULT nextval('public.type_detergent_id_seq'::regclass);


--
-- Name: type_document id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_document ALTER COLUMN id SET DEFAULT nextval('public.type_document_id_seq'::regclass);


--
-- Name: type_ejector id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_ejector ALTER COLUMN id SET DEFAULT nextval('public.type_ejector_id_seq'::regclass);


--
-- Name: type_intrinsic_value id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_intrinsic_value ALTER COLUMN id SET DEFAULT nextval('public.type_intrinsic_value_id_seq'::regclass);


--
-- Name: type_param id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_param ALTER COLUMN id SET DEFAULT nextval('public.type_param_id_seq'::regclass);


--
-- Name: type_param_sensor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_param_sensor ALTER COLUMN id SET DEFAULT nextval('public.type_param_sensor_id_seq'::regclass);


--
-- Name: type_param_test_mean id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_param_test_mean ALTER COLUMN id SET DEFAULT nextval('public.type_param_test_mean_id_seq'::regclass);


--
-- Name: type_role id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_role ALTER COLUMN id SET DEFAULT nextval('public.type_role_id_seq'::regclass);


--
-- Name: type_sensor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_sensor ALTER COLUMN id SET DEFAULT nextval('public.type_sensor_id_seq'::regclass);


--
-- Name: type_tank id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_tank ALTER COLUMN id SET DEFAULT nextval('public.type_tank_id_seq'::regclass);


--
-- Name: type_test_point id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_test_point ALTER COLUMN id SET DEFAULT nextval('public.type_test_point_id_seq'::regclass);


--
-- Name: type_unity id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_unity ALTER COLUMN id SET DEFAULT nextval('public.type_unity_id_seq'::regclass);


--
-- Name: user_right id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right ALTER COLUMN id SET DEFAULT nextval('public.user_right_id_seq'::regclass);


--
-- Name: velocity_speed id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.velocity_speed ALTER COLUMN id SET DEFAULT nextval('public.velocity_speed_id_seq'::regclass);


--
-- Data for Name: account; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.account (id, uname, orga, fname, lname, tel, email, password) FROM stdin;
1	root	root	\N	\N	\N	\N	123456
2	manager	group_manager	\N	\N	\N	\N	123456
3	validator	orga_1	fname1	lname1	\N	\N	0000
4	creator	orga_1	fname2	lname2	\N	\N	0000
5	reader	orga_1	fname2	lname2	\N	\N	0000
6	nobody	\N	\N	\N	\N	\N	0000
7	Bob	\N	\N	\N	\N	\N	0000
8	Jack	\N	\N	\N	\N	\N	0000
9	Alice	\N	\N	\N	\N	\N	0000
10	Steven	\N	\N	\N	\N	\N	0000
11	Rose	\N	\N	\N	\N	\N	0000
\.


--
-- Data for Name: acquisition_config; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.acquisition_config (id, ref, date, validate) FROM stdin;
1	acq_1	\N	t
2	acq_2	\N	t
\.


--
-- Data for Name: airfield; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.airfield (id, name, runway, alt) FROM stdin;
1	Aix	Ron	1300
2	Paris	Louvre	0
3	Shanghai	Bund	10
\.


--
-- Data for Name: attribute; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attribute (id, attribute, id_unity, value) FROM stdin;
1	Hydrochloroquine	1	85
2	Aspirine	1	10
3	Arsonic	1	5
4	Substrate	3	19
5	Coating Type	3	75
6	a1	2	10
7	a2	2	20
8	a3	2	30
9	Altitude	4	3000
10	Max Speed	5	120
11	Wing setting	6	1.5
\.


--
-- Data for Name: attribute_coating; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attribute_coating (id, id_coating, id_attribute) FROM stdin;
1	1	1
2	1	2
3	1	3
4	2	4
5	2	5
6	7	6
7	7	7
8	8	8
\.


--
-- Data for Name: attribute_detergent; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attribute_detergent (id, id_detergent, id_attribute) FROM stdin;
\.


--
-- Data for Name: attribute_test_mean; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.attribute_test_mean (id, id_test_mean, id_attribute) FROM stdin;
1	2	9
2	2	10
3	2	11
\.


--
-- Data for Name: calibration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.calibration (id, id_sensor, id_type_param, id_type_versus, value_mesure, value_true, value_versus) FROM stdin;
\.


--
-- Data for Name: camera; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.camera (id, id_type_camera, number, s_min, s_max, axe, h_aperture, w_aperture) FROM stdin;
1	1	12	\N	\N	\N	\N	\N
\.


--
-- Data for Name: camera_in_config; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.camera_in_config (id, id_config_camera, id_test_mean, d, h_axe, v_axe, s, lens) FROM stdin;
\.


--
-- Data for Name: coating; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.coating (id, id_type_coating, number, validate) FROM stdin;
1	1	CH-1	t
2	1	CH-2	f
3	2	1-Root	t
4	2	2-Middle Root	t
5	2	3-Middle End	t
6	2	4-End	t
7	1	n1	t
8	1	n2	t
9	1	n3	t
\.


--
-- Data for Name: coating_location; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.coating_location (id, id_coating, "order", location, date, validation) FROM stdin;
\.


--
-- Data for Name: cond_init; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cond_init (id, cond_init, id_airfield) FROM stdin;
1	["1_", "2_", "3_", "4_", "5_", "6_", "7_", "8_"]	1
\.


--
-- Data for Name: config_camera; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.config_camera (id, ref, type_camera, date, validate) FROM stdin;
1	camera_config_1	1	\N	t
2	camera_config_2	1	\N	t
\.


--
-- Data for Name: config_on_acqui; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.config_on_acqui (id, id_hardware, id_software, id_software_value, id_acquisition_config) FROM stdin;
\.


--
-- Data for Name: data_sensor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data_sensor (id, id_test, id_sensor_coating_config, id_type_param, "time", value, validate) FROM stdin;
1	1	1	1	14:21:12.1222	100	t
2	1	1	1	15:35:38.654805	120	t
\.


--
-- Data for Name: data_vol; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data_vol (id, id_test, id_type_param, "time", value, validate) FROM stdin;
1	1	1	15:35:38.654805	999	t
\.


--
-- Data for Name: def_test_point; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.def_test_point (id, id_type_test_point, coating, detergent, create_by, validation) FROM stdin;
\.


--
-- Data for Name: detergent; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.detergent (id, id_type_detergent, number, validate) FROM stdin;
\.


--
-- Data for Name: document; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.document (id, type, ref, number, link, validate) FROM stdin;
\.


--
-- Data for Name: document_test; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.document_test (id, id_test, id_document, validate) FROM stdin;
\.


--
-- Data for Name: ejector; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ejector (id, id_type_ejector, number, v_min, v_max, e_axe, ins_vol, nb_type) FROM stdin;
\.


--
-- Data for Name: ejector_config; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ejector_config (id, ref, type_ejector, date, validation) FROM stdin;
\.


--
-- Data for Name: ejector_in_config; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ejector_in_config (id, id_ejector_config, d, h_axe, v_axe) FROM stdin;
\.


--
-- Data for Name: hardware; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hardware (id, ref, number) FROM stdin;
\.


--
-- Data for Name: hardware_software; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.hardware_software (id, id_hardware, id_software) FROM stdin;
\.


--
-- Data for Name: insect; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.insect (id, name, masse, alt_min, alt_max, length, width, thickness, hemolymphe) FROM stdin;
1	Beattle	0.05	1500	2000	5	0.75	1.2	
2	Bombyx	0.05	3500	4250	7	1.05	1.3	
3	Butterfly	0.05	1000	1500	3.5	0.5	0.9	
4	Fly	0.5	1400	1800	10.5	2.5	1.9	
5	Mosquito	0.07	10	50	1.35	0.5	0.8	
6	Spider	0.1	4500	5000	8.35	3.5	2.8	
\.


--
-- Data for Name: insect_in_cond_init; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.insect_in_cond_init (id, id_cond_init, id_insect, validate) FROM stdin;
\.


--
-- Data for Name: intrinsic_value; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.intrinsic_value (id, id_type_intrinsic_value, id_test, time_begin, time_end, link, confident, remark) FROM stdin;
\.


--
-- Data for Name: intrinsic_value_value; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.intrinsic_value_value (id, id_intrinsic_value, id_type_param, value) FROM stdin;
\.


--
-- Data for Name: param_intrinsic_value; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.param_intrinsic_value (id, id_type_intrinsic_value, id_type_param) FROM stdin;
\.


--
-- Data for Name: param_test_point; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.param_test_point (id, id_type_test_point, id_type_param) FROM stdin;
\.


--
-- Data for Name: photo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.photo (id, id_test, name, longitude, latitude, altitude_m, altitude_feet, gtm, duration, distance, incidence, speed, iso, quantite, poids, validate) FROM stdin;
\.


--
-- Data for Name: pilot; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pilot (id, pilot) FROM stdin;
1	Zara
2	Hermes
\.


--
-- Data for Name: position_on_tank; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.position_on_tank (id, id_tank, num_loc, coord, metric, type) FROM stdin;
1	3	0-0	{2436,4,-49}	{{0.945535186276394,0,0.32551990954973},{0,1,0},{0.32551990954973,0,-0.945535186276394}}	Barometric
2	3	0-1	{2481,4,-14}	{{0.357433463675218,1,0.933938605608065},{0,1,0},{0.933938605608065,0,-0.357433463675218}}	Barometric
3	3	0-2	{2483,4,3.7}	{{-0.147483612534009,2,0.989064499430608},{0,1,0},{0.989064499430608,0,0.147483612534009}}	Barometric
4	3	0-3	{2481,4,14}	{{-0.415508705876326,3,0.909589201420609},{0,1,0},{0.909589201420609,0,0.415508705876326}}	Barometric
5	3	0-4	{2475.8,4,23}	{{-0.589537583490262,4,0.807740947118853},{0,1,0},{0.807740947118853,0,0.589537583490262}}	Barometric
6	3	0-5	{2470,4,31}	{{-0.675226947737502,5,0.737610038603798},{0,1,0},{0.737610038603798,0,0.675226947737502}}	Barometric
7	3	0-6	{2462,4,38}	{{-0.763463846138858,6,0.645850567576481},{0,1,0},{0.645850567576481,0,0.763463846138858}}	Barometric
8	3	0-7	{2454,4,45}	{{-0.858238276023236,7,0.513251460366811},{0,1,0},{0.513251460366811,0,0.858238276023236}}	Barometric
9	3	0-8	{2445,4,51.5}	{{-0.85220124087634,8,0.523214148364535},{0,1,0},{0.523214148364535,0,0.85220124087634}}	Barometric
10	3	0-9	{2436,4,57}	{{-0.868983421255946,9,0.494841200368675},{0,1,0},{0.494841200368675,0,0.868983421255946}}	Barometric
11	3	0-10	{2427,4,62}	{{-0.898048507369272,10,0.439896440553708},{0,1,0},{0.439896440553708,0,0.898048507369272}}	Barometric
12	3	0-11	{2410,4,72}	{{-0.915219523626268,11,0.402955609929067},{0,1,0},{0.402955609929067,0,-0.915219523626268}}	Barometric
\.


--
-- Data for Name: quantite; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.quantite (id, id_ejector_in_config, id_cond_init, id_insect, qnt, validate) FROM stdin;
\.


--
-- Data for Name: ref_sensor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ref_sensor (id, id_type_sensor, ref) FROM stdin;
1	2	LIS3DH
\.


--
-- Data for Name: sensor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sensor (id, id_ref_sensor, number, validate) FROM stdin;
1	1	001	t
2	1	002	t
\.


--
-- Data for Name: sensor_coating_config; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sensor_coating_config (id, id_position_on_tank, id_sensor, id_coating, id_tank_configuration) FROM stdin;
1	\N	1	\N	\N
\.


--
-- Data for Name: sensor_location; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sensor_location (id, type, ref, serial_number, "order", location, "time", validation) FROM stdin;
1	Accelerometer	LIS3DH	001	order	in store	2022-06-21 15:35:38.644159+02	t
2	Accelerometer	LIS3DH	002	order	in store	2022-06-21 15:35:38.644159+02	t
\.


--
-- Data for Name: software; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.software (id, ref, release) FROM stdin;
\.


--
-- Data for Name: software_value; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.software_value (id, ref, release) FROM stdin;
\.


--
-- Data for Name: software_value_software; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.software_value_software (id, id_software, id_software_value) FROM stdin;
\.


--
-- Data for Name: tank; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tank (id, id_type_tank, number, validate) FROM stdin;
1	2	tk_00	f
2	2	tk_01	f
3	1	t1	f
\.


--
-- Data for Name: tank_configuration; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tank_configuration (id, ref, date, validate, tank_type) FROM stdin;
1	tk_config_01	2022-06-21	t	1
2	tk_config_02	2022-06-21	f	2
3	tank_config_1	2022-06-21	t	3
4	tank_config_2	2022-06-21	t	3
\.


--
-- Data for Name: test; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.test (id, id_test_mean, type, number, id_test_driver, date, time_begin, time_end, id_tank_conf, id_acqui_conf, id_camera_conf, id_ejector_conf, id_cond_init, id_pilot, id_copilot, validate, achievement) FROM stdin;
1	2	Flight	158	9	2022-05-25	08:00:00	21:00:00	1	1	1	\N	1	1	2	f	0.75
\.


--
-- Data for Name: test_mean; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.test_mean (id, type, name, number, validate) FROM stdin;
1	Aircraft	A320	1258	f
2	Aircraft	SONACA 200	12	f
3	Aircraft	SONACA 200	25	t
4	Wind tunnel	CWT	1	f
5	Wind tunnel	VKI	L1-A	t
\.


--
-- Data for Name: test_point; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.test_point (id, id_type_test_point, id_test, time_begin, time_end, link, confident, remark, issue, validate) FROM stdin;
\.


--
-- Data for Name: test_point_value; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.test_point_value (id, id_test_point, id_type_param, value) FROM stdin;
\.


--
-- Data for Name: test_team; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.test_team (id, ref) FROM stdin;
1	Flight team
2	Wind Tunnel team
\.


--
-- Data for Name: type_camera; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_camera (id, ref) FROM stdin;
1	UV7076
2	came1
\.


--
-- Data for Name: type_coating; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_coating (id, ref) FROM stdin;
1	CHOPIN
2	STELLAR.WP5.CID.COAT
\.


--
-- Data for Name: type_detergent; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_detergent (id, ref) FROM stdin;
1	SOPURA.STELLAR
2	VACINNE
\.


--
-- Data for Name: type_document; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_document (id, ref) FROM stdin;
\.


--
-- Data for Name: type_ejector; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_ejector (id, ref) FROM stdin;
1	Chopin ejector
\.


--
-- Data for Name: type_intrinsic_value; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_intrinsic_value (id, ref, create_by, state) FROM stdin;
\.


--
-- Data for Name: type_param; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_param (id, name, id_unity, axes) FROM stdin;
1	Ld Time	7	\N
2	UTCOfst	8	\N
3	AltB	9	\N
4	Latitude	10	\N
5	Longitude	10	\N
6	AltMSL	11	\N
7	IAS	5	\N
8	Pitch	6	\N
9	Roll	6	\N
10	Gama x	12	{1,0,0}
11	Gama y	12	{0,1,0}
12	Gama z	12	{0,0,1}
13	Course	6	\N
14	GPS altitude	4	\N
15	GPS Ground speed	13	\N
16	GPS heading	6	\N
17	Indicated air speed	13	\N
18	InHg Altitude	14	\N
19	ISA Pressure altitud	4	\N
20	Lateral acceleration	12	\N
21	Latitude	6	\N
22	local time UTC	7	\N
23	Longitude	6	\N
24	Magnetic heading	6	\N
25	Normal acceleration	12	\N
26	QFE altitude baro	4	\N
27	See level Altitude	4	\N
28	Static Temperature	15	\N
29	True Air Speed	13	\N
30	Vertical speed	16	\N
31	Wind direction	6	\N
32	Wind speed	13	\N
\.


--
-- Data for Name: type_param_sensor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_param_sensor (id, id_ref_sensor, id_type_param) FROM stdin;
1	1	10
2	1	11
3	1	12
\.


--
-- Data for Name: type_param_test_mean; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_param_test_mean (id, id_test_mean, id_type_param) FROM stdin;
7	2	13
8	2	14
9	2	15
10	2	16
11	2	17
12	2	18
13	2	19
14	2	20
15	2	21
16	2	22
17	2	23
18	2	24
19	2	25
20	2	8
21	2	26
22	2	9
23	2	27
24	2	28
25	2	29
26	2	30
27	2	31
28	2	32
\.


--
-- Data for Name: type_role; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_role (id, ref) FROM stdin;
1	manager
2	administrator
3	valideur
4	creator
5	reader
6	none
\.


--
-- Data for Name: type_sensor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_sensor (id, ref) FROM stdin;
1	Barometric
2	Accelerometer
\.


--
-- Data for Name: type_tank; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_tank (id, ref) FROM stdin;
1	T_Snonaca 200
2	Slat A320
\.


--
-- Data for Name: type_test_point; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_test_point (id, ref, create_by, state) FROM stdin;
1	Cleanability	\N	\N
2	Climb-out	\N	\N
3	Insect Residues	\N	\N
\.


--
-- Data for Name: type_unity; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_unity (id, ref) FROM stdin;
1	%
2	
3	cm
4	ft
5	kt
6	deg
7	hh:mm:ss
8	hh:mm
9	ft Baro
10	degrees
11	ftmsl
12	g
13	Kts
14	inHg
15	deg C
16	ft/mn
\.


--
-- Data for Name: user_right; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_right (id, id_account, role, id_test_mean, id_type_coating, id_type_detergent, id_type_tank, id_type_sensor, id_type_ejector, id_type_camera, id_type_test_point, id_type_intrinsic_value, id_test_team, insect, acqui_system) FROM stdin;
1	1	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
2	2	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
3	3	2	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
4	3	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	t	\N
5	4	5	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	f	\N
6	3	5	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	f
7	4	2	2	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
8	3	3	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
9	4	4	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
10	5	5	\N	1	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
11	6	6	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N	\N
12	7	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N
13	8	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N
14	9	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	1	\N	\N
15	10	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N
16	7	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N
17	8	4	\N	\N	\N	\N	\N	\N	\N	\N	\N	2	\N	\N
\.


--
-- Data for Name: velocity_speed; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.velocity_speed (id, id_ejector_in_config, id_cond_init, speed, validate) FROM stdin;
\.


--
-- Name: account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.account_id_seq', 11, true);


--
-- Name: acquisition_config_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.acquisition_config_id_seq', 2, true);


--
-- Name: airfield_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.airfield_id_seq', 3, true);


--
-- Name: attribute_coating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attribute_coating_id_seq', 8, true);


--
-- Name: attribute_detergent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attribute_detergent_id_seq', 1, false);


--
-- Name: attribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attribute_id_seq', 11, true);


--
-- Name: attribute_test_mean_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attribute_test_mean_id_seq', 3, true);


--
-- Name: calibration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.calibration_id_seq', 1, false);


--
-- Name: camera_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.camera_id_seq', 1, true);


--
-- Name: camera_in_config_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.camera_in_config_id_seq', 1, false);


--
-- Name: coating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.coating_id_seq', 9, true);


--
-- Name: coating_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.coating_location_id_seq', 1, false);


--
-- Name: cond_init_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cond_init_id_seq', 1, true);


--
-- Name: config_camera_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.config_camera_id_seq', 2, true);


--
-- Name: config_on_acqui_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.config_on_acqui_id_seq', 1, false);


--
-- Name: data_sensor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.data_sensor_id_seq', 2, true);


--
-- Name: data_vol_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.data_vol_id_seq', 1, true);


--
-- Name: def_test_point_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.def_test_point_id_seq', 1, false);


--
-- Name: detergent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.detergent_id_seq', 1, false);


--
-- Name: document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.document_id_seq', 1, false);


--
-- Name: document_test_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.document_test_id_seq', 1, false);


--
-- Name: ejector_config_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ejector_config_id_seq', 1, false);


--
-- Name: ejector_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ejector_id_seq', 1, false);


--
-- Name: ejector_in_config_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ejector_in_config_id_seq', 1, false);


--
-- Name: hardware_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hardware_id_seq', 1, false);


--
-- Name: hardware_software_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hardware_software_id_seq', 1, false);


--
-- Name: insect_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.insect_id_seq', 6, true);


--
-- Name: insect_in_cond_init_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.insect_in_cond_init_id_seq', 1, false);


--
-- Name: intrinsic_value_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.intrinsic_value_id_seq', 1, false);


--
-- Name: intrinsic_value_value_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.intrinsic_value_value_id_seq', 1, false);


--
-- Name: param_intrinsic_value_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.param_intrinsic_value_id_seq', 1, false);


--
-- Name: param_test_point_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.param_test_point_id_seq', 1, false);


--
-- Name: photo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.photo_id_seq', 1, false);


--
-- Name: pilot_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pilot_id_seq', 2, true);


--
-- Name: position_on_tank_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.position_on_tank_id_seq', 12, true);


--
-- Name: quantite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.quantite_id_seq', 1, false);


--
-- Name: ref_sensor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ref_sensor_id_seq', 1, true);


--
-- Name: sensor_coating_config_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sensor_coating_config_id_seq', 1, true);


--
-- Name: sensor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sensor_id_seq', 2, true);


--
-- Name: sensor_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sensor_location_id_seq', 2, true);


--
-- Name: software_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.software_id_seq', 1, false);


--
-- Name: software_value_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.software_value_id_seq', 1, false);


--
-- Name: software_value_software_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.software_value_software_id_seq', 1, false);


--
-- Name: tank_configuration_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tank_configuration_id_seq', 4, true);


--
-- Name: tank_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tank_id_seq', 3, true);


--
-- Name: test_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.test_id_seq', 1, true);


--
-- Name: test_mean_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.test_mean_id_seq', 5, true);


--
-- Name: test_point_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.test_point_id_seq', 1, false);


--
-- Name: test_point_value_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.test_point_value_id_seq', 1, false);


--
-- Name: test_team_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.test_team_id_seq', 2, true);


--
-- Name: type_camera_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_camera_id_seq', 2, true);


--
-- Name: type_coating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_coating_id_seq', 2, true);


--
-- Name: type_detergent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_detergent_id_seq', 2, true);


--
-- Name: type_document_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_document_id_seq', 1, false);


--
-- Name: type_ejector_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_ejector_id_seq', 1, true);


--
-- Name: type_intrinsic_value_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_intrinsic_value_id_seq', 1, false);


--
-- Name: type_param_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_param_id_seq', 32, true);


--
-- Name: type_param_sensor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_param_sensor_id_seq', 3, true);


--
-- Name: type_param_test_mean_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_param_test_mean_id_seq', 28, true);


--
-- Name: type_role_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_role_id_seq', 1, false);


--
-- Name: type_sensor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_sensor_id_seq', 2, true);


--
-- Name: type_tank_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_tank_id_seq', 2, true);


--
-- Name: type_test_point_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_test_point_id_seq', 3, true);


--
-- Name: type_unity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_unity_id_seq', 16, true);


--
-- Name: user_right_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_right_id_seq', 17, true);


--
-- Name: velocity_speed_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.velocity_speed_id_seq', 1, false);


--
-- Name: account account_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account
    ADD CONSTRAINT account_pkey PRIMARY KEY (id);


--
-- Name: account account_uname_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.account
    ADD CONSTRAINT account_uname_key UNIQUE (uname);


--
-- Name: acquisition_config acquisition_config_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acquisition_config
    ADD CONSTRAINT acquisition_config_pkey PRIMARY KEY (id);


--
-- Name: acquisition_config acquisition_config_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.acquisition_config
    ADD CONSTRAINT acquisition_config_ref_key UNIQUE (ref);


--
-- Name: airfield airfield_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.airfield
    ADD CONSTRAINT airfield_pkey PRIMARY KEY (id);


--
-- Name: attribute_coating attribute_coating_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_coating
    ADD CONSTRAINT attribute_coating_pkey PRIMARY KEY (id);


--
-- Name: attribute_detergent attribute_detergent_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_detergent
    ADD CONSTRAINT attribute_detergent_pkey PRIMARY KEY (id);


--
-- Name: attribute attribute_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute
    ADD CONSTRAINT attribute_pkey PRIMARY KEY (id);


--
-- Name: attribute_test_mean attribute_test_mean_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_test_mean
    ADD CONSTRAINT attribute_test_mean_pkey PRIMARY KEY (id);


--
-- Name: calibration calibration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.calibration
    ADD CONSTRAINT calibration_pkey PRIMARY KEY (id);


--
-- Name: camera_in_config camera_in_config_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.camera_in_config
    ADD CONSTRAINT camera_in_config_pkey PRIMARY KEY (id);


--
-- Name: camera camera_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.camera
    ADD CONSTRAINT camera_pkey PRIMARY KEY (id);


--
-- Name: coating_location coating_location_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coating_location
    ADD CONSTRAINT coating_location_pkey PRIMARY KEY (id);


--
-- Name: coating coating_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coating
    ADD CONSTRAINT coating_pkey PRIMARY KEY (id);


--
-- Name: cond_init cond_init_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cond_init
    ADD CONSTRAINT cond_init_pkey PRIMARY KEY (id);


--
-- Name: config_camera config_camera_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.config_camera
    ADD CONSTRAINT config_camera_pkey PRIMARY KEY (id);


--
-- Name: config_camera config_camera_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.config_camera
    ADD CONSTRAINT config_camera_ref_key UNIQUE (ref);


--
-- Name: config_on_acqui config_on_acqui_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.config_on_acqui
    ADD CONSTRAINT config_on_acqui_pkey PRIMARY KEY (id);


--
-- Name: data_sensor data_sensor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_sensor
    ADD CONSTRAINT data_sensor_pkey PRIMARY KEY (id);


--
-- Name: data_vol data_vol_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_vol
    ADD CONSTRAINT data_vol_pkey PRIMARY KEY (id);


--
-- Name: def_test_point def_test_point_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.def_test_point
    ADD CONSTRAINT def_test_point_pkey PRIMARY KEY (id);


--
-- Name: detergent detergent_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detergent
    ADD CONSTRAINT detergent_pkey PRIMARY KEY (id);


--
-- Name: document document_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.document
    ADD CONSTRAINT document_pkey PRIMARY KEY (id);


--
-- Name: document_test document_test_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.document_test
    ADD CONSTRAINT document_test_pkey PRIMARY KEY (id);


--
-- Name: ejector_config ejector_config_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ejector_config
    ADD CONSTRAINT ejector_config_pkey PRIMARY KEY (id);


--
-- Name: ejector_config ejector_config_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ejector_config
    ADD CONSTRAINT ejector_config_ref_key UNIQUE (ref);


--
-- Name: ejector_in_config ejector_in_config_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ejector_in_config
    ADD CONSTRAINT ejector_in_config_pkey PRIMARY KEY (id);


--
-- Name: ejector ejector_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ejector
    ADD CONSTRAINT ejector_pkey PRIMARY KEY (id);


--
-- Name: hardware hardware_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hardware
    ADD CONSTRAINT hardware_pkey PRIMARY KEY (id);


--
-- Name: hardware_software hardware_software_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hardware_software
    ADD CONSTRAINT hardware_software_pkey PRIMARY KEY (id);


--
-- Name: insect_in_cond_init insect_in_cond_init_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.insect_in_cond_init
    ADD CONSTRAINT insect_in_cond_init_pkey PRIMARY KEY (id);


--
-- Name: insect insect_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.insect
    ADD CONSTRAINT insect_pkey PRIMARY KEY (id);


--
-- Name: intrinsic_value intrinsic_value_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.intrinsic_value
    ADD CONSTRAINT intrinsic_value_pkey PRIMARY KEY (id);


--
-- Name: intrinsic_value_value intrinsic_value_value_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.intrinsic_value_value
    ADD CONSTRAINT intrinsic_value_value_pkey PRIMARY KEY (id);


--
-- Name: param_intrinsic_value param_intrinsic_value_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.param_intrinsic_value
    ADD CONSTRAINT param_intrinsic_value_pkey PRIMARY KEY (id);


--
-- Name: param_test_point param_test_point_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.param_test_point
    ADD CONSTRAINT param_test_point_pkey PRIMARY KEY (id);


--
-- Name: photo photo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.photo
    ADD CONSTRAINT photo_pkey PRIMARY KEY (id);


--
-- Name: pilot pilot_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pilot
    ADD CONSTRAINT pilot_pkey PRIMARY KEY (id);


--
-- Name: position_on_tank position_on_tank_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.position_on_tank
    ADD CONSTRAINT position_on_tank_pkey PRIMARY KEY (id);


--
-- Name: quantite quantite_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quantite
    ADD CONSTRAINT quantite_pkey PRIMARY KEY (id);


--
-- Name: ref_sensor ref_sensor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ref_sensor
    ADD CONSTRAINT ref_sensor_pkey PRIMARY KEY (id);


--
-- Name: sensor_coating_config sensor_coating_config_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor_coating_config
    ADD CONSTRAINT sensor_coating_config_pkey PRIMARY KEY (id);


--
-- Name: sensor_location sensor_location_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor_location
    ADD CONSTRAINT sensor_location_pkey PRIMARY KEY (id);


--
-- Name: sensor sensor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor
    ADD CONSTRAINT sensor_pkey PRIMARY KEY (id);


--
-- Name: software software_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.software
    ADD CONSTRAINT software_pkey PRIMARY KEY (id);


--
-- Name: software_value software_value_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.software_value
    ADD CONSTRAINT software_value_pkey PRIMARY KEY (id);


--
-- Name: software_value_software software_value_software_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.software_value_software
    ADD CONSTRAINT software_value_software_pkey PRIMARY KEY (id);


--
-- Name: tank_configuration tank_configuration_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tank_configuration
    ADD CONSTRAINT tank_configuration_pkey PRIMARY KEY (id);


--
-- Name: tank_configuration tank_configuration_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tank_configuration
    ADD CONSTRAINT tank_configuration_ref_key UNIQUE (ref);


--
-- Name: tank tank_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tank
    ADD CONSTRAINT tank_pkey PRIMARY KEY (id);


--
-- Name: test_mean test_mean_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_mean
    ADD CONSTRAINT test_mean_pkey PRIMARY KEY (id);


--
-- Name: test_mean test_mean_type_name_number_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_mean
    ADD CONSTRAINT test_mean_type_name_number_key UNIQUE (type, name, number);


--
-- Name: test test_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_pkey PRIMARY KEY (id);


--
-- Name: test_point test_point_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_point
    ADD CONSTRAINT test_point_pkey PRIMARY KEY (id);


--
-- Name: test_point_value test_point_value_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_point_value
    ADD CONSTRAINT test_point_value_pkey PRIMARY KEY (id);


--
-- Name: test_team test_team_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_team
    ADD CONSTRAINT test_team_pkey PRIMARY KEY (id);


--
-- Name: test_team test_team_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_team
    ADD CONSTRAINT test_team_ref_key UNIQUE (ref);


--
-- Name: type_camera type_camera_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_camera
    ADD CONSTRAINT type_camera_pkey PRIMARY KEY (id);


--
-- Name: type_camera type_camera_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_camera
    ADD CONSTRAINT type_camera_ref_key UNIQUE (ref);


--
-- Name: type_coating type_coating_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_coating
    ADD CONSTRAINT type_coating_pkey PRIMARY KEY (id);


--
-- Name: type_coating type_coating_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_coating
    ADD CONSTRAINT type_coating_ref_key UNIQUE (ref);


--
-- Name: type_detergent type_detergent_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_detergent
    ADD CONSTRAINT type_detergent_pkey PRIMARY KEY (id);


--
-- Name: type_detergent type_detergent_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_detergent
    ADD CONSTRAINT type_detergent_ref_key UNIQUE (ref);


--
-- Name: type_document type_document_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_document
    ADD CONSTRAINT type_document_pkey PRIMARY KEY (id);


--
-- Name: type_document type_document_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_document
    ADD CONSTRAINT type_document_ref_key UNIQUE (ref);


--
-- Name: type_ejector type_ejector_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_ejector
    ADD CONSTRAINT type_ejector_pkey PRIMARY KEY (id);


--
-- Name: type_ejector type_ejector_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_ejector
    ADD CONSTRAINT type_ejector_ref_key UNIQUE (ref);


--
-- Name: type_intrinsic_value type_intrinsic_value_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_intrinsic_value
    ADD CONSTRAINT type_intrinsic_value_pkey PRIMARY KEY (id);


--
-- Name: type_intrinsic_value type_intrinsic_value_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_intrinsic_value
    ADD CONSTRAINT type_intrinsic_value_ref_key UNIQUE (ref);


--
-- Name: type_param type_param_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_param
    ADD CONSTRAINT type_param_pkey PRIMARY KEY (id);


--
-- Name: type_param_sensor type_param_sensor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_param_sensor
    ADD CONSTRAINT type_param_sensor_pkey PRIMARY KEY (id);


--
-- Name: type_param_test_mean type_param_test_mean_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_param_test_mean
    ADD CONSTRAINT type_param_test_mean_pkey PRIMARY KEY (id);


--
-- Name: type_role type_role_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_role
    ADD CONSTRAINT type_role_pkey PRIMARY KEY (id);


--
-- Name: type_role type_role_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_role
    ADD CONSTRAINT type_role_ref_key UNIQUE (ref);


--
-- Name: type_sensor type_sensor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_sensor
    ADD CONSTRAINT type_sensor_pkey PRIMARY KEY (id);


--
-- Name: type_sensor type_sensor_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_sensor
    ADD CONSTRAINT type_sensor_ref_key UNIQUE (ref);


--
-- Name: type_tank type_tank_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_tank
    ADD CONSTRAINT type_tank_pkey PRIMARY KEY (id);


--
-- Name: type_tank type_tank_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_tank
    ADD CONSTRAINT type_tank_ref_key UNIQUE (ref);


--
-- Name: type_test_point type_test_point_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_test_point
    ADD CONSTRAINT type_test_point_pkey PRIMARY KEY (id);


--
-- Name: type_test_point type_test_point_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_test_point
    ADD CONSTRAINT type_test_point_ref_key UNIQUE (ref);


--
-- Name: type_unity type_unity_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_unity
    ADD CONSTRAINT type_unity_pkey PRIMARY KEY (id);


--
-- Name: type_unity type_unity_ref_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_unity
    ADD CONSTRAINT type_unity_ref_key UNIQUE (ref);


--
-- Name: user_right user_right_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_pkey PRIMARY KEY (id);


--
-- Name: velocity_speed velocity_speed_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.velocity_speed
    ADD CONSTRAINT velocity_speed_pkey PRIMARY KEY (id);


--
-- Name: attribute_coating attribute_coating_id_attribute_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_coating
    ADD CONSTRAINT attribute_coating_id_attribute_fkey FOREIGN KEY (id_attribute) REFERENCES public.attribute(id);


--
-- Name: attribute_coating attribute_coating_id_coating_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_coating
    ADD CONSTRAINT attribute_coating_id_coating_fkey FOREIGN KEY (id_coating) REFERENCES public.coating(id);


--
-- Name: attribute_detergent attribute_detergent_id_attribute_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_detergent
    ADD CONSTRAINT attribute_detergent_id_attribute_fkey FOREIGN KEY (id_attribute) REFERENCES public.attribute(id);


--
-- Name: attribute_detergent attribute_detergent_id_detergent_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_detergent
    ADD CONSTRAINT attribute_detergent_id_detergent_fkey FOREIGN KEY (id_detergent) REFERENCES public.detergent(id);


--
-- Name: attribute attribute_id_unity_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute
    ADD CONSTRAINT attribute_id_unity_fkey FOREIGN KEY (id_unity) REFERENCES public.type_unity(id);


--
-- Name: attribute_test_mean attribute_test_mean_id_attribute_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_test_mean
    ADD CONSTRAINT attribute_test_mean_id_attribute_fkey FOREIGN KEY (id_attribute) REFERENCES public.attribute(id);


--
-- Name: attribute_test_mean attribute_test_mean_id_test_mean_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.attribute_test_mean
    ADD CONSTRAINT attribute_test_mean_id_test_mean_fkey FOREIGN KEY (id_test_mean) REFERENCES public.test_mean(id);


--
-- Name: calibration calibration_id_sensor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.calibration
    ADD CONSTRAINT calibration_id_sensor_fkey FOREIGN KEY (id_sensor) REFERENCES public.sensor(id);


--
-- Name: calibration calibration_id_type_param_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.calibration
    ADD CONSTRAINT calibration_id_type_param_fkey FOREIGN KEY (id_type_param) REFERENCES public.type_param(id);


--
-- Name: calibration calibration_id_type_versus_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.calibration
    ADD CONSTRAINT calibration_id_type_versus_fkey FOREIGN KEY (id_type_versus) REFERENCES public.type_param(id);


--
-- Name: camera camera_id_type_camera_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.camera
    ADD CONSTRAINT camera_id_type_camera_fkey FOREIGN KEY (id_type_camera) REFERENCES public.type_camera(id);


--
-- Name: camera_in_config camera_in_config_id_config_camera_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.camera_in_config
    ADD CONSTRAINT camera_in_config_id_config_camera_fkey FOREIGN KEY (id_config_camera) REFERENCES public.config_camera(id);


--
-- Name: camera_in_config camera_in_config_id_test_mean_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.camera_in_config
    ADD CONSTRAINT camera_in_config_id_test_mean_fkey FOREIGN KEY (id_test_mean) REFERENCES public.test_mean(id);


--
-- Name: coating coating_id_type_coating_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coating
    ADD CONSTRAINT coating_id_type_coating_fkey FOREIGN KEY (id_type_coating) REFERENCES public.type_coating(id);


--
-- Name: coating_location coating_location_id_coating_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.coating_location
    ADD CONSTRAINT coating_location_id_coating_fkey FOREIGN KEY (id_coating) REFERENCES public.coating(id);


--
-- Name: cond_init cond_init_id_airfield_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cond_init
    ADD CONSTRAINT cond_init_id_airfield_fkey FOREIGN KEY (id_airfield) REFERENCES public.airfield(id);


--
-- Name: config_camera config_camera_type_camera_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.config_camera
    ADD CONSTRAINT config_camera_type_camera_fkey FOREIGN KEY (type_camera) REFERENCES public.camera(id);


--
-- Name: config_on_acqui config_on_acqui_id_acquisition_config_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.config_on_acqui
    ADD CONSTRAINT config_on_acqui_id_acquisition_config_fkey FOREIGN KEY (id_acquisition_config) REFERENCES public.acquisition_config(id);


--
-- Name: config_on_acqui config_on_acqui_id_hardware_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.config_on_acqui
    ADD CONSTRAINT config_on_acqui_id_hardware_fkey FOREIGN KEY (id_hardware) REFERENCES public.hardware(id);


--
-- Name: config_on_acqui config_on_acqui_id_software_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.config_on_acqui
    ADD CONSTRAINT config_on_acqui_id_software_fkey FOREIGN KEY (id_software) REFERENCES public.software(id);


--
-- Name: config_on_acqui config_on_acqui_id_software_value_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.config_on_acqui
    ADD CONSTRAINT config_on_acqui_id_software_value_fkey FOREIGN KEY (id_software_value) REFERENCES public.software_value(id);


--
-- Name: data_sensor data_sensor_id_sensor_coating_config_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_sensor
    ADD CONSTRAINT data_sensor_id_sensor_coating_config_fkey FOREIGN KEY (id_sensor_coating_config) REFERENCES public.sensor_coating_config(id);


--
-- Name: data_sensor data_sensor_id_test_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_sensor
    ADD CONSTRAINT data_sensor_id_test_fkey FOREIGN KEY (id_test) REFERENCES public.test(id);


--
-- Name: data_sensor data_sensor_id_type_param_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_sensor
    ADD CONSTRAINT data_sensor_id_type_param_fkey FOREIGN KEY (id_type_param) REFERENCES public.type_param(id);


--
-- Name: data_vol data_vol_id_test_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_vol
    ADD CONSTRAINT data_vol_id_test_fkey FOREIGN KEY (id_test) REFERENCES public.test(id);


--
-- Name: data_vol data_vol_id_type_param_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.data_vol
    ADD CONSTRAINT data_vol_id_type_param_fkey FOREIGN KEY (id_type_param) REFERENCES public.type_param(id);


--
-- Name: def_test_point def_test_point_id_type_test_point_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.def_test_point
    ADD CONSTRAINT def_test_point_id_type_test_point_fkey FOREIGN KEY (id_type_test_point) REFERENCES public.type_test_point(id);


--
-- Name: detergent detergent_id_type_detergent_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detergent
    ADD CONSTRAINT detergent_id_type_detergent_fkey FOREIGN KEY (id_type_detergent) REFERENCES public.type_detergent(id);


--
-- Name: document_test document_test_id_document_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.document_test
    ADD CONSTRAINT document_test_id_document_fkey FOREIGN KEY (id_document) REFERENCES public.document(id);


--
-- Name: document_test document_test_id_test_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.document_test
    ADD CONSTRAINT document_test_id_test_fkey FOREIGN KEY (id_test) REFERENCES public.test(id);


--
-- Name: document document_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.document
    ADD CONSTRAINT document_type_fkey FOREIGN KEY (type) REFERENCES public.type_document(id);


--
-- Name: ejector_config ejector_config_type_ejector_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ejector_config
    ADD CONSTRAINT ejector_config_type_ejector_fkey FOREIGN KEY (type_ejector) REFERENCES public.ejector(id);


--
-- Name: ejector ejector_id_type_ejector_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ejector
    ADD CONSTRAINT ejector_id_type_ejector_fkey FOREIGN KEY (id_type_ejector) REFERENCES public.type_ejector(id);


--
-- Name: ejector_in_config ejector_in_config_id_ejector_config_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ejector_in_config
    ADD CONSTRAINT ejector_in_config_id_ejector_config_fkey FOREIGN KEY (id_ejector_config) REFERENCES public.ejector_config(id);


--
-- Name: hardware_software hardware_software_id_hardware_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hardware_software
    ADD CONSTRAINT hardware_software_id_hardware_fkey FOREIGN KEY (id_hardware) REFERENCES public.hardware(id);


--
-- Name: hardware_software hardware_software_id_software_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hardware_software
    ADD CONSTRAINT hardware_software_id_software_fkey FOREIGN KEY (id_software) REFERENCES public.software(id);


--
-- Name: insect_in_cond_init insect_in_cond_init_id_cond_init_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.insect_in_cond_init
    ADD CONSTRAINT insect_in_cond_init_id_cond_init_fkey FOREIGN KEY (id_cond_init) REFERENCES public.cond_init(id);


--
-- Name: insect_in_cond_init insect_in_cond_init_id_insect_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.insect_in_cond_init
    ADD CONSTRAINT insect_in_cond_init_id_insect_fkey FOREIGN KEY (id_insect) REFERENCES public.insect(id);


--
-- Name: intrinsic_value intrinsic_value_id_test_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.intrinsic_value
    ADD CONSTRAINT intrinsic_value_id_test_fkey FOREIGN KEY (id_test) REFERENCES public.test(id);


--
-- Name: intrinsic_value intrinsic_value_id_type_intrinsic_value_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.intrinsic_value
    ADD CONSTRAINT intrinsic_value_id_type_intrinsic_value_fkey FOREIGN KEY (id_type_intrinsic_value) REFERENCES public.type_intrinsic_value(id);


--
-- Name: intrinsic_value_value intrinsic_value_value_id_intrinsic_value_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.intrinsic_value_value
    ADD CONSTRAINT intrinsic_value_value_id_intrinsic_value_fkey FOREIGN KEY (id_intrinsic_value) REFERENCES public.intrinsic_value(id);


--
-- Name: intrinsic_value_value intrinsic_value_value_id_type_param_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.intrinsic_value_value
    ADD CONSTRAINT intrinsic_value_value_id_type_param_fkey FOREIGN KEY (id_type_param) REFERENCES public.type_param(id);


--
-- Name: param_intrinsic_value param_intrinsic_value_id_type_intrinsic_value_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.param_intrinsic_value
    ADD CONSTRAINT param_intrinsic_value_id_type_intrinsic_value_fkey FOREIGN KEY (id_type_intrinsic_value) REFERENCES public.type_intrinsic_value(id);


--
-- Name: param_intrinsic_value param_intrinsic_value_id_type_param_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.param_intrinsic_value
    ADD CONSTRAINT param_intrinsic_value_id_type_param_fkey FOREIGN KEY (id_type_param) REFERENCES public.type_param(id);


--
-- Name: param_test_point param_test_point_id_type_param_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.param_test_point
    ADD CONSTRAINT param_test_point_id_type_param_fkey FOREIGN KEY (id_type_param) REFERENCES public.type_param(id);


--
-- Name: param_test_point param_test_point_id_type_test_point_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.param_test_point
    ADD CONSTRAINT param_test_point_id_type_test_point_fkey FOREIGN KEY (id_type_test_point) REFERENCES public.type_test_point(id);


--
-- Name: photo photo_id_test_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.photo
    ADD CONSTRAINT photo_id_test_fkey FOREIGN KEY (id_test) REFERENCES public.test(id);


--
-- Name: position_on_tank position_on_tank_id_tank_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.position_on_tank
    ADD CONSTRAINT position_on_tank_id_tank_fkey FOREIGN KEY (id_tank) REFERENCES public.tank(id);


--
-- Name: quantite quantite_id_cond_init_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quantite
    ADD CONSTRAINT quantite_id_cond_init_fkey FOREIGN KEY (id_cond_init) REFERENCES public.cond_init(id);


--
-- Name: quantite quantite_id_ejector_in_config_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quantite
    ADD CONSTRAINT quantite_id_ejector_in_config_fkey FOREIGN KEY (id_ejector_in_config) REFERENCES public.ejector_in_config(id);


--
-- Name: quantite quantite_id_insect_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.quantite
    ADD CONSTRAINT quantite_id_insect_fkey FOREIGN KEY (id_insect) REFERENCES public.insect(id);


--
-- Name: ref_sensor ref_sensor_id_type_sensor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ref_sensor
    ADD CONSTRAINT ref_sensor_id_type_sensor_fkey FOREIGN KEY (id_type_sensor) REFERENCES public.type_sensor(id);


--
-- Name: sensor_coating_config sensor_coating_config_id_coating_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor_coating_config
    ADD CONSTRAINT sensor_coating_config_id_coating_fkey FOREIGN KEY (id_coating) REFERENCES public.coating(id);


--
-- Name: sensor_coating_config sensor_coating_config_id_position_on_tank_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor_coating_config
    ADD CONSTRAINT sensor_coating_config_id_position_on_tank_fkey FOREIGN KEY (id_position_on_tank) REFERENCES public.position_on_tank(id);


--
-- Name: sensor_coating_config sensor_coating_config_id_sensor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor_coating_config
    ADD CONSTRAINT sensor_coating_config_id_sensor_fkey FOREIGN KEY (id_sensor) REFERENCES public.sensor(id);


--
-- Name: sensor_coating_config sensor_coating_config_id_tank_configuration_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor_coating_config
    ADD CONSTRAINT sensor_coating_config_id_tank_configuration_fkey FOREIGN KEY (id_tank_configuration) REFERENCES public.tank_configuration(id);


--
-- Name: sensor sensor_id_ref_sensor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sensor
    ADD CONSTRAINT sensor_id_ref_sensor_fkey FOREIGN KEY (id_ref_sensor) REFERENCES public.ref_sensor(id);


--
-- Name: software_value_software software_value_software_id_software_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.software_value_software
    ADD CONSTRAINT software_value_software_id_software_fkey FOREIGN KEY (id_software) REFERENCES public.software(id);


--
-- Name: software_value_software software_value_software_id_software_value_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.software_value_software
    ADD CONSTRAINT software_value_software_id_software_value_fkey FOREIGN KEY (id_software_value) REFERENCES public.software_value(id);


--
-- Name: tank_configuration tank_configuration_tank_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tank_configuration
    ADD CONSTRAINT tank_configuration_tank_type_fkey FOREIGN KEY (tank_type) REFERENCES public.tank(id);


--
-- Name: tank tank_id_type_tank_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tank
    ADD CONSTRAINT tank_id_type_tank_fkey FOREIGN KEY (id_type_tank) REFERENCES public.type_tank(id);


--
-- Name: test test_id_acqui_conf_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_id_acqui_conf_fkey FOREIGN KEY (id_acqui_conf) REFERENCES public.acquisition_config(id);


--
-- Name: test test_id_camera_conf_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_id_camera_conf_fkey FOREIGN KEY (id_camera_conf) REFERENCES public.config_camera(id);


--
-- Name: test test_id_cond_init_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_id_cond_init_fkey FOREIGN KEY (id_cond_init) REFERENCES public.cond_init(id);


--
-- Name: test test_id_copilot_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_id_copilot_fkey FOREIGN KEY (id_copilot) REFERENCES public.pilot(id);


--
-- Name: test test_id_ejector_conf_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_id_ejector_conf_fkey FOREIGN KEY (id_ejector_conf) REFERENCES public.ejector_config(id);


--
-- Name: test test_id_pilot_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_id_pilot_fkey FOREIGN KEY (id_pilot) REFERENCES public.pilot(id);


--
-- Name: test test_id_tank_conf_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_id_tank_conf_fkey FOREIGN KEY (id_tank_conf) REFERENCES public.tank_configuration(id);


--
-- Name: test test_id_test_driver_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_id_test_driver_fkey FOREIGN KEY (id_test_driver) REFERENCES public.account(id);


--
-- Name: test test_id_test_mean_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_id_test_mean_fkey FOREIGN KEY (id_test_mean) REFERENCES public.test_mean(id);


--
-- Name: test_point test_point_id_test_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_point
    ADD CONSTRAINT test_point_id_test_fkey FOREIGN KEY (id_test) REFERENCES public.test(id);


--
-- Name: test_point test_point_id_type_test_point_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_point
    ADD CONSTRAINT test_point_id_type_test_point_fkey FOREIGN KEY (id_type_test_point) REFERENCES public.type_test_point(id);


--
-- Name: test_point_value test_point_value_id_test_point_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_point_value
    ADD CONSTRAINT test_point_value_id_test_point_fkey FOREIGN KEY (id_test_point) REFERENCES public.test_point(id);


--
-- Name: test_point_value test_point_value_id_type_param_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.test_point_value
    ADD CONSTRAINT test_point_value_id_type_param_fkey FOREIGN KEY (id_type_param) REFERENCES public.type_param(id);


--
-- Name: type_param type_param_id_unity_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_param
    ADD CONSTRAINT type_param_id_unity_fkey FOREIGN KEY (id_unity) REFERENCES public.type_unity(id);


--
-- Name: type_param_sensor type_param_sensor_id_ref_sensor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_param_sensor
    ADD CONSTRAINT type_param_sensor_id_ref_sensor_fkey FOREIGN KEY (id_ref_sensor) REFERENCES public.ref_sensor(id);


--
-- Name: type_param_sensor type_param_sensor_id_type_param_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_param_sensor
    ADD CONSTRAINT type_param_sensor_id_type_param_fkey FOREIGN KEY (id_type_param) REFERENCES public.type_param(id);


--
-- Name: type_param_test_mean type_param_test_mean_id_test_mean_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_param_test_mean
    ADD CONSTRAINT type_param_test_mean_id_test_mean_fkey FOREIGN KEY (id_test_mean) REFERENCES public.test_mean(id);


--
-- Name: type_param_test_mean type_param_test_mean_id_type_param_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.type_param_test_mean
    ADD CONSTRAINT type_param_test_mean_id_type_param_fkey FOREIGN KEY (id_type_param) REFERENCES public.type_param(id);


--
-- Name: user_right user_right_id_account_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_id_account_fkey FOREIGN KEY (id_account) REFERENCES public.account(id) ON DELETE CASCADE;


--
-- Name: user_right user_right_id_test_mean_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_id_test_mean_fkey FOREIGN KEY (id_test_mean) REFERENCES public.test_mean(id);


--
-- Name: user_right user_right_id_test_team_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_id_test_team_fkey FOREIGN KEY (id_test_team) REFERENCES public.test_team(id);


--
-- Name: user_right user_right_id_type_camera_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_id_type_camera_fkey FOREIGN KEY (id_type_camera) REFERENCES public.type_camera(id);


--
-- Name: user_right user_right_id_type_coating_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_id_type_coating_fkey FOREIGN KEY (id_type_coating) REFERENCES public.type_coating(id);


--
-- Name: user_right user_right_id_type_detergent_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_id_type_detergent_fkey FOREIGN KEY (id_type_detergent) REFERENCES public.type_detergent(id);


--
-- Name: user_right user_right_id_type_ejector_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_id_type_ejector_fkey FOREIGN KEY (id_type_ejector) REFERENCES public.type_ejector(id);


--
-- Name: user_right user_right_id_type_intrinsic_value_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_id_type_intrinsic_value_fkey FOREIGN KEY (id_type_intrinsic_value) REFERENCES public.type_intrinsic_value(id);


--
-- Name: user_right user_right_id_type_sensor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_id_type_sensor_fkey FOREIGN KEY (id_type_sensor) REFERENCES public.type_sensor(id);


--
-- Name: user_right user_right_id_type_tank_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_id_type_tank_fkey FOREIGN KEY (id_type_tank) REFERENCES public.type_tank(id);


--
-- Name: user_right user_right_id_type_test_point_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_id_type_test_point_fkey FOREIGN KEY (id_type_test_point) REFERENCES public.type_test_point(id);


--
-- Name: user_right user_right_role_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_right
    ADD CONSTRAINT user_right_role_fkey FOREIGN KEY (role) REFERENCES public.type_role(id);


--
-- Name: velocity_speed velocity_speed_id_cond_init_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.velocity_speed
    ADD CONSTRAINT velocity_speed_id_cond_init_fkey FOREIGN KEY (id_cond_init) REFERENCES public.cond_init(id);


--
-- Name: velocity_speed velocity_speed_id_ejector_in_config_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.velocity_speed
    ADD CONSTRAINT velocity_speed_id_ejector_in_config_fkey FOREIGN KEY (id_ejector_in_config) REFERENCES public.ejector_in_config(id);


--
-- PostgreSQL database dump complete
--

