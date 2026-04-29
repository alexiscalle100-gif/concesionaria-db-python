-- 1. Tablas Independientes (Maestras)
CREATE TABLE cargo (
    id_cargo SERIAL PRIMARY KEY,
    nombre_cargo VARCHAR(50) NOT NULL,
    descripcion TEXT,
    nivel INTEGER
);

CREATE TABLE categoria (
    id_categoria SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);

CREATE TABLE cliente (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    ci VARCHAR(20) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    email VARCHAR(100),
    direccion TEXT,
    fecha_registro DATE DEFAULT CURRENT_DATE
);

-- 2. Tablas con dependencias simples
CREATE TABLE empleado (
    id_empleado SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    ci VARCHAR(20) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    email VARCHAR(100),
    fecha_ingreso DATE,
    id_cargo INTEGER REFERENCES cargo(id_cargo),
    id_jefe INTEGER REFERENCES empleado(id_empleado) -- Relación recursiva
);

CREATE TABLE auto (
    id_auto SERIAL PRIMARY KEY,
    vin VARCHAR(17) UNIQUE NOT NULL,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    anio INTEGER NOT NULL,
    color VARCHAR(30),
    precio_lista DECIMAL(12, 2) NOT NULL,
    kilometraje INTEGER,
    estado VARCHAR(20) DEFAULT 'disponible',
    combustible VARCHAR(30),
    transmision VARCHAR(30),
    id_categoria INTEGER REFERENCES categoria(id_categoria)
);

-- 3. Tablas de Movimiento y Transacciones
CREATE TABLE venta (
    id_venta SERIAL PRIMARY KEY,
    fecha_venta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    precio_final DECIMAL(12, 2) NOT NULL,
    tipo_pago VARCHAR(50), -- Contado o Financiamiento
    descuento DECIMAL(12, 2),
    id_cliente INTEGER REFERENCES cliente(id_cliente),
    id_empleado INTEGER REFERENCES empleado(id_empleado)
);

CREATE TABLE detalle_venta (
    id_detalle SERIAL PRIMARY KEY,
    id_venta INTEGER REFERENCES venta(id_venta),
    id_auto INTEGER REFERENCES auto(id_auto),
    precio_unitario DECIMAL(12, 2) NOT NULL,
    descuento_unitario DECIMAL(12, 2),
    subtotal DECIMAL(12, 2) NOT NULL
);

-- 4. Tablas de Finanzas
CREATE TABLE financiamiento (
    id_financiamiento SERIAL PRIMARY KEY,
    monto_financiado DECIMAL(12, 2) NOT NULL,
    cuotas INTEGER NOT NULL,
    tasa_interes DECIMAL(5, 2),
    valor_cuota DECIMAL(12, 2),
    fecha_inicio DATE,
    estado VARCHAR(20),
    id_venta INTEGER REFERENCES venta(id_venta)
);

CREATE TABLE pago (
    id_pago SERIAL PRIMARY KEY,
    fecha_pago TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    monto DECIMAL(12, 2) NOT NULL,
    numero_cuota INTEGER,
    metodo_pago VARCHAR(50),
    estado VARCHAR(20),
    id_financiamiento INTEGER REFERENCES financiamiento(id_financiamiento)
);