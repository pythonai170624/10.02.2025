from sqlite_query import SqliteSelectQuery
from template_db.postgres_query import PostgresQuery

print('-' * 25 , 'SQLITE')
sqlite_query = SqliteSelectQuery("example.db")
sqlite_query.run("SELECT * FROM USERS")  # run the template
print(sqlite_query.get_query_result())

sqlite_query.run("SELECT * FROM USERS where age > 25")  # run the template
print(sqlite_query.get_query_result())

postgres_query = PostgresQuery(db_name="postgres", user="postgres",
    password="admin", host="localhost", port="5432")

print('-' * 25 , 'POSTGRESQL')
postgres_query.run("SELECT * FROM USERS ")  # run the template
print(postgres_query.get_query_result())
