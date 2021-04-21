#[macro_use]
extern crate diesel;

mod handlers;
mod database;
mod crud;
mod model;
mod schema;

use handlers::hello;
use crud::*;
use model::*;
use gotham::router::builder::DrawRoutes;
use gotham::router::builder::DefineSingleRoute;
use diesel::Insertable;
use crate::schema::participant::dsl::participant;
use gotham::hyper::header::Values;
use diesel::query_builder::ValuesClause;


fn router() -> gotham::router::Router {
    gotham::router::builder::build_simple_router(|route| {
        route.get("/hello").to(hello::say_hello);
    })
}

fn main() {
    let database = database::PgDatabase::new("postgres://postgres:@localhost/soutienprog".to_owned());

    let participant_crud = ParticipantCRUD::new(&database);
    let school_module_crud = SchoolModuleCRUD::new(&database);

    let insert_participant = vec!(
       NewParticipant::new("r@gmail.com".to_owned(), 1)
    );


    let insert_school_module = vec!(
      NewSchoolModule::new("Réseau".to_string(), "M2102".to_string())
    );

    println!("{:?}", school_module_crud.insert(insert_school_module).unwrap());
    println!("{:?}", participant_crud.insert(insert_participant).unwrap());

    println!("Server running");
    gotham::start("127.0.0.1:8080", || Ok(router()));
}
