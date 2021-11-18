-- list genres of dexter
SELECT tvs.title, g.name FROM tv_shows tvs
LEFT JOIN tv_show_genres tvg
ON tvg.show_id = tvs.id
LEFT JOIN tv_genres g
ON tvg.genre_id = g.id
ORDER BY tvs.title, g.name ASC
