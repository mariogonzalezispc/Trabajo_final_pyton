/*----------------------------------------------------------------
Creo Tabla Tipo
----------------------------------------------------------------*/
CREATE TABLE `Tipo` (
	`Id_Tipo` INT(11) NOT NULL AUTO_INCREMENT,
	`Nombre_Tipo` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`Id_Tipo`));

/*----------------------------------------------------------------
Creo Tabla Estado
----------------------------------------------------------------*/
CREATE TABLE `Estado` (
	`Id_Estado` INT(11) NOT NULL AUTO_INCREMENT,
	`Nombre_Estado` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`Id_Estado`));

/*----------------------------------------------------------------
Creo Tabla Operatoria_Comercial
----------------------------------------------------------------*/
CREATE TABLE `OperatoriaComercial` (
	`Id_Operatoria_Comercial` INT(11) NOT NULL AUTO_INCREMENT,
	`Nombre_Operatoria_Comercial` VARCHAR(50) NOT NULL DEFAULT '0' COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`Id_Operatoria_Comercial`));

/*----------------------------------------------------------------
Creo Tabla Propietario
----------------------------------------------------------------*/
CREATE TABLE `Propietario` (
	`Id_Propietario` INT(11) NOT NULL AUTO_INCREMENT,
	`Nombre` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`Direccion` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	`Contacto` VARCHAR(50) NOT NULL COLLATE 'utf8mb4_general_ci',
	PRIMARY KEY (`Id_Propietario`));

/*----------------------------------------------------------------
Creo Tabla Propiedad
----------------------------------------------------------------*/
CREATE TABLE `Propiedad` (
	`Id_Propiedad` INT NOT NULL AUTO_INCREMENT,
	`Id_Tipo` INT NULL DEFAULT '0',
	`Id_Estado` INT NULL DEFAULT '0',
	`Id_Operacion_Comercial` INT NULL DEFAULT '0',
	`Id_Propietario` INT NULL DEFAULT '0',
	`Direccion` VARCHAR(50) NULL DEFAULT NULL,
	`Habitacion` VARCHAR(50) NULL DEFAULT NULL,
	`Baños` VARCHAR(50) NULL DEFAULT NULL,
	`Patio` VARCHAR(50) NULL DEFAULT NULL,
	`Cochera` VARCHAR(50) NULL DEFAULT NULL,
	PRIMARY KEY (`Id_Propiedad`),
	CONSTRAINT `FK__Propietario` FOREIGN KEY (`Id_Propietario`) REFERENCES `Propietario` (`Id_Propietario`) ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT `FK__Tipo` FOREIGN KEY (`Id_Tipo`) REFERENCES `Tipo` (`Id_Tipo`) ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT `FK__Estado` FOREIGN KEY (`Id_Estado`) REFERENCES `Estado` (`Id_Estado`) ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT `FK__OperatoriaComercial` FOREIGN KEY (`Id_Operacion_Comercial`) REFERENCES `OperatoriaComercial` (`Id_Operatoria_Comercial`) ON UPDATE NO ACTION ON DELETE NO ACTION
)
COLLATE='utf8mb4_general_ci'
;

/*----------------------------------------------------------------
Inserto un registro en la base de datos en la tabla propiedad
----------------------------------------------------------------*/
INSERT INTO 
`inmobiliaria`.`Propiedad` 
(`Id_Propiedad`,
 `Id_Tipo`,
 `Id_Estado`,
 `Id_Operacion_Comercial`,
 `Id_Propietario`,
 `Direccion`,
 `Habitaciones`, 
 `Baños`,
 `Patio`,
 `Cochera`) 
 VALUES (NULL, '1', '3', '1', '11', 'Mauricio Yaradola 2345', '3', '1', '1', '1');

/*----------------------------------------------------------------
Modifico un registro en la base de datos en la tabla propiedad
----------------------------------------------------------------*/
UPDATE `inmobiliaria`.`Propiedad` 
SET `Direccion`='Dias de la fuente 1346' 
WHERE  `Id_Propiedad`=1;

/*----------------------------------------------------------------
Inserto un registro en la base de datos en la tabla propietario
----------------------------------------------------------------*/
INSERT INTO `inmobiliaria`.`Propietario` 
 (`Nombre`,
  `Direccion`,
  `Contacto`) 
VALUES 
('Revol Eduardo',
 'Ruta 5 KM 78 Alta Gracia',
  '3541236985');

/*----------------------------------------------------------------
Modifico un registro en la base de datos en la tabla propietario
----------------------------------------------------------------*/
UPDATE `inmobiliaria`.`Propietario` 
SET `Nombre`='Freites Anibal' 
WHERE  `Id_Propietario`=8;

/*----------------------------------------------------------------
Listado general de las propiedades
----------------------------------------------------------------*/
SELECT
Propiedad.Direccion,
Propiedad.Habitaciones,
Propiedad.`Baños`,
Propiedad.Patio,
Propiedad.Cochera,
Tipo.Nombre_Tipo,
Estado.Nombre_Estado,
Propietario.Nombre,
Propietario.Contacto
FROM Propiedad, Propietario, Tipo, Estado
WHERE Propiedad.Id_Propietario = Propietario.Id_Propietario 
AND Propiedad.Id_Tipo = Tipo.Id_Tipo
AND Propiedad.Id_Estado = Estado.Id_Estado;

/*----------------------------------------------------------------
Listado general de las propiedades en alquiler
----------------------------------------------------------------*/
SELECT 
Propiedad.Direccion,
Propiedad.Habitaciones,
Propiedad.`Baños`,
Propiedad.Patio,
Propiedad.Cochera,
Estado.Nombre_Estado,
Propietario.Nombre,
Propietario.Contacto,
Tipo.Nombre_Tipo
FROM Propiedad, Estado, Propietario, Tipo 
WHERE Propiedad.Id_Estado = 1
AND Propiedad.Id_Estado = Estado.Id_Estado
AND Propiedad.Id_Propietario= Propietario.Id_Propietario
AND Propiedad.Id_Tipo= Tipo.Id_Tipo;

/*----------------------------------------------------------------
Listado general de las propiedades ALQUILADA
----------------------------------------------------------------*/
SELECT 
Propiedad.Direccion,
Propiedad.Habitaciones,
Propiedad.`Baños`,
Propiedad.Patio,
Propiedad.Cochera,
Estado.Nombre_Estado,
Propietario.Nombre,
Propietario.Contacto,
Tipo.Nombre_Tipo
FROM Propiedad, Estado, Propietario, Tipo 
WHERE Propiedad.Id_Estado = 2
AND Propiedad.Id_Estado = Estado.Id_Estado
AND Propiedad.Id_Propietario= Propietario.Id_Propietario
AND Propiedad.Id_Tipo= Tipo.Id_Tipo;

/*----------------------------------------------------------------
Listado general de las propiedades en Venta
----------------------------------------------------------------*/
SELECT 
Propiedad.Direccion,
Propiedad.Habitaciones,
Propiedad.`Baños`,
Propiedad.Patio,
Propiedad.Cochera,
Estado.Nombre_Estado,
Propietario.Nombre,
Propietario.Contacto,
Tipo.Nombre_Tipo
FROM Propiedad, Estado, Propietario, Tipo 
WHERE Propiedad.Id_Estado = 3
AND Propiedad.Id_Estado = Estado.Id_Estado
AND Propiedad.Id_Propietario= Propietario.Id_Propietario
AND Propiedad.Id_Tipo= Tipo.Id_Tipo;

/*----------------------------------------------------------------
Listado general de las propiedades en VENDIDAS
----------------------------------------------------------------*/
SELECT 
Propiedad.Direccion,
Propiedad.Habitaciones,
Propiedad.`Baños`,
Propiedad.Patio,
Propiedad.Cochera,
Estado.Nombre_Estado,
Propietario.Nombre,
Propietario.Contacto,
Tipo.Nombre_Tipo
FROM Propiedad, Estado, Propietario, Tipo 
WHERE Propiedad.Id_Estado = 4
AND Propiedad.Id_Estado = Estado.Id_Estado
AND Propiedad.Id_Propietario= Propietario.Id_Propietario
AND Propiedad.Id_Tipo= Tipo.Id_Tipo;