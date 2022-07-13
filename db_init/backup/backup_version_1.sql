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
    date timestamp with time zone,
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
2	Paris	Louvre	0
3	Shanghai	Bund	10
4			\N
1	Aix	Ron	1300
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
16	Aspirine	3	111
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
14	10	16
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
10	1	xxx	f
\.


--
-- Data for Name: coating_location; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.coating_location (id, id_coating, "order", location, date, validation) FROM stdin;
1	1	order	in config	2022-06-24 10:16:37.087682+02	t
2	3	order	in config	2022-06-24 10:16:37.087682+02	t
\.


--
-- Data for Name: cond_init; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cond_init (id, cond_init, id_airfield) FROM stdin;
2	["", "", "", "", "", "", "", ""]	4
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
177719	1	13	13	06:35:16.878	100193.36	t
177720	1	13	13	06:35:17.869	100191.51	t
177721	1	13	13	06:35:18.857	100192.36	t
177722	1	13	13	06:35:19.841	100190.52	t
177723	1	13	13	06:35:20.832	100191.37	t
177724	1	13	13	06:35:21.819	100186.97	t
177725	1	13	13	06:35:22.807	100190.52	t
177726	1	13	13	06:35:23.792	100192.36	t
177727	1	13	13	06:35:24.783	100186.97	t
177728	1	13	13	06:35:25.769	100192.36	t
177729	1	13	13	06:35:26.759	100191.37	t
177730	1	13	13	06:35:27.75	100187.82	t
177731	1	13	13	06:35:28.74	100190.52	t
177732	1	13	13	06:35:29.733	100199.46	t
177733	1	13	13	06:35:30.722	100197.61	t
177734	1	13	14	06:35:16.878	19.4	t
177735	1	13	14	06:35:17.869	19.41	t
177736	1	13	14	06:35:18.857	19.41	t
177737	1	13	14	06:35:19.841	19.42	t
177738	1	13	14	06:35:20.832	19.42	t
177739	1	13	14	06:35:21.819	19.41	t
177740	1	13	14	06:35:22.807	19.42	t
177741	1	13	14	06:35:23.792	19.41	t
177742	1	13	14	06:35:24.783	19.41	t
177743	1	13	14	06:35:25.769	19.41	t
177744	1	13	14	06:35:26.759	19.42	t
177745	1	13	14	06:35:27.75	19.42	t
177746	1	13	14	06:35:28.74	19.42	t
177747	1	13	14	06:35:29.733	19.42	t
177748	1	13	14	06:35:30.722	19.43	t
177749	1	13	15	06:35:16.878	49.51	t
177750	1	13	15	06:35:17.869	49.54	t
177751	1	13	15	06:35:18.857	49.14	t
177752	1	13	15	06:35:19.841	49.14	t
177753	1	13	15	06:35:20.832	49.08	t
177754	1	13	15	06:35:21.819	49.16	t
177755	1	13	15	06:35:22.807	49.53	t
177756	1	13	15	06:35:23.792	49.46	t
177757	1	13	15	06:35:24.783	49.44	t
177758	1	13	15	06:35:25.769	49.41	t
177759	1	13	15	06:35:26.759	49.31	t
177760	1	13	15	06:35:27.75	49.49	t
177761	1	13	15	06:35:28.74	49.26	t
177762	1	13	15	06:35:29.733	49.42	t
177763	1	13	15	06:35:30.722	49.24	t
177764	1	14	13	06:35:16.878	100113.85	t
177765	1	14	13	06:35:17.869	100111.17	t
177766	1	14	13	06:35:18.857	100107.49	t
177767	1	14	13	06:35:19.841	100117.23	t
177768	1	14	13	06:35:20.832	100115.52	t
177769	1	14	13	06:35:21.819	100116.38	t
177770	1	14	13	06:35:22.807	100114.55	t
177771	1	14	13	06:35:23.792	100117.23	t
177772	1	14	13	06:35:24.783	100113.7	t
177773	1	14	13	06:35:25.769	100109.2	t
177774	1	14	13	06:35:26.759	100113.7	t
177775	1	14	13	06:35:27.75	100114.55	t
177776	1	14	13	06:35:28.74	100111.88	t
177777	1	14	13	06:35:29.733	100114.55	t
177778	1	14	13	06:35:30.722	100117.23	t
177779	1	14	14	06:35:16.878	19.51	t
177780	1	14	14	06:35:17.869	19.51	t
177781	1	14	14	06:35:18.857	19.52	t
177782	1	14	14	06:35:19.841	19.53	t
177783	1	14	14	06:35:20.832	19.52	t
177784	1	14	14	06:35:21.819	19.53	t
177785	1	14	14	06:35:22.807	19.53	t
177786	1	14	14	06:35:23.792	19.53	t
177787	1	14	14	06:35:24.783	19.53	t
177788	1	14	14	06:35:25.769	19.53	t
177789	1	14	14	06:35:26.759	19.53	t
177790	1	14	14	06:35:27.75	19.53	t
177791	1	14	14	06:35:28.74	19.53	t
177792	1	14	14	06:35:29.733	19.53	t
177793	1	14	14	06:35:30.722	19.53	t
177794	1	14	15	06:35:16.878	49.27	t
177795	1	14	15	06:35:17.869	49.36	t
177796	1	14	15	06:35:18.857	49.34	t
177797	1	14	15	06:35:19.841	49.35	t
177798	1	14	15	06:35:20.832	49.49	t
177799	1	14	15	06:35:21.819	49.39	t
177800	1	14	15	06:35:22.807	49.28	t
177801	1	14	15	06:35:23.792	49.18	t
177802	1	14	15	06:35:24.783	49.21	t
177803	1	14	15	06:35:25.769	49.4	t
177804	1	14	15	06:35:26.759	49.14	t
177805	1	14	15	06:35:27.75	49.23	t
177806	1	14	15	06:35:28.74	49.28	t
177807	1	14	15	06:35:29.733	49.19	t
177808	1	14	15	06:35:30.722	49.11	t
177809	1	18	13	06:35:16.878	100133.82	t
177810	1	18	13	06:35:17.869	100130.08	t
177811	1	18	13	06:35:18.857	100134.48	t
177812	1	18	13	06:35:19.841	100135.32	t
177813	1	18	13	06:35:20.832	100131.78	t
177814	1	18	13	06:35:21.819	100128.23	t
177815	1	18	13	06:35:22.807	100132.63	t
177816	1	18	13	06:35:23.792	100134.48	t
177817	1	18	13	06:35:24.783	100134.48	t
177818	1	18	13	06:35:25.769	100129.93	t
177819	1	18	13	06:35:26.759	100123.68	t
177820	1	18	13	06:35:27.75	100132.63	t
177821	1	18	13	06:35:28.74	100136.17	t
177822	1	18	13	06:35:29.733	100129.93	t
177823	1	18	13	06:35:30.722	100130.78	t
177824	1	18	14	06:35:16.878	19.74	t
177825	1	18	14	06:35:17.869	19.75	t
177826	1	18	14	06:35:18.857	19.76	t
177827	1	18	14	06:35:19.841	19.76	t
177828	1	18	14	06:35:20.832	19.76	t
177829	1	18	14	06:35:21.819	19.75	t
177830	1	18	14	06:35:22.807	19.76	t
177831	1	18	14	06:35:23.792	19.76	t
177832	1	18	14	06:35:24.783	19.76	t
177833	1	18	14	06:35:25.769	19.76	t
177834	1	18	14	06:35:26.759	19.76	t
177835	1	18	14	06:35:27.75	19.76	t
177836	1	18	14	06:35:28.74	19.77	t
177837	1	18	14	06:35:29.733	19.76	t
177838	1	18	14	06:35:30.722	19.77	t
177839	1	18	15	06:35:16.878	48.75	t
177840	1	18	15	06:35:17.869	48.39	t
177841	1	18	15	06:35:18.857	48.49	t
177842	1	18	15	06:35:19.841	48.45	t
177843	1	18	15	06:35:20.832	48.44	t
177844	1	18	15	06:35:21.819	48.63	t
177845	1	18	15	06:35:22.807	48.63	t
177846	1	18	15	06:35:23.792	48.52	t
177847	1	18	15	06:35:24.783	48.6	t
177848	1	18	15	06:35:25.769	48.59	t
177849	1	18	15	06:35:26.759	48.59	t
177850	1	18	15	06:35:27.75	48.45	t
177851	1	18	15	06:35:28.74	48.66	t
177852	1	18	15	06:35:29.733	48.55	t
177853	1	18	15	06:35:30.722	48.59	t
177854	1	19	13	06:35:16.878	100164.97	t
177855	1	19	13	06:35:17.869	100161.32	t
177856	1	19	13	06:35:18.857	100162.23	t
177857	1	19	13	06:35:19.841	100161.32	t
177858	1	19	13	06:35:20.832	100167.64	t
177859	1	19	13	06:35:21.819	100160.41	t
177860	1	19	13	06:35:22.807	100159.46	t
177861	1	19	13	06:35:23.792	100156.82	t
177862	1	19	13	06:35:24.783	100162.23	t
177863	1	19	13	06:35:25.769	100160.41	t
177864	1	19	13	06:35:26.759	100158.58	t
177865	1	19	13	06:35:27.75	100160.41	t
177866	1	19	13	06:35:28.74	100160.41	t
177867	1	19	13	06:35:29.733	100163.11	t
177868	1	19	13	06:35:30.722	100159.46	t
177869	1	19	14	06:35:16.878	19.53	t
177870	1	19	14	06:35:17.869	19.54	t
177871	1	19	14	06:35:18.857	19.55	t
177872	1	19	14	06:35:19.841	19.54	t
177873	1	19	14	06:35:20.832	19.55	t
177874	1	19	14	06:35:21.819	19.55	t
177875	1	19	14	06:35:22.807	19.56	t
177876	1	19	14	06:35:23.792	19.55	t
177877	1	19	14	06:35:24.783	19.55	t
177878	1	19	14	06:35:25.769	19.55	t
177879	1	19	14	06:35:26.759	19.56	t
177880	1	19	14	06:35:27.75	19.55	t
177881	1	19	14	06:35:28.74	19.55	t
177882	1	19	14	06:35:29.733	19.55	t
177883	1	19	14	06:35:30.722	19.56	t
177884	1	19	15	06:35:16.878	48.46	t
177885	1	19	15	06:35:17.869	48.66	t
177886	1	19	15	06:35:18.857	48.66	t
177887	1	19	15	06:35:19.841	48.68	t
177888	1	19	15	06:35:20.832	48.46	t
177889	1	19	15	06:35:21.819	48.68	t
177890	1	19	15	06:35:22.807	48.7	t
177891	1	19	15	06:35:23.792	48.71	t
177892	1	19	15	06:35:24.783	48.5	t
177893	1	19	15	06:35:25.769	48.71	t
177894	1	19	15	06:35:26.759	48.66	t
177895	1	19	15	06:35:27.75	48.69	t
177896	1	19	15	06:35:28.74	48.67	t
177897	1	19	15	06:35:29.733	48.5	t
177898	1	19	15	06:35:30.722	48.71	t
177899	1	20	13	06:35:16.878	100167.67	t
177900	1	20	13	06:35:17.869	100171.22	t
177901	1	20	13	06:35:18.857	100175.6	t
177902	1	20	13	06:35:19.841	100170.2	t
177903	1	20	13	06:35:20.832	100174.78	t
177904	1	20	13	06:35:21.819	100170.2	t
177905	1	20	13	06:35:22.807	100164.81	t
177906	1	20	13	06:35:23.792	100172.08	t
177907	1	20	13	06:35:24.783	100167.5	t
177908	1	20	13	06:35:25.769	100171.06	t
177909	1	20	13	06:35:26.759	100174.61	t
177910	1	20	13	06:35:27.75	100162.96	t
177911	1	20	13	06:35:28.74	100171.22	t
177912	1	20	13	06:35:29.733	100164.81	t
177913	1	20	13	06:35:30.722	100171.22	t
177914	1	20	14	06:35:16.878	19.56	t
177915	1	20	14	06:35:17.869	19.57	t
177916	1	20	14	06:35:18.857	19.58	t
177917	1	20	14	06:35:19.841	19.58	t
177918	1	20	14	06:35:20.832	19.57	t
177919	1	20	14	06:35:21.819	19.58	t
177920	1	20	14	06:35:22.807	19.58	t
177921	1	20	14	06:35:23.792	19.57	t
177922	1	20	14	06:35:24.783	19.58	t
177923	1	20	14	06:35:25.769	19.58	t
177924	1	20	14	06:35:26.759	19.59	t
177925	1	20	14	06:35:27.75	19.58	t
177926	1	20	14	06:35:28.74	19.57	t
177927	1	20	14	06:35:29.733	19.58	t
177928	1	20	14	06:35:30.722	19.57	t
177929	1	20	15	06:35:16.878	40.16	t
177930	1	20	15	06:35:17.869	40.15	t
177931	1	20	15	06:35:18.857	40.15	t
177932	1	20	15	06:35:19.841	40.15	t
177933	1	20	15	06:35:20.832	40.14	t
177934	1	20	15	06:35:21.819	40.14	t
177935	1	20	15	06:35:22.807	40.13	t
177936	1	20	15	06:35:23.792	40.14	t
177937	1	20	15	06:35:24.783	40.13	t
177938	1	20	15	06:35:25.769	40.14	t
177939	1	20	15	06:35:26.759	40.13	t
177940	1	20	15	06:35:27.75	40.12	t
177941	1	20	15	06:35:28.74	40.13	t
177942	1	20	15	06:35:29.733	40.12	t
177943	1	20	15	06:35:30.722	40.13	t
177944	1	21	13	06:35:16.878	100187.74	t
177945	1	21	13	06:35:17.869	100191.27	t
177946	1	21	13	06:35:18.857	100185.89	t
177947	1	21	13	06:35:19.841	100193.96	t
177948	1	21	13	06:35:20.832	100192.24	t
177949	1	21	13	06:35:21.819	100193.11	t
177950	1	21	13	06:35:22.807	100193.96	t
177951	1	21	13	06:35:23.792	100185.89	t
177952	1	21	13	06:35:24.783	100193.11	t
177953	1	21	13	06:35:25.769	100194.8	t
177954	1	21	13	06:35:26.759	100193.11	t
177955	1	21	13	06:35:27.75	100194.8	t
177956	1	21	13	06:35:28.74	100193.96	t
177957	1	21	13	06:35:29.733	100189.42	t
177958	1	21	13	06:35:30.722	100191.27	t
177959	1	21	14	06:35:16.878	19.75	t
177960	1	21	14	06:35:17.869	19.76	t
177961	1	21	14	06:35:18.857	19.76	t
177962	1	21	14	06:35:19.841	19.76	t
177963	1	21	14	06:35:20.832	19.75	t
177964	1	21	14	06:35:21.819	19.75	t
177965	1	21	14	06:35:22.807	19.76	t
177966	1	21	14	06:35:23.792	19.76	t
177967	1	21	14	06:35:24.783	19.75	t
177968	1	21	14	06:35:25.769	19.76	t
177969	1	21	14	06:35:26.759	19.75	t
177970	1	21	14	06:35:27.75	19.76	t
177971	1	21	14	06:35:28.74	19.76	t
177972	1	21	14	06:35:29.733	19.76	t
177973	1	21	14	06:35:30.722	19.76	t
177974	1	21	15	06:35:16.878	47.3	t
177975	1	21	15	06:35:17.869	47.31	t
177976	1	21	15	06:35:18.857	47.27	t
177977	1	21	15	06:35:19.841	47.25	t
177978	1	21	15	06:35:20.832	47.22	t
177979	1	21	15	06:35:21.819	47.19	t
177980	1	21	15	06:35:22.807	47.16	t
177981	1	21	15	06:35:23.792	47.13	t
177982	1	21	15	06:35:24.783	47.12	t
177983	1	21	15	06:35:25.769	47.14	t
177984	1	21	15	06:35:26.759	47.12	t
177985	1	21	15	06:35:27.75	47.13	t
177986	1	21	15	06:35:28.74	47.14	t
177987	1	21	15	06:35:29.733	47.14	t
177988	1	21	15	06:35:30.722	47.15	t
177989	1	22	13	06:35:16.878	100179.5	t
177990	1	22	13	06:35:17.869	100181.91	t
177991	1	22	13	06:35:18.857	100172.74	t
177992	1	22	13	06:35:19.841	100178.32	t
177993	1	22	13	06:35:20.832	100175.12	t
177994	1	22	13	06:35:21.819	100170.76	t
177995	1	22	13	06:35:22.807	100170.76	t
177996	1	22	13	06:35:23.792	100173.55	t
177997	1	22	13	06:35:24.783	100177.91	t
177998	1	22	13	06:35:25.769	100172.34	t
177999	1	22	13	06:35:26.759	100178.71	t
178000	1	22	13	06:35:27.75	100179.89	t
178001	1	22	13	06:35:28.74	100172.34	t
178002	1	22	13	06:35:29.733	100169.55	t
178003	1	22	13	06:35:30.722	100174.32	t
178004	1	22	14	06:35:16.878	19.81	t
178005	1	22	14	06:35:17.869	19.82	t
178006	1	22	14	06:35:18.857	19.82	t
178007	1	22	14	06:35:19.841	19.82	t
178008	1	22	14	06:35:20.832	19.83	t
178009	1	22	14	06:35:21.819	19.82	t
178010	1	22	14	06:35:22.807	19.82	t
178011	1	22	14	06:35:23.792	19.82	t
178012	1	22	14	06:35:24.783	19.83	t
178013	1	22	14	06:35:25.769	19.83	t
178014	1	22	14	06:35:26.759	19.84	t
178015	1	22	14	06:35:27.75	19.83	t
178016	1	22	14	06:35:28.74	19.83	t
178017	1	22	14	06:35:29.733	19.83	t
178018	1	22	14	06:35:30.722	19.83	t
178019	1	22	15	06:35:16.878	47.68	t
178020	1	22	15	06:35:17.869	47.69	t
178021	1	22	15	06:35:18.857	47.69	t
178022	1	22	15	06:35:19.841	47.68	t
178023	1	22	15	06:35:20.832	47.68	t
178024	1	22	15	06:35:21.819	47.67	t
178025	1	22	15	06:35:22.807	47.67	t
178026	1	22	15	06:35:23.792	47.68	t
178027	1	22	15	06:35:24.783	47.67	t
178028	1	22	15	06:35:25.769	47.68	t
178029	1	22	15	06:35:26.759	47.67	t
178030	1	22	15	06:35:27.75	47.68	t
178031	1	22	15	06:35:28.74	47.68	t
178032	1	22	15	06:35:29.733	47.69	t
178033	1	22	15	06:35:30.722	47.68	t
178034	1	23	13	06:35:16.878	100185.35	t
178035	1	23	13	06:35:17.869	100188.03	t
178036	1	23	13	06:35:18.857	100178.09	t
178037	1	23	13	06:35:19.841	100183.46	t
178038	1	23	13	06:35:20.832	100178.09	t
178039	1	23	13	06:35:21.819	100183.46	t
178040	1	23	13	06:35:22.807	100182.43	t
178041	1	23	13	06:35:23.792	100186.97	t
178042	1	23	13	06:35:24.783	100186.97	t
178043	1	23	13	06:35:25.769	100188.62	t
178044	1	23	13	06:35:26.759	100189.65	t
178045	1	23	13	06:35:27.75	100178.92	t
178046	1	23	13	06:35:28.74	100187.8	t
178047	1	23	13	06:35:29.733	100191.3	t
178048	1	23	13	06:35:30.722	100185.11	t
178049	1	23	14	06:35:16.878	19.85	t
178050	1	23	14	06:35:17.869	19.85	t
178051	1	23	14	06:35:18.857	19.86	t
178052	1	23	14	06:35:19.841	19.86	t
178053	1	23	14	06:35:20.832	19.86	t
178054	1	23	14	06:35:21.819	19.86	t
178055	1	23	14	06:35:22.807	19.87	t
178056	1	23	14	06:35:23.792	19.86	t
178057	1	23	14	06:35:24.783	19.86	t
178058	1	23	14	06:35:25.769	19.87	t
178059	1	23	14	06:35:26.759	19.86	t
178060	1	23	14	06:35:27.75	19.86	t
178061	1	23	14	06:35:28.74	19.87	t
178062	1	23	14	06:35:29.733	19.87	t
178063	1	23	14	06:35:30.722	19.87	t
178064	1	23	15	06:35:16.878	46.58	t
178065	1	23	15	06:35:17.869	46.6	t
178066	1	23	15	06:35:18.857	46.57	t
178067	1	23	15	06:35:19.841	46.56	t
178068	1	23	15	06:35:20.832	46.55	t
178069	1	23	15	06:35:21.819	46.55	t
178070	1	23	15	06:35:22.807	46.57	t
178071	1	23	15	06:35:23.792	46.56	t
178072	1	23	15	06:35:24.783	46.56	t
178073	1	23	15	06:35:25.769	46.56	t
178074	1	23	15	06:35:26.759	46.57	t
178075	1	23	15	06:35:27.75	46.58	t
178076	1	23	15	06:35:28.74	46.57	t
178077	1	23	15	06:35:29.733	46.57	t
178078	1	23	15	06:35:30.722	46.57	t
178079	1	24	13	06:35:16.878	100183.06	t
178080	1	24	13	06:35:17.869	100180.24	t
178081	1	24	13	06:35:18.857	100183.72	t
178082	1	24	13	06:35:19.841	100181.06	t
178083	1	24	13	06:35:20.832	100181.89	t
178084	1	24	13	06:35:21.819	100187.21	t
178085	1	24	13	06:35:22.807	100181.06	t
178086	1	24	13	06:35:23.792	100181.06	t
178087	1	24	13	06:35:24.783	100182.72	t
178088	1	24	13	06:35:25.769	100181.06	t
178089	1	24	13	06:35:26.759	100190.7	t
178090	1	24	13	06:35:27.75	100189.87	t
178091	1	24	13	06:35:28.74	100185.38	t
178092	1	24	13	06:35:29.733	100181.89	t
178093	1	24	13	06:35:30.722	100182.72	t
178094	1	24	14	06:35:16.878	19.82	t
178095	1	24	14	06:35:17.869	19.84	t
178096	1	24	14	06:35:18.857	19.84	t
178097	1	24	14	06:35:19.841	19.84	t
178098	1	24	14	06:35:20.832	19.85	t
178099	1	24	14	06:35:21.819	19.85	t
178100	1	24	14	06:35:22.807	19.84	t
178101	1	24	14	06:35:23.792	19.84	t
178102	1	24	14	06:35:24.783	19.85	t
178103	1	24	14	06:35:25.769	19.84	t
178104	1	24	14	06:35:26.759	19.85	t
178105	1	24	14	06:35:27.75	19.85	t
178106	1	24	14	06:35:28.74	19.85	t
178107	1	24	14	06:35:29.733	19.85	t
178108	1	24	14	06:35:30.722	19.85	t
178109	1	24	15	06:35:16.878	46.52	t
178110	1	24	15	06:35:17.869	46.52	t
178111	1	24	15	06:35:18.857	46.52	t
178112	1	24	15	06:35:19.841	46.54	t
178113	1	24	15	06:35:20.832	46.51	t
178114	1	24	15	06:35:21.819	46.51	t
178115	1	24	15	06:35:22.807	46.5	t
178116	1	24	15	06:35:23.792	46.51	t
178117	1	24	15	06:35:24.783	46.51	t
178118	1	24	15	06:35:25.769	46.51	t
178119	1	24	15	06:35:26.759	46.52	t
178120	1	24	15	06:35:27.75	46.5	t
178121	1	24	15	06:35:28.74	46.51	t
178122	1	24	15	06:35:29.733	46.52	t
178123	1	24	15	06:35:30.722	46.51	t
178124	1	15	13	06:35:16.878	100145.09	t
178125	1	15	13	06:35:17.869	100144.08	t
178126	1	15	13	06:35:18.857	100144.08	t
178127	1	15	13	06:35:19.841	100143.06	t
178128	1	15	13	06:35:20.832	100145.74	t
178129	1	15	13	06:35:21.819	100151.95	t
178130	1	15	13	06:35:22.807	100145.74	t
178131	1	15	13	06:35:23.792	100140.38	t
178132	1	15	13	06:35:24.783	100144.08	t
178133	1	15	13	06:35:25.769	100141.39	t
178134	1	15	13	06:35:26.759	100145.74	t
178135	1	15	13	06:35:27.75	100143.06	t
178136	1	15	13	06:35:28.74	100142.05	t
178137	1	15	13	06:35:29.733	100144.73	t
178138	1	15	13	06:35:30.722	100139.36	t
178139	1	15	14	06:35:16.878	19.79	t
178140	1	15	14	06:35:17.869	19.8	t
178141	1	15	14	06:35:18.857	19.8	t
178142	1	15	14	06:35:19.841	19.81	t
178143	1	15	14	06:35:20.832	19.81	t
178144	1	15	14	06:35:21.819	19.82	t
178145	1	15	14	06:35:22.807	19.81	t
178146	1	15	14	06:35:23.792	19.81	t
178147	1	15	14	06:35:24.783	19.8	t
178148	1	15	14	06:35:25.769	19.8	t
178149	1	15	14	06:35:26.759	19.81	t
178150	1	15	14	06:35:27.75	19.81	t
178151	1	15	14	06:35:28.74	19.82	t
178152	1	15	14	06:35:29.733	19.82	t
178153	1	15	14	06:35:30.722	19.82	t
178154	1	15	15	06:35:16.878	46.33	t
178155	1	15	15	06:35:17.869	46.33	t
178156	1	15	15	06:35:18.857	46.33	t
178157	1	15	15	06:35:19.841	46.32	t
178158	1	15	15	06:35:20.832	46.3	t
178159	1	15	15	06:35:21.819	46.31	t
178160	1	15	15	06:35:22.807	46.29	t
178161	1	15	15	06:35:23.792	46.29	t
178162	1	15	15	06:35:24.783	46.3	t
178163	1	15	15	06:35:25.769	46.3	t
178164	1	15	15	06:35:26.759	46.31	t
178165	1	15	15	06:35:27.75	46.3	t
178166	1	15	15	06:35:28.74	46.3	t
178167	1	15	15	06:35:29.733	46.31	t
178168	1	15	15	06:35:30.722	46.29	t
178169	1	16	13	06:35:16.878	100175.23	t
178170	1	16	13	06:35:17.869	100176.97	t
178171	1	16	13	06:35:18.857	100174.26	t
178172	1	16	13	06:35:19.841	100173.3	t
178173	1	16	13	06:35:20.832	100176.88	t
178174	1	16	13	06:35:21.819	100178.72	t
178175	1	16	13	06:35:22.807	100174.17	t
178176	1	16	13	06:35:23.792	100175.04	t
178177	1	16	13	06:35:24.783	100177.75	t
178178	1	16	13	06:35:25.769	100178.72	t
178179	1	16	13	06:35:26.759	100176.88	t
178180	1	16	13	06:35:27.75	100174.17	t
178181	1	16	13	06:35:28.74	100173.3	t
178182	1	16	13	06:35:29.733	100169.62	t
178183	1	16	13	06:35:30.722	100177.75	t
178184	1	16	14	06:35:16.878	20.18	t
178185	1	16	14	06:35:17.869	20.19	t
178186	1	16	14	06:35:18.857	20.19	t
178187	1	16	14	06:35:19.841	20.2	t
178188	1	16	14	06:35:20.832	20.2	t
178189	1	16	14	06:35:21.819	20.2	t
178190	1	16	14	06:35:22.807	20.2	t
178191	1	16	14	06:35:23.792	20.21	t
178192	1	16	14	06:35:24.783	20.21	t
178193	1	16	14	06:35:25.769	20.2	t
178194	1	16	14	06:35:26.759	20.2	t
178195	1	16	14	06:35:27.75	20.2	t
178196	1	16	14	06:35:28.74	20.2	t
178197	1	16	14	06:35:29.733	20.21	t
178198	1	16	14	06:35:30.722	20.21	t
178199	1	16	15	06:35:16.878	48.34	t
178200	1	16	15	06:35:17.869	48.32	t
178201	1	16	15	06:35:18.857	48.32	t
178202	1	16	15	06:35:19.841	48.31	t
178203	1	16	15	06:35:20.832	48.3	t
178204	1	16	15	06:35:21.819	48.3	t
178205	1	16	15	06:35:22.807	48.29	t
178206	1	16	15	06:35:23.792	48.32	t
178207	1	16	15	06:35:24.783	48.3	t
178208	1	16	15	06:35:25.769	48.3	t
178209	1	16	15	06:35:26.759	48.3	t
178210	1	16	15	06:35:27.75	48.29	t
178211	1	16	15	06:35:28.74	48.29	t
178212	1	16	15	06:35:29.733	48.29	t
178213	1	16	15	06:35:30.722	48.31	t
\.


--
-- Data for Name: data_vol; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.data_vol (id, id_test, id_type_param, "time", value, validate) FROM stdin;
1	1	1	10:16:37.112264	999	t
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
1	2	99-99	{158.3,1029,100}	{{1.3,2.4,5.5},{11,23,79},{111,222,333}}	Barometric
2	2	100-100	{158.3,119,120}	{{1.3,2.4,7},{11,23,79},{111,222,333}}	Barometric
3	2	101-102	{158.3,1029,100}	{{1.3,2.4,5.5},{11,23,79},{111,222,333}}	Barometric
4	2	102-103	{158.3,119,120}	{{1.3,2.4,7},{11,23,79},{111,222,333}}	Barometric
5	2	999-999	{158.3,119,120}	{{1.3,2.4,7},{11,23,79},{111,222,333}}	Coating
6	2	555-555	{158.3,119,120}	{{1.3,2.4,7},{11,23,79},{111,222,333}}	Accelerometer
7	2	444-444	{158.3,119,120}	{{1.3,2.4,7},{11,23,79},{111,222,333}}	Accelerometer
39	3	0-0	{2436,4,-49}	{{0.945535186276394,0,0.32551990954973},{0,1,0},{0.32551990954973,0,-0.945535186276394}}	Barometric
40	3	0-1	{2481,4,-14}	{{0.357433463675218,1,0.933938605608065},{0,1,0},{0.933938605608065,0,-0.357433463675218}}	Barometric
41	3	0-2	{2483,4,3.7}	{{-0.147483612534009,2,0.989064499430608},{0,1,0},{0.989064499430608,0,0.147483612534009}}	Barometric
42	3	0-3	{2481,4,14}	{{-0.415508705876326,3,0.909589201420609},{0,1,0},{0.909589201420609,0,0.415508705876326}}	Barometric
43	3	0-4	{2475.8,4,23}	{{-0.589537583490262,4,0.807740947118853},{0,1,0},{0.807740947118853,0,0.589537583490262}}	Barometric
44	3	0-5	{2470,4,31}	{{-0.675226947737502,5,0.737610038603798},{0,1,0},{0.737610038603798,0,0.675226947737502}}	Barometric
45	3	0-6	{2462,4,38}	{{-0.763463846138858,6,0.645850567576481},{0,1,0},{0.645850567576481,0,0.763463846138858}}	Barometric
46	3	0-7	{2454,4,45}	{{-0.858238276023236,7,0.513251460366811},{0,1,0},{0.513251460366811,0,0.858238276023236}}	Barometric
47	3	0-8	{2445,4,51.5}	{{-0.85220124087634,8,0.523214148364535},{0,1,0},{0.523214148364535,0,0.85220124087634}}	Barometric
48	3	0-9	{2436,4,57}	{{-0.868983421255946,9,0.494841200368675},{0,1,0},{0.494841200368675,0,0.868983421255946}}	Barometric
49	3	0-10	{2427,4,62}	{{-0.898048507369272,10,0.439896440553708},{0,1,0},{0.439896440553708,0,0.898048507369272}}	Barometric
50	3	0-11	{2410,4,72}	{{-0.915219523626268,11,0.402955609929067},{0,1,0},{0.402955609929067,0,-0.915219523626268}}	Barometric
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
1	1	LIS3DH
2	2	AccS1
3	2	AccS2
4	2	AccS3
\.


--
-- Data for Name: sensor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sensor (id, id_ref_sensor, number, validate) FROM stdin;
1	1	001	t
2	1	002	t
3	2	0942H	t
4	2	0943H	t
6	1	0011	f
7	1	0012	f
8	1	0013	f
9	1	0014	f
10	1	0015	f
11	1	0016	f
12	1	0017	f
13	1	0018	f
14	1	0019	f
15	1	0020	f
16	1	0021	f
17	1	0010	f
\.


--
-- Data for Name: sensor_coating_config; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sensor_coating_config (id, id_position_on_tank, id_sensor, id_coating, id_tank_configuration) FROM stdin;
1	1	1	\N	2
2	2	2	\N	2
3	5	\N	1	2
4	1	1	\N	1
5	2	2	\N	1
6	5	\N	3	1
7	6	3	\N	2
8	7	4	\N	2
12	3	1	\N	2
13	39	17	\N	5
14	40	6	\N	5
15	49	15	\N	5
16	50	16	\N	5
17	41	7	\N	5
18	42	8	\N	5
19	43	9	\N	5
20	44	10	\N	5
21	45	11	\N	5
22	46	12	\N	5
23	47	13	\N	5
24	48	14	\N	5
26	39	1	\N	15
27	39	17	\N	16
28	40	6	\N	16
29	49	15	\N	16
30	50	16	\N	16
31	41	7	\N	16
32	42	8	\N	16
33	43	9	\N	16
34	44	10	\N	16
35	45	11	\N	16
36	46	12	\N	16
37	47	13	\N	16
38	48	14	\N	16
\.


--
-- Data for Name: sensor_location; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sensor_location (id, type, ref, serial_number, "order", location, "time", validation) FROM stdin;
1	Barometric	LIS3DH	001	order	in store	2022-06-24 10:16:37.087682+02	t
2	Barometric	LIS3DH	002	order	in store	2022-06-24 10:16:37.087682+02	t
3	Accelerometer	AccS1	0942H	order	in store	2022-06-24 10:16:37.087682+02	t
4	Accelerometer	AccS1	0943H	order	in store	2022-06-24 10:16:37.087682+02	t
5	Accelerometer	AccS1	0943H	order	in config	2022-06-24 10:16:37.087682+02	t
6	Accelerometer	AccS1	0943H	order	in config	2022-06-24 10:16:37.087682+02	t
7	Barometric	LIS3DH	001	out of order	in store	2022-06-24 11:04:47.39929+02	t
8	Barometric	LIS3DH	0010	order	in store	2022-06-28 14:18:36.719427+02	t
9	Barometric	LIS3DH	0011	order	in store	2022-06-28 14:18:36.719427+02	t
10	Barometric	LIS3DH	0012	order	in store	2022-06-28 14:18:36.719427+02	t
11	Barometric	LIS3DH	0013	order	in store	2022-06-28 14:18:36.719427+02	t
12	Barometric	LIS3DH	0014	order	in store	2022-06-28 14:18:36.719427+02	t
13	Barometric	LIS3DH	0015	order	in store	2022-06-28 14:18:36.719427+02	t
14	Barometric	LIS3DH	0016	order	in store	2022-06-28 14:18:36.719427+02	t
15	Barometric	LIS3DH	0017	order	in store	2022-06-28 14:18:36.719427+02	t
16	Barometric	LIS3DH	0018	order	in store	2022-06-28 14:18:36.719427+02	t
17	Barometric	LIS3DH	0019	order	in store	2022-06-28 14:18:36.719427+02	t
18	Barometric	LIS3DH	0020	order	in store	2022-06-28 14:18:36.719427+02	t
19	Barometric	LIS3DH	0021	order	in store	2022-06-28 14:18:36.719427+02	t
20	Barometric	LIS3DH	0010	removed	in store	2022-06-28 14:18:36.719427+02	f
21	Barometric	LIS3DH	0010	order	in store	2022-06-28 14:18:36.719427+02	t
24	Barometric	LIS3DH	001	order	in config	2022-06-30 12:08:51.486632+02	t
25	Barometric	LIS3DH	001	order	in store	2022-06-30 12:08:51.486632+02	t
26	Barometric	LIS3DH	0010	order	in config	2022-06-30 13:58:57.705588+02	t
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
1	tk_config_01	2022-06-24	t	2
2	tk_config_02	2022-06-24	f	2
3	tank_config_1	2022-06-24	t	3
4	tank_config_2	2022-06-24	t	3
5	A/C	2022-06-28	t	3
15	abc	2022-06-30	f	3
16	A/C/1	2022-06-30	f	3
\.


--
-- Data for Name: test; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.test (id, id_test_mean, type, number, id_test_driver, date, time_begin, time_end, id_tank_conf, id_acqui_conf, id_camera_conf, id_ejector_conf, id_cond_init, id_pilot, id_copilot, validate, achievement) FROM stdin;
2	2	\N	160	\N	1900-01-01	00:00:00	00:00:00	\N	\N	\N	\N	2	\N	\N	f	\N
1	2	Flight	158	9	2022-05-25	08:00:00	21:00:00	5	1	1	\N	1	1	2	f	0.75
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
13	P	2	{NULL,NULL,NULL}
14	T	2	{NULL,NULL,NULL}
15	H	2	{NULL,NULL,NULL}
\.


--
-- Data for Name: type_param_sensor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_param_sensor (id, id_ref_sensor, id_type_param) FROM stdin;
1	1	10
2	1	11
3	1	12
4	1	13
5	1	14
6	1	15
\.


--
-- Data for Name: type_param_test_mean; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.type_param_test_mean (id, id_test_mean, id_type_param) FROM stdin;
1	2	3
2	2	4
3	2	5
4	2	6
5	2	7
6	2	8
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

SELECT pg_catalog.setval('public.airfield_id_seq', 5, true);


--
-- Name: attribute_coating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attribute_coating_id_seq', 14, true);


--
-- Name: attribute_detergent_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attribute_detergent_id_seq', 1, false);


--
-- Name: attribute_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.attribute_id_seq', 16, true);


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

SELECT pg_catalog.setval('public.coating_id_seq', 10, true);


--
-- Name: coating_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.coating_location_id_seq', 2, true);


--
-- Name: cond_init_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cond_init_id_seq', 3, true);


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

SELECT pg_catalog.setval('public.data_sensor_id_seq', 178213, true);


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

SELECT pg_catalog.setval('public.position_on_tank_id_seq', 50, true);


--
-- Name: quantite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.quantite_id_seq', 1, false);


--
-- Name: ref_sensor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ref_sensor_id_seq', 4, true);


--
-- Name: sensor_coating_config_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sensor_coating_config_id_seq', 38, true);


--
-- Name: sensor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sensor_id_seq', 17, true);


--
-- Name: sensor_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sensor_location_id_seq', 26, true);


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

SELECT pg_catalog.setval('public.tank_configuration_id_seq', 16, true);


--
-- Name: tank_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tank_id_seq', 3, true);


--
-- Name: test_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.test_id_seq', 3, true);


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

SELECT pg_catalog.setval('public.type_param_id_seq', 15, true);


--
-- Name: type_param_sensor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_param_sensor_id_seq', 6, true);


--
-- Name: type_param_test_mean_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.type_param_test_mean_id_seq', 6, true);


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

SELECT pg_catalog.setval('public.type_unity_id_seq', 12, true);


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

