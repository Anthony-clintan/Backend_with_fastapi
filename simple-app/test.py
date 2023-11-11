import sqlite3

# Your FastAPI code here...

# Example: Connecting to an SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Example: Creating a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
''')

# Example: Inserting data
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', ('Product A', 19.99))
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', ('Product B', 29.99))

# Example: Querying data
cursor.execute('SELECT * FROM products')
products = cursor.fetchall()
print(products)

# Don't forget to commit the changes and close the connection when done
conn.commit()
conn.close()
