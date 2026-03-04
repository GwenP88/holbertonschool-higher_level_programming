-- Script that creates the table force_name on your MySQL server.
-- If user or database already exists, script should not fail.
-- Create the table force_name (id INT, name VARCHAR (256) can't be null)
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
