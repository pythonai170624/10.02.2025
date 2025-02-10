from tinydb import TinyDB, Query

# Initialize database
db = TinyDB('db.json')

# # Insert records
# db.insert({'name': 'Alice', 'age': 25})
# db.insert({'name': 'Bob', 'age': 30})

# Query data
User = Query()
results = db.search(User.age > 20)

print("Users:", results)

# Close database
db.close()
