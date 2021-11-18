-- list genres of dexter
SELECT g.name FROM tv_genres g
INNER JOIN tv_show_genres tvg
ON tvg.genre_id = g.id
INNER JOIN tv_shows tvs
ON tvg.show_id = tvs.id
WHERE tvs.title = 'Dexter'
ORDER BY g.name ASC
