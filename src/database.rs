use diesel::pg::PgConnection;

pub struct PgDatabase {
    connection: PgConnection    
}


impl PgDatabase {
    pub fn new(database_url: String) -> Self {
        Self {
            connection: PgConnection::establish(&database_url)
        }
    }

    pub fn getConnection(&self) -> PgConnection {
        &self.connection
    }
}

