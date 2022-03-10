-- Write a script that lists all shows contained in the database
SELECT s.title, g.genre_id AS genre_id FROM tv_shows AS s LEFT JOIN tv_show_genres AS g ON g.show_id = s.id ORDER BY s.title, g.genre_id;
