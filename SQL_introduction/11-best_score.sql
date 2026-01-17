-- Lists all records with score >= 10 in second_table
-- Results display score then name, ordered by score (top first)
-- Database name is passed as argument to mysql command
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
