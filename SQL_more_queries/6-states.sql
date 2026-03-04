-- Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- If the table and/or the database already exists, script should not fail.
-- Create the database hbtn_0d_usa.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa.
-- Create the table unique_id (id INT with default value 1 and must be unique, name VARCHAR (256)).
CREATE TABLE IF NOT EXISTS states  (id INT PRIMARY KEY, name VARCHAR(256) NOT NULL);
