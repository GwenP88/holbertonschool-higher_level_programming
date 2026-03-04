-- Script that creates the database hbtn_0d_2 and the user user_0d_2.
-- If user or database amready exists, script should not fail.
-- Create the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create the user user_0d_2 (password should be set to user_0d_2_pwd)
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grant all privileges on the MySQL server to user_0d_2
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
