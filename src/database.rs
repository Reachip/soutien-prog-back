use diesel::pg::PgConnection;
use diesel::Connection;

pub struct PgDatabase {
    pub connection: PgConnection
}


impl PgDatabase {
    pub fn new(database_url: String) -> Self {
        Self {
            connection: PgConnection::establish(&database_url).unwrap()
        }
    }
}