
CREATE DATABASE netflix_db;
drop database if exists netflix_db

DROP TABLE IF EXISTS netflix;
CREATE TABLE netflix
(
    show_id      VARCHAR(10),
    type         VARCHAR(20),
    title        VARCHAR(250),
    director     VARCHAR(550),          
    casts        VARCHAR(1050),
    country      VARCHAR(550),
    date_added   VARCHAR(55),
    release_year INT,
    rating       VARCHAR(15),
    duration     VARCHAR(50),
    listed_in    VARCHAR(250),
    description  VARCHAR(550)
);

select * from netflix_db.public.netflix n 
