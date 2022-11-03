
CREATE TABLE `Propiedad` (
	`Id_Propiedad` INT NULL,
	`Id_Tipo` INT NULL,
	`Id_Estado` INT NULL,
	`Id_Operacion_Comercial` INT NULL,
	`Id_Propietario` INT NULL,
	`Nombre` INT NULL,
	`Direccion` INT NULL,
	`Contacto` INT NULL
)



/*----------------------------------------------------------------
Listado general de las propiedades
------------------------------------------------------------------
*/

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
Listado general de las propiedades
------------------------------------------------------------------
*/
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
------------------------------------------------------------------
*/
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
------------------------------------------------------------------
*/
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
------------------------------------------------------------------
*/
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
------------------------------------------------------------------
*/
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