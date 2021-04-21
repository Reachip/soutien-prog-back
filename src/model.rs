use crate::schema::*;
use diesel::Queryable;

#[derive(Queryable, Insertable)]
#[table_name="courses"]
pub struct Courses {
    courses_id: i32,
    teacher_id: i32,
    school_module_id: i32
}

#[derive(Queryable, Insertable, Debug)]
#[table_name="participant"]
pub struct Participant {
    participant_id: i32,
    mail: String,
    school_module_id: i32
}


#[derive(Insertable, Debug)]
#[table_name="participant"]
pub struct NewParticipant {
    mail: String,
    school_module_id: i32
}

impl NewParticipant {
    pub fn new(mail: String, school_module_id: i32) -> Self {
        Self {
            mail,
            school_module_id
        }
    }
}

impl Participant {
    pub fn new(participant_id: i32, mail: String, school_module_id: i32) -> Self {
        Self {
            participant_id,
            mail,
            school_module_id
        }
    }
}

/*
#[derive(Queryable)]
pub struct SchoolModule {
    school_module_id: i32
    module_name: String,
    module_number: String
}*/