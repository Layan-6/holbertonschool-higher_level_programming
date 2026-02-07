#!/usr/bin/python3
"""
Script to create and populate the SQLite database
"""
import sqlite3
import os

def create_database():
    """Create SQLite database with products table"""
    
    # Remove existing database file if exists
    if os.path.exists('products.db'):
        os.remove('products.db')
    
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create Products table
    cursor.execute("""
    CREATE TABLE Products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL
    )
    """)
    
    # Insert sample data
    products = [
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Wireless Mouse', 'Electronics', 29.99),
        (4, 'Notebook', 'Stationery', 8.49),
        (5, 'Desk Lamp', 'Home Goods', 24.99),
        (6, 'USB Cable', 'Electronics', 12.99),
        (7, 'Water Bottle', 'Accessories', 18.99),
        (8, 'Backpack', 'Accessories', 49.99)
    ]
    
    cursor.executemany("""
    INSERT INTO Products (id, name, category, price)
    VALUES (?, ?, ?, ?)
    """, products)
    
    conn.commit()
    conn.close()
    print("Database 'products.db' created successfully!")

if __name__ == '__main__':
    create_database()
