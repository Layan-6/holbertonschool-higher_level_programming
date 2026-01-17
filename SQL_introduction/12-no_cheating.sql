-- Updates the score of Bob to 10 in second_table
-- Uses only the name field, not Bob's id value
-- Database name is passed as argument to mysql command
UPDATE second_table SET score = 10 WHERE name = 'Bob';
