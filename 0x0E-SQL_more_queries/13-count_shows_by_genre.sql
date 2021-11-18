-- list by genres
SELECT g.name AS genre, COUNT(tvg.genre_id) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres tvg ON tvg.genre_id = g.id
GROUP BY tvg.genre_id
ORDER BY number_of_shows DESC
