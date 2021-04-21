table! {
    courses (courses_id) {
        courses_id -> Int4,
        teacher_id -> Int4,
        school_module_id -> Int4,
    }
}

table! {
    participant (participant_id) {
        participant_id -> Int4,
        mail -> Varchar,
        school_module_id -> Int4,
    }
}

table! {
    school_module (school_module_id) {
        school_module_id -> Int4,
        module_name -> Varchar,
        module_number -> Varchar,
    }
}

table! {
    teacher (teacher_id) {
        teacher_id -> Int4,
        username -> Varchar,
        mail -> Varchar,
        pwd -> Varchar,
    }
}

joinable!(courses -> teacher (teacher_id));

allow_tables_to_appear_in_same_query!(
    courses,
    participant,
    school_module,
    teacher,
);
