import sqlite3

# Step 1: Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("example.db")

# Step 2: Create a cursor object to execute SQL commands
cursor = conn.cursor()
#
# # Step 3: Create a table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER NOT NULL,
#     email TEXT UNIQUE NOT NULL
# )
# """)
# print("Table 'users' created successfully.")
#
# # Step 4: Insert data into the table
# cursor.execute("""
# INSERT INTO users (name, age, email)
# VALUES (?, ?, ?)
# """, ("Alice", 25, "alice@example.com"))
#
# cursor.execute("""
# INSERT INTO users (name, age, email)
# VALUES (?, ?, ?)
# """, ("Bob", 30, "bob@example.com"))
#
# # Commit the changes to the database
# conn.commit()
# print("Data inserted successfully.")

# Step 5: Select and display the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Users in the database:")
result = []
for row in rows:
    result.append(row)
print(result)

# Step 6: Close the connection
conn.close()
print("Database connection closed.")
