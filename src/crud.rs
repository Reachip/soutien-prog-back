use diesel;
use crate::database::PgDatabase;
use crate::model::{Participant, NewParticipant, Courses, NewCourses, NewSchoolModule, SchoolModule};

use crate::schema::participant::dsl::*;
use diesel::{RunQueryDsl, QueryResult, Insertable};
use crate::schema;
use crate::schema::courses::dsl::courses;
use crate::schema::school_module::dsl::school_module;

pub struct ParticipantCRUD<'a> {
    database: &'a PgDatabase
}

pub struct CoursesCRUD<'a> {
    database: &'a PgDatabase
}

pub struct SchoolModuleCRUD<'a> {
    database: &'a PgDatabase
}


impl<'a> SchoolModuleCRUD<'a> {
    pub fn new(database: &'a PgDatabase) -> Self where Self: Sized {
        Self { database }
    }

    pub fn insert(&self, values: Vec<NewSchoolModule>) -> std::result::Result<SchoolModule, diesel::result::Error> {
        diesel::insert_into(school_module)
            .values(values)
            .get_result::<SchoolModule>(&self.database.connection)
    }

    fn delete(&self, values: Vec<NewSchoolModule>) {}
}

impl<'a> CoursesCRUD<'a> {
    pub fn new(database: &'a PgDatabase) -> Self where Self: Sized {
        Self { database }
    }

    pub fn insert(&self, values: Vec<NewCourses>) -> std::result::Result<Courses, diesel::result::Error> {
        diesel::insert_into(courses)
            .values(values)
            .get_result::<Courses>(&self.database.connection)
    }

    fn delete(&self, values: Vec<NewCourses>) {}
}

impl<'a> ParticipantCRUD<'a> {
    pub fn new(database: &'a PgDatabase) -> Self where Self: Sized {
        Self { database }
    }

    pub fn insert(&self, values: Vec<NewParticipant>) -> std::result::Result<Participant, diesel::result::Error> {
        diesel::insert_into(participant)
            .values(values)
            .get_result::<Participant>(&self.database.connection)
    }

    fn delete(&self, values: Vec<NewParticipant>) {}
}