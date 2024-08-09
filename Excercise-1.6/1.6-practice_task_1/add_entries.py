import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',  # Replace with your actual MySQL username
    passwd='password',  # Replace with your actual MySQL password
    database='my_database'  # Replace with your actual database name
)

# Create a cursor object
cursor = conn.cursor()

# Create the stock table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock (
        item_id INT PRIMARY KEY AUTO_INCREMENT,
        item_name VARCHAR(50),
        manufacturer VARCHAR(100),
        price FLOAT,
        quantity INT
    )
""")

# Insert entries into the stock table, omitting 'item_id' to allow AUTO_INCREMENT
cursor.execute("""
    INSERT INTO stock (item_name, manufacturer, price, quantity)
    VALUES ('Paper', 'Georgia-Pacific Corp.', 35, 40)
""")

cursor.execute("""
    INSERT INTO stock (item_name, manufacturer, price, quantity)
    VALUES ('Butter', 'Organic Valley', 18, 37)
""")

cursor.execute("""
    INSERT INTO stock (item_name, manufacturer, price, quantity)
    VALUES ('Pencils', 'Staedtler', 17, 55)
""")

# Commit the transaction
conn.commit()

# Retrieve and display the data to verify insertion
cursor.execute("SELECT * FROM stock")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
cursor.close()
conn.close()
