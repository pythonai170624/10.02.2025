import time

import psycopg2

# Step 1: Connect to the PostgreSQL database

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)
print("Database connection successful.")

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Create a table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     age INTEGER NOT NULL,
#     email VARCHAR(150) UNIQUE NOT NULL
# )
# """)
# conn.commit()
# print("Table 'users' created successfully.")
#
# try:
#     # Step 4: Insert data into the table
#     cursor.execute("""
#     INSERT INTO users (name, age, email)
#     VALUES (%s, %s, %s)
#     """, ("Alice", 25, "alice@example.com"))
#
#     cursor.execute("""
#     INSERT INTO users (name, age, email)
#     VALUES (%s, %s, %s)
#     """, ("Bob", 30, "bob@example.com"))
#
#     # Commit the changes
#     conn.commit()
#     print("Data inserted successfully.")
# except:
#     print('Insert error')
#     cursor = conn.cursor()

# Step 5: Select and display the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Users in the database:")
result = []
for row in rows:
    result.append(row)
print(result)

conn.close()

