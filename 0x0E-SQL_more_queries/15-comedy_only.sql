-- list genres of dexter
SELECT tvs.title FROM tv_shows
INNER JOIN tv_show_genres tvg
ON tvg.genre_id = tvs.id
INNER JOIN tv_genre g
ON tvg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY tvs.title ASC
