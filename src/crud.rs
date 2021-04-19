use diesel;

use crate::database::PgDatabase;
use crate::schema::participant::dsl::*;

pub struct ParticipantCRUD {
    database: PgDatabase
}

trait CRUD {
    fn new(database: PgDatabase) -> Self where Self : Sized;
    fn insert(&self, values: Vec<Participant>);
    fn delete(&self, values: Vec<Participant>);
}

/*
impl CRUD for ParticipantCRUD {
    fn new(database: PgDatabase) -> Self where Self : Sized {
        Self {
            database
        }
    }

    fn insert(&self, values: )   {
        diesel::insert_into()
            .values(values)
            .execute(&self.database.getConnection());
    }

    fn delete(&self, values: Vec<&'a str>) {

    }
}
*/