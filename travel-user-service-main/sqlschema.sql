use user_service;

-- Drop table
DROP TABLE IF EXISTS user_service.user;
DROP TABLE IF EXISTS user_service.trips;


create table user_service.user
(
    user_id         varchar(255) primary key,
    email           varchar(128) not null,
    username        varchar(128) not null
);

create table user_service.trips
(
    trip_id     int auto_increment primary key,
    user_id     varchar(255),
    foreign key (user_id) references user_service.user (user_id)
);




