CREATE TABLE availabilities
(
    start timestamp with time zone not null,
    "end" timestamp with time zone not null
);

CREATE TABLE reservations
(
    start timestamp with time zone not null,
    "end" timestamp with time zone not null,
    title text not null,
    email character varying(320) not null
);
