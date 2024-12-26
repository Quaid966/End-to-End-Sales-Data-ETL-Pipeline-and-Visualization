
import psycopg2
from faker import Faker
import random

# Initialize Faker
faker = Faker()

# Database connection
try:
    conn = psycopg2.connect("dbname=database_name user=postgres password=your_password")
    print("Connection successfully established.")
except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")
    exit()

cursor = conn.cursor()

# Create the order table
try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS "order" (
            order_id SERIAL PRIMARY KEY,
            customer_id INT NOT NULL,
            product_id INT NOT NULL,                       
            quantity INT NOT NULL,             
            order_date TIMESTAMP NOT NULL
        );
    """)
    print("Table 'order' created successfully.")
except psycopg2.Error as e:
    print(f"Error creating table: {e}")
    conn.close()
    exit()

# Insert 400 fake transactions
try:
    for _ in range(400):
        customer_id = random.randint(1, 100)  # Assuming 100 customers exist
        product_id = random.randint(1, 20)   # Assuming 20 products exist
        quantity = random.randint(1, 10)     # Random quantity between 1 and 10
        order_date = faker.date_time_this_year()

        cursor.execute(
            """
            INSERT INTO "order" (customer_id, product_id, quantity, order_date)
            VALUES (%s, %s, %s, %s);
            """,
            (customer_id, product_id, quantity, order_date),
        )

    conn.commit()
    print("400 orders inserted successfully.")
except psycopg2.Error as e:
    print(f"Error inserting data: {e}")
    conn.rollback()  # Rollback in case of error

# Close the cursor and connection
cursor.close()
conn.close()
print("Database connection closed.")
