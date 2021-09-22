USE miregistro;

/* Cargar categorias tramites*/
ALTER TABLE categoriatramite AUTO_INCREMENT = 10;

INSERT INTO categoriatramite (Nombre)
VALUES(('Informe historico de dominio'),
	  ('Cambio de domicilio con pedido'),
      ('Canc prenda inc c'),
	  ('Canc prenda inc a/b'),
      ('Informe multa e infracciones'),
	  ('Asignacion de Cedula'),
      ('Modificacion Prenda'),
	  ('Informe Estado de Dominio por correo'),
      ('Transferencia c/pedido'),
	  ('Fotocopia de constancias registrales'),
	  ('Informe historico por corresponder'),
	  ('Reposicion de placa metalica'),
      ('Devolucion del automotor al titular'),
	  ('Certificados dominiales'),
      ('Denuncia de robo'),
	  ('Dominiales'));
      
UPDATE categoriatramite SET Nombre = "Otros" WHERE IdCategoriaTramite = 1;

SELECT * FROM categoriatramite;

/* Cargar etapas tramites */
INSERT INTO etapatramite (Nombre)
VALUES ('Observado');

SELECT * FROM etapatramite;
ALTER TABLE etapatramite AUTO_INCREMENT = 1;
DELETE FROM etapatramite WHERE IdEtapaTramite = 1;

/* Cargar categoria de errores */

INSERT INTO categoriaerror (Nombre)
VALUES  ('Error categoria A'),
		('Error categoria B');
        
SELECT * FROM categoriaerror;

INSERT INTO tramite (Dominio, FkIdCategoria, FkIdEmpresa, Fecha, Observaciones)
VALUES 
(
	'AA000XX', /* Dominio */
	1 /* IdCategoria */,
    1 /* IdEmpresa */,
    NOW() /* Fecha */,
    'Sin observaciones'
);

SET @last_id_tramite = LAST_INSERT_ID();

/* Procesos */
INSERT INTO tramite_proceso
VALUES 
(
	last_insert_id() /* TramiteId */,
    3 /* IdEtapa*/,
    1 /* IdEmpleado */,
    True /* Estado actual */
);

ALTER TABLE tramite  AUTO_INCREMENT = 1;
DELETE FROM tramite WHERE tramite.IdTramite = 2183;
DELETE FROM tramite WHERE IdTramite < 10000;
DELETE FROM tramite_proceso WHERE IdTramite < 10000;

SELECT count(*) FROM tramite;

UPDATE tramite_proceso SET FkIdEmpleado = 2 WHERE IdTramite = 1 AND IdEtapaTramite = 1;
SELECT * FROM tramite_proceso WHERE IdTramite = 2183;
SELECT COUNT(*) FROM tramite_proceso;

/* Errores */
INSERT INTO tramite_error
VALUES 
(
	1 /* TramiteId */,
    1 /* IdCategoriaError*/,
    1 /* IdEmpleado */,
    False /* Estado actual */
);

SELECT * FROM tramite_proceso;
SELECT * FROM empleado;

SELECT T.IdTramite AS ID, T.Dominio AS Dominio, Ct.Nombre AS Categoria, T.Fecha AS Fecha, T.Observaciones AS Observaciones,
		Et.Nombre AS 'Proceso', P.Nombre AS 'Quien Proceso', 
		(SELECT Et1.Nombre FROM tramite T1 JOIN tramite_proceso Tp1 ON Tp1.IdTramite = T1.IdTramite
			JOIN etapatramite Et1 ON Et1.IdEtapaTramite = Tp1.IdEtapaTramite WHERE T1.IdTramite = T.IdTramite AND Et1.IdEtapaTramite = '1') AS Inscripcion,
        (SELECT P2.Nombre FROM tramite_proceso Tp2 
		JOIN empleado E2 ON E2.IdEmpleado = Tp2.FkIdEmpleado
		JOIN usuario U2 ON U2.IdUsuario = E2.FkIdUsuario
		JOIN perfil P2 ON P2.IdPerfil = U2.FkIdPerfil
        WHERE Tp2.IdTramite = T.IdTramite AND Tp2.IdEtapaTramite = 2 LIMIT 1) AS 'Quien Inscribio'
FROM tramite T
	JOIN categoriatramite Ct ON Ct.IdCategoriaTramite = T.FkIdCategoria
	JOIN tramite_proceso Tp ON Tp.IdTramite = T.IdTramite
	JOIN etapatramite Et ON Et.IdEtapaTramite = Tp.IdEtapaTramite
	JOIN empleado E ON E.IdEmpleado = Tp.FkIdEmpleado
	JOIN usuario U ON U.IdUsuario = E.FkIdUsuario
	JOIN perfil P ON P.IdPerfil = U.FkIdPerfil
GROUP BY T.IdTramite
LIMIT 10;

SELECT COUNT(*) FROM tramite;

SELECT T.IdTramite AS ID, T.Dominio AS Dominio, Ct.Nombre AS Categoria, T.Observaciones AS Observaciones
                 FROM tramite T
					JOIN categoriatramite Ct ON Ct.IdCategoriaTramite = T.FkIdCategoria
                 GROUP BY T.IdTramite;
                 
SELECT * FROM tramite WHERE tramite.IdTramite > 2180;

SET SQL_SAFE_UPDATES=0;

DELETE FROM tramite WHERE Observaciones = "Sin observaciones pendientes";
ALTER TABLE tramite AUTO_INCREMENT = 1; 




