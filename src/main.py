database/script.sql
-- SCHEMA: public

-- DROP SCHEMA IF EXISTS public ;

CREATE SCHEMA IF NOT EXISTS public
    AUTHORIZATION pg_database_owner;

COMMENT ON SCHEMA public
    IS 'standard public schema';

GRANT USAGE ON SCHEMA public TO PUBLIC;

GRANT ALL ON SCHEMA public TO pg_database_owner;

---
-- Table: public.auto

-- DROP TABLE IF EXISTS public.auto;

CREATE TABLE IF NOT EXISTS public.auto
(
    id_auto integer NOT NULL DEFAULT nextval('auto_id_auto_seq'::regclass),
    vin character varying(17) COLLATE pg_catalog."default" NOT NULL,
    marca character varying(50) COLLATE pg_catalog."default" NOT NULL,
    modelo character varying(50) COLLATE pg_catalog."default" NOT NULL,
    anio integer NOT NULL,
    color character varying(30) COLLATE pg_catalog."default",
    precio_lista numeric(12,2) NOT NULL,
    kilometraje integer,
    estado character varying(20) COLLATE pg_catalog."default" DEFAULT 'disponible'::character varying,
    combustible character varying(30) COLLATE pg_catalog."default",
    transmision character varying(30) COLLATE pg_catalog."default",
    id_categoria integer,
    CONSTRAINT auto_pkey PRIMARY KEY (id_auto),
    CONSTRAINT auto_vin_key UNIQUE (vin),
    CONSTRAINT auto_id_categoria_fkey FOREIGN KEY (id_categoria)
        REFERENCES public.categoria (id_categoria) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.auto
    OWNER to postgres;
----
-- Table: public.cliente

-- DROP TABLE IF EXISTS public.cliente;

CREATE TABLE IF NOT EXISTS public.cliente
(
    id_cliente integer NOT NULL DEFAULT nextval('cliente_id_cliente_seq'::regclass),
    nombre character varying(100) COLLATE pg_catalog."default" NOT NULL,
    apellido character varying(100) COLLATE pg_catalog."default" NOT NULL,
    ci character varying(20) COLLATE pg_catalog."default" NOT NULL,
    telefono character varying(15) COLLATE pg_catalog."default",
    email character varying(100) COLLATE pg_catalog."default",
    direccion text COLLATE pg_catalog."default",
    fecha_registro date DEFAULT CURRENT_DATE,
    CONSTRAINT cliente_pkey PRIMARY KEY (id_cliente),
    CONSTRAINT cliente_ci_key UNIQUE (ci)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cliente
    OWNER to postgres;
----
-- Table: public.empleado

-- DROP TABLE IF EXISTS public.empleado;

CREATE TABLE IF NOT EXISTS public.empleado
(
    id_empleado integer NOT NULL DEFAULT nextval('empleado_id_empleado_seq'::regclass),
    nombre character varying(100) COLLATE pg_catalog."default" NOT NULL,
    apellido character varying(100) COLLATE pg_catalog."default" NOT NULL,
    ci character varying(20) COLLATE pg_catalog."default" NOT NULL,
    telefono character varying(15) COLLATE pg_catalog."default",
    email character varying(100) COLLATE pg_catalog."default",
    fecha_ingreso date,
    id_cargo integer,
    id_jefe integer,
    CONSTRAINT empleado_pkey PRIMARY KEY (id_empleado),
    CONSTRAINT empleado_ci_key UNIQUE (ci),
    CONSTRAINT empleado_id_cargo_fkey FOREIGN KEY (id_cargo)
        REFERENCES public.cargo (id_cargo) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT empleado_id_jefe_fkey FOREIGN KEY (id_jefe)
        REFERENCES public.empleado (id_empleado) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.empleado
    OWNER to postgres;
----
-- Table: public.categoria

-- DROP TABLE IF EXISTS public.categoria;

CREATE TABLE IF NOT EXISTS public.categoria
(
    id_categoria integer NOT NULL DEFAULT nextval('categoria_id_categoria_seq'::regclass),
    nombre character varying(50) COLLATE pg_catalog."default" NOT NULL,
    descripcion text COLLATE pg_catalog."default",
    CONSTRAINT categoria_pkey PRIMARY KEY (id_categoria)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.categoria
    OWNER to postgres;
----
-- Table: public.cargo

-- DROP TABLE IF EXISTS public.cargo;

CREATE TABLE IF NOT EXISTS public.cargo
(
    id_cargo integer NOT NULL DEFAULT nextval('cargo_id_cargo_seq'::regclass),
    nombre_cargo character varying(50) COLLATE pg_catalog."default" NOT NULL,
    descripcion text COLLATE pg_catalog."default",
    nivel integer,
    CONSTRAINT cargo_pkey PRIMARY KEY (id_cargo)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.cargo
    OWNER to postgres;
----
-- Table: public.venta

-- DROP TABLE IF EXISTS public.venta;

CREATE TABLE IF NOT EXISTS public.venta
(
    id_venta integer NOT NULL DEFAULT nextval('venta_id_venta_seq'::regclass),
    fecha_venta timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    precio_final numeric(12,2) NOT NULL,
    tipo_pago character varying(50) COLLATE pg_catalog."default",
    descuento numeric(12,2),
    id_cliente integer,
    id_empleado integer,
    CONSTRAINT venta_pkey PRIMARY KEY (id_venta),
    CONSTRAINT venta_id_cliente_fkey FOREIGN KEY (id_cliente)
        REFERENCES public.cliente (id_cliente) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT venta_id_empleado_fkey FOREIGN KEY (id_empleado)
        REFERENCES public.empleado (id_empleado) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.venta
    OWNER to postgres;
----
-- Table: public.detalle_venta

-- DROP TABLE IF EXISTS public.detalle_venta;

CREATE TABLE IF NOT EXISTS public.detalle_venta
(
    id_detalle integer NOT NULL DEFAULT nextval('detalle_venta_id_detalle_seq'::regclass),
    id_venta integer,
    id_auto integer,
    precio_unitario numeric(12,2) NOT NULL,
    descuento_unitario numeric(12,2),
    subtotal numeric(12,2) NOT NULL,
    CONSTRAINT detalle_venta_pkey PRIMARY KEY (id_detalle),
    CONSTRAINT detalle_venta_id_auto_fkey FOREIGN KEY (id_auto)
        REFERENCES public.auto (id_auto) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT detalle_venta_id_venta_fkey FOREIGN KEY (id_venta)
        REFERENCES public.venta (id_venta) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.detalle_venta
    OWNER to postgres;
----
-- Table: public.pago

-- DROP TABLE IF EXISTS public.pago;

CREATE TABLE IF NOT EXISTS public.pago
(
    id_pago integer NOT NULL DEFAULT nextval('pago_id_pago_seq'::regclass),
    fecha_pago timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    monto numeric(12,2) NOT NULL,
    numero_cuota integer,
    metodo_pago character varying(50) COLLATE pg_catalog."default",
    estado character varying(20) COLLATE pg_catalog."default",
    id_financiamiento integer,
    CONSTRAINT pago_pkey PRIMARY KEY (id_pago),
    CONSTRAINT pago_id_financiamiento_fkey FOREIGN KEY (id_financiamiento)
        REFERENCES public.financiamiento (id_financiamiento) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.pago
    OWNER to postgres;
----
-- Table: public.financiamiento

-- DROP TABLE IF EXISTS public.financiamiento;

CREATE TABLE IF NOT EXISTS public.financiamiento
(
    id_financiamiento integer NOT NULL DEFAULT nextval('financiamiento_id_financiamiento_seq'::regclass),
    monto_financiado numeric(12,2) NOT NULL,
    cuotas integer NOT NULL,
    tasa_interes numeric(5,2),
    valor_cuota numeric(12,2),
    fecha_inicio date,
    estado character varying(20) COLLATE pg_catalog."default",
    id_venta integer,
    CONSTRAINT financiamiento_pkey PRIMARY KEY (id_financiamiento),
    CONSTRAINT financiamiento_id_venta_fkey FOREIGN KEY (id_venta)
        REFERENCES public.venta (id_venta) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.financiamiento
    OWNER to postgres;
