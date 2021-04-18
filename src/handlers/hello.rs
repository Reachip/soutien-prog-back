use gotham::state::State;

const HW: &'static str = "Hello World";

pub fn say_hello(state: State) -> (State, &'static str) {
    (state, HW)
}
