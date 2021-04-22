import sqlite3

#conn = sqlite3.connect(':memory')
conn = sqlite3.connect('customer.db')

# Create a custor
c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    )""")

# Insert a record
c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'derp@hehe.com')")

# Insert multiple records
many_customers = [('Wes', 'Brown', 'wes@brown.com'),
                 ('derp', 'heeyo', 'breakdown@derp.com'),
                 ('Hehe', 'Testerino', 'testy@derp.com')
                ]

c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Query the Database
c.execute("SELECT * FROM customers")
c.fetchone()
c.fetchmany(3)
print(c.fetchall())

# Formatted results
c.execute("SELECT * FROM customers WHERE last_name = 'Elder'")

# Primary key row-id
 c.execute("SELECT rowid, * from customers")

items = c.fetchall();

for item in items:
    print(item)

# Datatypes
# NULL - Does it exist or does it not exist
# INTEGER - A whole number
# REAL - Decimal
# TEXT
# BLOB - Stored exactly as it is, e.g. .png, .mp3

# Commit to the database
conn.commit()

# Close the connection
conn.close()
