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
    let participant_crud = ParticipantCRUD::new(database);

    let insert = vec!(
       NewParticipant::new("r@gmail.com".to_owned(), 0));
    println!("{:?}", participant_crud.insert(insert).unwrap());

    println!("Server running");
    gotham::start("127.0.0.1:8080", || Ok(router()));
}
