create sequence if not exists teacher_id_seq; 
create sequence if not exists participant_id_seq; 
create sequence if not exists school_module_id_seq; 

CREATE TABLE if not exists school_module (
	school_module_id INTEGER NOT NULL DEFAULT nextval('school_module_id_seq') PRIMARY KEY,
	module_name VARCHAR(50),
	module_number VARCHAR(10),
	UNIQUE(school_module_id)
);

CREATE TABLE if not exists teacher (
	teacher_id INTEGER NOT NULL DEFAULT nextval('teacher_id_seq') PRIMARY KEY,
	username varchar(50),
	mail varchar(64),
	pwd varchar(200),
	UNIQUE(teacher_id)
);


CREATE TABLE if not exists courses (
	teacher_id INTEGER,
	school_module_id INTEGER,
	constraint fk_teacher FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id),
	constraint fk_school_module FOREIGN KEY (school_module_id) REFERENCES school_module(school_module_id),
	UNIQUE(teacher_id)
);

CREATE TABLE if not exists participant (
	participant_id INTEGER NOT NULL DEFAULT nextval('participant_id_seq') PRIMARY KEY,
	mail varchar(64),
	school_module_id INTEGER,
	constraint fk_school_module FOREIGN KEY (school_module_id) REFERENCES school_module(school_module_id),
	UNIQUE(participant_id)
);


