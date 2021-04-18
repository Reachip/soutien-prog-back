table! {
    courses (courses_id) {
        courses_id -> Int4,
        teacher_id -> Nullable<Int4>,
        school_module_id -> Nullable<Int4>,
    }
}

table! {
    participant (participant_id) {
        participant_id -> Int4,
        mail -> Nullable<Varchar>,
        school_module_id -> Nullable<Int4>,
    }
}

table! {
    school_module (school_module_id) {
        school_module_id -> Int4,
        module_name -> Nullable<Varchar>,
        module_number -> Nullable<Varchar>,
    }
}

table! {
    teacher (teacher_id) {
        teacher_id -> Int4,
        username -> Nullable<Varchar>,
        mail -> Nullable<Varchar>,
        pwd -> Nullable<Varchar>,
    }
}

joinable!(courses -> teacher (teacher_id));

allow_tables_to_appear_in_same_query!(
    courses,
    participant,
    school_module,
    teacher,
);
