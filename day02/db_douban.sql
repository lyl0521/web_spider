CREATE DATABASE db_douban;

use db_douban;

drop table if exists db_douban.movie;
create table db_douban.movie(
    id int auto_increment primary key ,
    name varchar(255) not null,
    star float not null,
    comment varchar(255) not null ,
    url varchar(255) not null ,
    director varchar(255) not null,
    actor varchar(255) not null
);

select * from db_douban.movie