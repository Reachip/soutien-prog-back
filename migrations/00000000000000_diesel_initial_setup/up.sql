-- This file was automatically created by Diesel to setup helper functions
-- and other internal bookkeeping. This file is safe to edit, any future
-- changes will be added to existing projects as new migrations.
-- Your SQL goes here
-- Sets up a trigger for the given table to automatically set a column called
-- `updated_at` whenever the row is modified (unless `updated_at` was included
-- in the modified columns)
--
-- # Example
--
-- ```sql
-- CREATE TABLE users (id SERIAL PRIMARY KEY, updated_at TIMESTAMP NOT NULL DEFAULT NOW());
--
-- SELECT diesel_manage_updated_at('users');
-- ```

CREATE TABLE if not exists school_module (
	school_module_id SERIAL PRIMARY KEY,
	module_name VARCHAR(50) NOT NULL,
	module_number VARCHAR(10) NOT NULL,
	UNIQUE(module_name, module_number)
);

CREATE TABLE if not exists teacher (
	teacher_id SERIAL PRIMARY KEY,
	username varchar(50) NOT NULL,
	mail varchar(64) NOT NULL,
	pwd varchar(200) NOT NULL,
	UNIQUE(username, mail)
);

CREATE TABLE if not exists courses (
	courses_id SERIAL PRIMARY KEY,
	teacher_id INTEGER NOT NULL,
	school_module_id INTEGER NOT NULL,
	starting_at TIMESTAMP NOT NULL,
    ending_at TIMESTAMP NOT NULL,
    constraint fk_teacher FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id),
	constraint fk_school_module FOREIGN KEY (school_module_id) REFERENCES school_module(school_module_id)
);

CREATE TABLE if not exists participant
(
    participant_id   SERIAL PRIMARY KEY,
    mail             varchar(64) NOT NULL,
    school_module_id INTEGER     NOT NULL,
    constraint fk_school_module FOREIGN KEY (school_module_id) REFERENCES school_module (school_module_id)
);

CREATE OR REPLACE FUNCTION diesel_manage_updated_at(_tbl regclass) RETURNS VOID AS $$
BEGIN
    EXECUTE format('CREATE TRIGGER set_updated_at BEFORE UPDATE ON %s
                    FOR EACH ROW EXECUTE PROCEDURE diesel_set_updated_at()', _tbl);
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION diesel_set_updated_at() RETURNS trigger AS $$
BEGIN
    IF (
        NEW IS DISTINCT FROM OLD AND
        NEW.updated_at IS NOT DISTINCT FROM OLD.updated_at
    ) THEN
        NEW.updated_at := current_timestamp;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
