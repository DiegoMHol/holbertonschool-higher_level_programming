-- Write a script that creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS cities(id int NOT NULL AUTO_INCREMENT, state_id int NOT NULL, name varchar(256) NOT NULL, PRIMARY KEY(id), FOREIGN KEY(state_id) REFERENCES states(id));
