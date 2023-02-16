<<<<<<< HEAD
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, "NULL") AS genre_id
=======
--  a script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL') AS genre_id
>>>>>>> f4b439bc05544df5888008f0ab4effb04b6aad5d
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, genre_id ASC;
