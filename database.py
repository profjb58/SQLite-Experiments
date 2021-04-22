import sqlite3 

# Create a table if it dosen't already exist
def create_table():
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS customers (
            first_name text,
            last_name text,
            email text
        )""")
    conn.commit()
    conn.close()

def add_many(many_customers):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)
    conn.commit()
    conn.close()
    
def add(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    
    conn.commit()
    conn.close()

# Query the DB and Return All Records
def show_all():
    #conn = sqlite3.connect(':memory')
    conn = sqlite3.connect('customer.db')

    # Create a cursor
    c = conn.cursor()
    
    # Query The Database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit the command
    conn.commit()
    # Close our connection
    conn.close()









