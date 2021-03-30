create database app;
use app;

Create table stories (
id int auto_increment,
header Varchar(250) not null,
story_description text,
start_date date,
end_date date,
primary key(id) ) ;


create table to_dos(
id int auto_increment,
header Varchar(250) not null,
to_do_description text,
story_id int not null,
to_do_status int not null,
start_date datetime,
end_date datetime,
primary key(id) );



