DROP TABLE IF EXISTS public.users;
CREATE TABLE public.users
(
    id  SERIAL PRIMARY KEY,
    email character varying(255) COLLATE pg_catalog."default",
    first_name character varying(255) COLLATE pg_catalog."default",
    last_name character varying(255) COLLATE pg_catalog."default",
    oauth_token character varying(255) COLLATE pg_catalog."default",
    oauth_token_secret character varying(255) COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.users
    OWNER to postgres;

GRANT ALL ON TABLE public.users TO jonas;

GRANT ALL ON TABLE public.users TO postgres;