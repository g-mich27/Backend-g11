INSERT INTO direcciones (direccion, numero, referencia, alumno_id) 
                VALUES ('Calle los Tulipanes', 429, 'Al costado de la bodega', NULL);

SELECT * FROM direcciones INNER JOIN alumnos ON direcciones.alumno_id = alumnos.id;

SELECT * FROM direcciones LEFT JOIN alumnos ON direcciones.alumno_id = alumnos.id;

SELECT * FROM direcciones RIGHT JOIN alumnos ON direcciones.alumno_id = alumnos.id;

SELECT * FROM direcciones FULL JOIN alumnos ON direcciones.alumno_id = alumnos.id;

--Crear una tabla llamada cursos en la cual vamos a tener lo siguiente
--Nombre TEXT, descripcion VARCHAR(100), habilitado BOOLEAN

CREATE TABLE cursos(
    id SERIAL PRIMARY KEY,
    nombre TEXT,
    descripcion VARCHAR(100),
    habilitado BOOLEAN
);

--Un alumno puede tener varios cursos y ademas un curso puede tener varios alumnos
-- Crear una tabla intermedia alumnos_cursos cuyas columnas seran las sgtes
-- id SERIAL PK, alumno_id INT, curso_id INT y crear sus llaves foraneas

CREATE TABLE alumnos_cursos(
    id SERIAL PRIMARY KEY,
    alumno_id INT NOT NULL,
    curso_id INT NOT NULL,
    UNIQUE (alumno_id, curso_id),
    CONSTRAINT fk_alumnos FOREIGN KEY (alumno_id) REFERENCES alumnos(id),
    CONSTRAINT fk_cursos FOREIGN KEY (curso_id) REFERENCES cursos(id)
);

INSERT INTO cursos (nombre, descripcion, habilitado) VALUES
                    ('Matematica', 'Matematica con algebra', true),
                    ('CTA', 'Cienta Tecnologia y Ambiente', true),
                    ('Comunicacion', 'Letras', true),
                    ('Arte', 'Artes plasticas', false),
                    ('Ingles', 'English for kids', true);


INSERT INTO alumnos_cursos (alumno_id, curso_id) VALUES
                               (1,     1),
                               (2,     1),
                               (1,     3),
                               (3,     4),
                               (3,     2),
                               (3,     3);


-- Haciendo un join desde la tabla alumnos, pasando por la tabla alumnos_cursos y terminando en la tabla cursos
SELECT * FROM
alumnos INNER JOIN alumnos_cursos
ON alumnos.id = alumnos_cursos.alumno_id
INNER JOIN cursos
ON alumnos_cursos.curso_id = cursos.id;


-- Si queremos colocar un alias a los nombres de la tablas
select a.nombre from
alumnos AS a inner join alumnos_cursos AS ac
on a.id = ac.alumno_id
inner join cursos AS c
on ac.curso_id = c.id;


-- Selecciona los nombre y apellidos de los alumnos que tengan el curso de comunicacion
select a.nombre, a.apellido
from alumnos as a inner join alumnos_cursos as ac on a.id = ac.alumno_id
inner join cursos as c on ac.curso_id = c.id
where c.nombre = 'Comunicacion';

-- Selecciona todos los cursos que lleve el alumno Michell
select c.nombre
from alumnos as a inner join alumnos_cursos as ac on a.id = ac.alumno_id
inner join cursos as c on ac.curso_id = c.id
where a.nombre = 'Michell';

-- Selecciona los alumnos cuyos cursos esten habilitados(true) 
select a.nombre, c.nombre
from alumnos as a inner join alumnos_cursos as ac on a.id = ac.alumno_id
inner join cursos as c on ac.curso_id = c.id
where c.habilitado = true and a.matriculado = true;
-- lo mismo pero sin alias
select alumnos.nombre, cursos.nombre
from alumnos inner join alumnos_cursos on alumnos.id = alumnos_cursos.alumno_id
inner join cursos on alumnos_cursos.curso_id = cursos.id
where cursos.habilitado = true and alumnos.matriculado = true;