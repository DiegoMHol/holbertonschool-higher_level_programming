--  a script that lists all records with a score >= 10 in the table second_table
SELECT score, name FROM second_table HAVING score >= 10 ORDER BY score DESC
