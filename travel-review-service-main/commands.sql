drop table if exists review cascade;



-- auto-generated definition
create table review
(
    id      int auto_increment
        primary key,
    review  varchar(255)                        null,
    rating  enum ('0', '1', '2', '3', '4', '5') not null,
    user_id varchar(255)                                not null,
    city    varchar(48)                         not null
);

-- Add Values -----



INSERT INTO
	review(review, rating, user_id, city)
VALUES
	('Great place to visit for family! :)', '4','10001','london'),
    ('Worst place I have ever visited :(', '2', '10002','new york'),
    ('It was ok place. Wont go again. :D', '3','10003','sydney'),
    ('Saw the bean and it was fun.Lot of activity', '4','10004','chicago'),
    ('Good place for couples and tourists. :XX', '5','10005','paris'),
    ('Awesome weather!!!!', '3','10006','los angeles'),
    ('Very chilly weather. But enjoyable.', '4','10005','glasgow'),
    ('nice place to visit n fall. :<', '0','10004','paris'),
    ('Great place ot visit year round :>', '3','10003','miami'),
    ('Very dull place!! :P', '3','10003','london'),
    ('Enjoyed my stay. Recommend everyone to go!! :D', '5', '10001' ,'chicago')