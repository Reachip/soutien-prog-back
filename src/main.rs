mod handlers;

use handlers::hello;

use gotham::router::builder::DrawRoutes;
use gotham::router::builder::DefineSingleRoute;


fn router() -> gotham::router::Router {
    gotham::router::builder::build_simple_router(|route| {
        route.get("/hello").to(hello::say_hello);
    })
}

fn main() {
    gotham::start("127.0.0.1:8080", || Ok(router()));
}
