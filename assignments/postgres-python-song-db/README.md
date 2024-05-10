
# SparkifyDB ETL Project

This project focuses on basic data modeling using python to
perform basic database and table creation, table population
as well as exploring the ETL cycle of json data.

This is really broken up into only two parts and a few small tasks.

Those are, in order:
* Create an ER diagram of our sparkifyDB.
* Making our create table and insert statements in `sql_queries.py`
* Run `create_tables.py`
* Walking through basic ETL in a jupyter notebook `etl.ipynb`
    * Transplanting that ETL into a single python script in `etl.py`
 
For the last three things we test each step of the process with `test.py`

### STEPS TO RUN
In a terminal do:
`%run create_tables.py`
`%run etl.py`
Then use test.ipynb to confirm the database was properly populated.


### EXPLORATION
The scenario of this project is that a music streaming service startup called Sparkify wants to better understand the listening patterns of their users. They need a database to facilitate easy exploration of their user data, which is currently stored in JSON logs in a slightly messy manner.

That mess takes the form of two datasets, one for song data and one for logs. We're given the structure of the database, all of the data types, and really all of the hard parts in the instructions for the project.

While the instructions tell me to justfy the database design, I 
didn't define it--the project instructions and premade code precluded
any decision making. I likely wouldn't have broken the time table out.
It doesn't make a ton of sense to do so since any query generated from it would be duplicated by the database engine using an algorithm
that's better than O(n).

### ER DIAGRAM

For some reason this is right at the beginning in the instructions, which is fine. I suppose if the code we were given
had actually produced key relationships that would make doing this a little too easy. I used MDML and 
DBdiagram.io to generate this. I defined all of the relevant key relationships, and one that's irrelevant. I also elected to betray it looking like a normal star, and more of a comet with a tail.

<img src="SparkifyDB ER Diagram.png">