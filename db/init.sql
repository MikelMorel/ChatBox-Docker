CREATE DATABASE chatlog;
use chatlog;

CREATE TABLE 'log' (
    'date' varchar(200) NOT NULL,
    'userName' varchar(200),
    'message' varchar(250),
);

insert into 'log' values('testuser','testmsg');

