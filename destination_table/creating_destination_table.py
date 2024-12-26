
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
                  CREATE TABLE poducts_orders (
                order_id SERIAL PRIMARY KEY,      
                customer_id INT,
                product_id IN,
                quantity INT,
                order_date TIMESTAMP,
                price FLOAT,
                category VARCHAR(255),
                rate FLOAT,
                count INT 
            );
    """)
    conn.commit()
    print("Table 'poducts_orders' created successfully.")
except psycopg2.Error as e:
    print(f"Error creating table: {e}")
    cursor.close()
    conn.close()
    print("Database connection closed.")

