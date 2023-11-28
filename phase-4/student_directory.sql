DROP TABLE IF EXISTS students;
DROP SEQUENCE IF EXISTS students_id_seq;


CREATE SEQUENCE IF NOT EXISTS students_id_seq;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cohort VARCHAR(255)
);

INSERT INTO students
    (name, cohort)
    VALUES('Bob', 'January 2023')