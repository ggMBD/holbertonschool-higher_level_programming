-- script that creates the MySQL server user user_0d_1.

CREATE USER IF NOT EXISTS
    'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
-- set all privileges
GRANT ALL PRIVILEGES ON *.*
    TO 'user_0d_1'@'localhost'
    WITH GRANT OPTION;
FLUSH PRIVILEGES;
