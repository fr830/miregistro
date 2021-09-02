USE miregistro;

INSERT rol (Nombre, Descripcion) 
VALUES ('Gestor de estadisticas', 'Permisos para leer estadisticas de empleados');
	
SELECT * FROM rol;

UPDATE rol SET Nombre = 'Root', Descripcion = 'Control total del sistema' WHERE IdRol = 3;

ALTER TABLE rol AUTO_INCREMENT = 0;
ALTER TABLE perfil AUTO_INCREMENT = 0;

DELETE FROM rol WHERE IdRol = 2;

INSERT INTO preguntaseguridad (Pregunta)
VALUES ('¿Cual era el nombre de tu primer mascota?'),
('¿Cual es el nombre de la ciudad en la que naciste?'),
('¿Cual era tu apodo de infancia?'),
('¿Cual es el nombre de la ciudad en la que se conocieron tus padres?'),
('¿Cual es el nombre de tu primo mayor?'),
('¿Como se llamaba la primera escuela a la que asististe?');

SELECT * FROM preguntaseguridad;

/* Insert nuevos usuarios */
DELETE FROM usuario_Seguridad WHERE IdUsuario < 10;
DELETE FROM usuario_rol WHERE IdUsuario < 10;
DELETE FROM empleado WHERE IdEmpleado < 10;
DELETE FROM perfil WHERE IdPerfil < 10;
DELETE FROM usuario WHERE IdUsuario < 10;

INSERT INTO usuario(FkIdPerfil, Usuario, Contraseña, Email)
VALUES(7, 'lauracalafate', 'registrocalafate', 'lauracalafate@hotmail.com');

INSERT INTO perfil (IdPerfil, Nombre, Apellido, Nick, FechaCumpleaños)
VALUES (7, 'Laura', 'Calafate', 'Lau', NOW());

ALTER TABLE usuario AUTO_INCREMENT = 1;

INSERT INTO empleado (IdEmpleado, FkIdUsuario, FkIdEmpresa, EstadoActual)
VALUES
(
	6,
	6,
    1,
    0
);

DELETE FROM perfil WHERE idperfil = 7;

UPDATE usuario SET Email = "paolapereyra061@gmail.com" WHERE IdUsuario = 3; 

UPDATE empleado set IdEmpleado = 1 where IdEmpleado = 1001;

SELECT * FROM perfil;
SELECT * FROM empleado;

/*Autentificar*/
SELECT * FROM usuario WHERE usuario='noelicalafate' AND contraseña='12345' AND activo = 1 LIMIT 1;

SELECT U.IdUsuario, P.IdPerfil,  U.Usuario, U.Email, U.activo, P.Nombre, P.Apellido, P.nick, P.FechaCumpleaños, Er.nombre
FROM usuario U
JOIN perfil P ON P.IdPerfil = U.FkIdPerfil
JOIN empleado E ON E.FkIdUsuario = U.IdUsuario
JOIN empresa Er ON Er.IdEmpresa = E.FkIdEmpresa;

ALTER TABLE usuario AUTO_INCREMENT = 1;
DELETE FROM usuario WHERE idusuario = 2;

/*Rol Insert*/
INSERT INTO usuario_rol (IdUsuario, IdRol, FechaInicio, FechaFin)
VALUES (3, 4, NOW(), '2022-12-01');

/*Rol Query*/
SELECT U.Usuario, R.IdRol, R.Nombre
FROM usuario_rol Ur
INNER JOIN usuario U ON U.IdUsuario = Ur.IdUsuario
INNER JOIN rol R ON R.IdRol = Ur.IdRol;

UPDATE rol SET Nombre = "Gestor caja" WHERE IdRol = "6";

