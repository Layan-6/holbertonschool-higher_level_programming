-- Lists all records of second_table excluding rows where name is NULL
-- Results display score and name (in this order)
-- Records listed by descending score
-- Database name is passed as argument to mysql command
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
