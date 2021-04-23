use gotham::state::State;

const HW: &'static str = "Hello World";

pub fn create_courses(state: State) -> (State, &'static str) {
    (state, HW)
}

pub fn search_courses(state: State) -> (State, &'static str) {
    (state, HW)
}