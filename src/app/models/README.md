In this project I decided to load CSVs in the postregres sql database at PostgresSQL docker image pull. 
That's means the tables and columns already have been created and typed with the SQL scripts. 
The pydandic models must match the same format for each columns. 
In a normal case, models are defining the columns type and migrations tools like Alembic are used to apply changes. 
