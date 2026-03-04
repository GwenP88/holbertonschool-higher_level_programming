-- Script that creates  the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- If the table and/or the database already exists, script should not fail.
-- Create the database hbtn_0d_usa.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create the table cities (id INT with primary key, auto increment and not null, state_id INT not null, name VARCHAR (256) not null).
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id));
