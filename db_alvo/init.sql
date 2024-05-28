--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1 (Debian 16.1-1.pgdg120+1)
-- Dumped by pg_dump version 16.1 (Debian 16.1-1.pgdg120+1)

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
-- Name: data; Type: TABLE; Schema: public; Owner: user_alvo
--

CREATE TABLE public.data (
    signal_id integer NOT NULL,
    "timestamp" timestamp without time zone NOT NULL,
    value double precision NOT NULL
);


ALTER TABLE public.data OWNER TO user_alvo;

--
-- Name: data_signal_id_seq; Type: SEQUENCE; Schema: public; Owner: user_alvo
--

CREATE SEQUENCE public.data_signal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.data_signal_id_seq OWNER TO user_alvo;

--
-- Name: data_signal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user_alvo
--

ALTER SEQUENCE public.data_signal_id_seq OWNED BY public.data.signal_id;


--
-- Name: signal; Type: TABLE; Schema: public; Owner: user_alvo
--

CREATE TABLE public.signal (
    id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.signal OWNER TO user_alvo;

--
-- Name: signal_id_seq; Type: SEQUENCE; Schema: public; Owner: user_alvo
--

CREATE SEQUENCE public.signal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.signal_id_seq OWNER TO user_alvo;

--
-- Name: signal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user_alvo
--

ALTER SEQUENCE public.signal_id_seq OWNED BY public.signal.id;


--
-- Name: data signal_id; Type: DEFAULT; Schema: public; Owner: user_alvo
--

ALTER TABLE ONLY public.data ALTER COLUMN signal_id SET DEFAULT nextval('public.data_signal_id_seq'::regclass);


--
-- Name: signal id; Type: DEFAULT; Schema: public; Owner: user_alvo
--

ALTER TABLE ONLY public.signal ALTER COLUMN id SET DEFAULT nextval('public.signal_id_seq'::regclass);


--
-- Data for Name: data; Type: TABLE DATA; Schema: public; Owner: user_alvo
--

COPY public.data (signal_id, "timestamp", value) FROM stdin;
\.


--
-- Data for Name: signal; Type: TABLE DATA; Schema: public; Owner: user_alvo
--

COPY public.signal (id, name) FROM stdin;
\.


--
-- Name: data_signal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user_alvo
--

SELECT pg_catalog.setval('public.data_signal_id_seq', 1, false);


--
-- Name: signal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user_alvo
--

SELECT pg_catalog.setval('public.signal_id_seq', 1, false);


--
-- Name: data data_pkey; Type: CONSTRAINT; Schema: public; Owner: user_alvo
--

ALTER TABLE ONLY public.data
    ADD CONSTRAINT data_pkey PRIMARY KEY (signal_id);


--
-- Name: signal signal_pkey; Type: CONSTRAINT; Schema: public; Owner: user_alvo
--

ALTER TABLE ONLY public.signal
    ADD CONSTRAINT signal_pkey PRIMARY KEY (id);


--
-- Name: data data_signal_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user_alvo
--

ALTER TABLE ONLY public.data
    ADD CONSTRAINT data_signal_id_fkey FOREIGN KEY (signal_id) REFERENCES public.signal(id);


--
-- PostgreSQL database dump complete
--

