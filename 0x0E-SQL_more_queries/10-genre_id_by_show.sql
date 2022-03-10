i-- Import the database dump from hbtn_0d_tvshows
SELECT s.title, g.genre_id AS genre_id FROM tv_shows AS s RIGHT JOIN tv_show_genres AS g ON g.show_id = s.id ORDER BY s.title, g.genre_id;
