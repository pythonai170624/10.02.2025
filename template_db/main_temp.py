from tinydb import Query

from sqlite_query import SqliteSelectQuery
from template_db.postgres_query import PostgresQuery
from template_db.tinydb_query import TinydbSelectQuery

print('-' * 25 , 'SQLITE')
sqlite_query = SqliteSelectQuery("example.db")
sqlite_query.run("SELECT * FROM USERS")  # run the template
print(sqlite_query.get_query_result())

sqlite_query.run("SELECT * FROM USERS where age > 25")  # run the template
print(sqlite_query.get_query_result())

print('-' * 25 , 'POSTGRESQL')
postgres_query = PostgresQuery(db_name="postgres", user="postgres",
    password="admin", host="localhost", port="5432")

postgres_query.run("SELECT * FROM USERS ")  # run the template
print(postgres_query.get_query_result())

print('-' * 25 , 'TINY_DB')
tinydb_query = TinydbSelectQuery("db.json")
tinydb_query.run(Query().age > 20)  # run the template
print(tinydb_query.get_query_result())

tinydb_query.run(Query().name == 'Alice')  # run the template
print(tinydb_query.get_query_result())