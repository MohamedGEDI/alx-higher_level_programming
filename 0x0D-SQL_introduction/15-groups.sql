-- group same alues
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score;
