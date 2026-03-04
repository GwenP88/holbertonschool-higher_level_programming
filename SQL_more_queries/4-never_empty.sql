-- Script that creates the table id_not_null on your MySQL server.
-- If the table already exists, script should not fail.
-- Create the table id_not_null (id INT with default value 1, name VARCHAR (256))
CREATE TABLE IF NOT EXISTS id_not_null (id INT NOT NULL DEFAULT 1, name VARCHAR(256));
