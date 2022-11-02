
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


SELECT * FROM `Propiedad` LIMIT 100;


SELECT Propiedad.Direccion,
 Propiedad.Habitaciones,
 Propiedad.`Baños`,
 Propiedad.Patio,
 Propiedad.Cochera,
 Propietario.Id_Propietario,
 Propietario.Nombre,
 Propietario.Contacto
FROM Propiedad, Propietario
WHERE Propiedad.Id_Propietario = Propietario.Id_Propietario

