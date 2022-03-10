-- Write a script that lists all the cities of California
SELECT cities.id, cities.name FROM cities
WHERE (SELECT id FROM states WHERE states.name = "California") = cities.state_id ORDER BY cities.id ASC;
