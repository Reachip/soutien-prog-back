use diesel;
use crate::database::PgDatabase;
use crate::model::{Participant, NewParticipant};

use crate::schema::participant::dsl::*;
use diesel::{RunQueryDsl, QueryResult, Insertable};
use crate::schema;

pub struct ParticipantCRUD {
    database: PgDatabase
}

pub trait CRUD {
    fn new(database: PgDatabase) -> Self where Self : Sized;
    fn insert <T>(&self, values: Vec<impl Insertable<T>>) -> std::result::Result<Participant, diesel::result::Error>;
    fn delete(&self, values: Vec<Participant>);
}

impl CRUD for ParticipantCRUD {
    fn new(database: PgDatabase) -> Self where Self : Sized {
        Self { database }
    }

    fn insert <T> (&self, values: Vec<impl Insertable<T> >) -> std::result::Result<Participant, diesel::result::Error> {
        diesel::insert_into(participant)
            .values(values)
            .get_result::<Participant>(&self.database.connection)
    }

    fn delete(&self, values: Vec<Participant>) {

    }
}