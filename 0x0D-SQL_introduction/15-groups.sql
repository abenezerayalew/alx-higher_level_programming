-- A script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

SELECT score FROM second_table GROUP BY score HAVING COUNT(id)>1;