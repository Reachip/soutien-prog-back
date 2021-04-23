use crate::schema::*;
use diesel::Queryable;
use chrono::NaiveDateTime;

#[derive(Queryable, Insertable)]
#[table_name = "courses"]
pub struct Courses {
    courses_id: i32,
    teacher_id: i32,
    school_module_id: i32,
    starting_at: NaiveDateTime,
    ending_at: NaiveDateTime
}

#[derive(Queryable, Insertable, Debug)]
#[table_name = "participant"]
pub struct Participant {
    participant_id: i32,
    mail: String,
    school_module_id: i32,
}


#[derive(Queryable, Insertable, Debug)]
#[table_name = "school_module"]
pub struct SchoolModule {
    school_module_id: i32,
    module_name: String,
    module_number: String,
}

#[derive(Insertable, Debug)]
#[table_name = "school_module"]
pub struct NewSchoolModule {
    module_name: String,
    module_number: String,
}

#[derive(Insertable, Debug)]
#[table_name = "participant"]
pub struct NewParticipant {
    mail: String,
    school_module_id: i32,
}

#[derive(Insertable, Debug)]
#[table_name = "courses"]
pub struct NewCourses {
    school_module_id: i32,
    starting_at: NaiveDateTime,
    ending_at: NaiveDateTime
}

impl NewSchoolModule {
    pub fn new(module_name: String, module_number: String) -> Self {
        Self { module_name, module_number }
    }
}

impl NewCourses {
    pub fn new(school_module_id: i32, starting_at: NaiveDateTime, ending_at: NaiveDateTime) -> Self {
        Self { school_module_id, starting_at, ending_at }
    }
}

impl NewParticipant {
    pub fn new(mail: String, school_module_id: i32) -> Self {
        Self { mail, school_module_id }
    }
}

impl Participant {
    pub fn new(participant_id: i32, mail: String, school_module_id: i32) -> Self {
        Self {
            participant_id,
            mail,
            school_module_id,
        }
    }
}