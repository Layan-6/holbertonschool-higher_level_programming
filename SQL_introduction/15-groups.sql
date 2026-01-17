-- Lists number of records with the same score in second_table
-- Displays: score, number of records (as number)
-- Sorted by number of records (descending)
-- Database name is passed as argument to mysql command
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
