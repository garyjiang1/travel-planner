-- mysql -uroot -p<commands.sql

DROP DATABASE IF EXISTS travel_service;

CREATE DATABASE IF NOT EXISTS travel_service;

use travel_service;

drop table if exists Itinerary cascade;

-- auto-generated definition
create table Itinerary
(
    itinerary_id int auto_increment primary key,
    total_cost float not null
);



INSERT INTO Itinerary(total_cost)
VALUES (500.10), (465.13), (222.45), (1000.00), (800.50), (675.15), (615.25), (800.50), (675.15), (615.25);

drop table if exists Travel cascade;

create table Travel (
    travel_id int auto_increment primary key,
    itinerary_id int,
    review_id int not null,
    origin varchar(255) not null,
    destination varchar(255) not null,
    origin_code varchar(225) not null,
    destination_code varchar(225) not null,
    departure_time datetime not null,
    arrival_time datetime not null,
    airline_name varchar(255) not null,
    flight_num varchar(255) not null,
    cost float not null
);
alter table Travel add constraint s_id foreign key(itinerary_id) references Itinerary(itinerary_id);

INSERT INTO Travel(itinerary_id, review_id, origin, destination, origin_code, destination_code, departure_time, arrival_time, airline_name, flight_num, cost)
VALUES (1, 100, 'London', 'New York', 'LHR', 'JFK', '2023-02-14T21:05:00', '2023-02-15T09:30:00', 'JetBlue', '1001', 800),
(2, 101, 'Paris', 'London', 'CDG', 'LHR', '2023-02-18T21:05:00', '2023-02-19T09:30:00', 'British Airway', '1002', 1000),
(3, 102, 'San Francisco', 'New York', 'SFO', 'JFK', '2023-02-13T21:05:00', '2023-02-14T09:30:00', 'JetBlue', '1007', 500),
(4, 103, 'Madrid', 'London', 'MAD', 'LHR', '2023-02-12T21:05:00', '2023-02-13T09:30:00', 'Iberia', '1034', 750),
(5, 104, 'Tokyo', 'New York', 'HND', 'JFK', '2023-01-14T21:05:00', '2023-01-15T09:30:00', 'Iberia', '1022', 900),
(6, 105, 'New York', 'Madrid', 'JFK', 'MAD', '2023-03-14T21:05:00', '2023-03-15T09:30:00', 'British Airways', '1034', 850),
(7, 106, 'New York', 'Philadelphia', 'JFK', 'PHL', '2023-02-22T21:05:00', '2023-02-23T23:30:00', 'JetBlue', '1001', 800),
(8, 107, 'London', 'New York', 'LHR', 'JFK', '2023-02-08T21:05:00', '2023-02-09T09:30:00', 'British Airways', '1056', 700),
(9, 108, 'New York', 'London', 'JFK', 'LHR', '2023-04-14T21:05:00', '2023-04-15T09:30:00', 'JetBlue', '1089', 600),
(10, 109, 'New York', 'Berlin', 'JFK', 'BML', '2023-05-14T21:05:00', '2023-05-15T09:30:00', 'British Airways', '1046', 1000);
