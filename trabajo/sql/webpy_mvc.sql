CREATE DATABASE webpy_mvc;

USE webpy_mvc;

CREATE TABLE personas(
    nombre varchar(50) NOT NULL PRIMARY KEY,
    email varchar(50) NOT NULL,
    edad varchar(15) NOT NULL,
    apPat varchar (15) NOT NULL,
    apMat VARCHAR (50) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO personas (nombre, email, edad,apPat,apMat),
VALUES ('Dejah','dejah@barson','19','diaz','martinez'),
('Jhon','jhon@earth','20','diaz','martinez'),
('Carthoris','carthoris@barson','20','diaz','martinez');

SHOW TABLES;

SELECT * FROM personas;

DESCRIBE personas;

CREATE USER 'webpy'@'localhost' IDENTIFIED BY 'webpy.2019';
GRANT ALL PRIVILEGES ON webpy_mvc.* TO 'webpy'@'localhost';
FLUSH PRIVILEGES;
