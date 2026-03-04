-- Script that creates the table force_name on your MySQL server.
-- If user or database amready exists, script should not fail.
-- Select the database hbtn_0d_2
USE hbtn_0d_2;
-- Create the table force_name (id INT, name VARCHAR (256) can't be null)
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
