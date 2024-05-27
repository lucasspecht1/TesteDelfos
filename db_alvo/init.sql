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
    "timestamp" timestamp without time zone NOT NULL,
    signal_id integer NOT NULL,
    value double precision NOT NULL
);


ALTER TABLE public.data OWNER TO user_alvo;

--
-- Name: signal; Type: TABLE; Schema: public; Owner: user_alvo
--

CREATE TABLE public.signal (
    id integer NOT NULL,
    name text NOT NULL
);


ALTER TABLE public.signal OWNER TO user_alvo;

--
-- Data for Name: data; Type: TABLE DATA; Schema: public; Owner: user_alvo
--

COPY public.data ("timestamp", signal_id, value) FROM stdin;
\.


--
-- Data for Name: signal; Type: TABLE DATA; Schema: public; Owner: user_alvo
--

COPY public.signal (id, name) FROM stdin;
\.


--
-- Name: data data_pkey; Type: CONSTRAINT; Schema: public; Owner: user_alvo
--

ALTER TABLE ONLY public.data
    ADD CONSTRAINT data_pkey PRIMARY KEY ("timestamp");


--
-- Name: signal signal_pkey; Type: CONSTRAINT; Schema: public; Owner: user_alvo
--

ALTER TABLE ONLY public.signal
    ADD CONSTRAINT signal_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

