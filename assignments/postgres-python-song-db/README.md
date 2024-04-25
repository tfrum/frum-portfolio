# CREATE TABLES
So here are our instructions
1. Write CREATE statements in sql_queries.py to create each table.
2. Write DROP statements in sql_queries.py to drop each table if it exists.
3. Run create_tables.py to create your database and tables.
4. Run test.ipynb to confirm the creation of your tables with the correct columns. Make sure to click "Restart kernel" to close the connection to the database after running this notebook.

We'll start at step 1:
We need to write some CREATE and DROP statements.
We need to make 5 tables: songplays, users, songs, artists, time. 
They provide the keys for these tables in part 3 of the project page.

However, we have an issue. I don't want to use Udacity's unintuitive Jupyter workspace *and* the create_tables.py file references databases that I don't have locally.