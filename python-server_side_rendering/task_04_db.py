#!/usr/bin/python3
"""
Task 4: Extending Dynamic Data Display to Include SQLite in Flask
"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def read_json_products():
    """Read products from JSON file"""
    json_file = 'products.json'
    
    if not os.path.exists(json_file):
        return []
    
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            
            # Handle different JSON structures
            if isinstance(data, dict):
                if 'products' in data:
                    return data['products']
                else:
                    return []
            elif isinstance(data, list):
                return data
            else:
                return []
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

def read_csv_products():
    """Read products from CSV file"""
    csv_file = 'products.csv'
    
    if not os.path.exists(csv_file):
        return []
    
    products = []
    try:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Clean and convert data
                cleaned_row = {}
                for key, value in row.items():
                    key_clean = key.strip().lower()
                    value_clean = value.strip() if isinstance(value, str) else value
                    
                    if key_clean == 'id' and value_clean.isdigit():
                        cleaned_row[key_clean] = int(value_clean)
                    elif key_clean == 'price':
                        try:
                            # Remove $ sign if present
                            if isinstance(value_clean, str):
                                value_clean = value_clean.replace('$', '').replace(',', '')
                            cleaned_row[key_clean] = float(value_clean)
                        except ValueError:
                            cleaned_row[key_clean] = value_clean
                    else:
                        cleaned_row[key_clean] = value_clean
                products.append(cleaned_row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    
    return products

def read_sql_products():
    """Read products from SQLite database"""
    db_file = 'products.db'
    
    if not os.path.exists(db_file):
        print(f"Database file '{db_file}' not found")
        return []
    
    products = []
    try:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name, category, price FROM Products ORDER BY id")
        rows = cursor.fetchall()
        
        # Convert rows to list of dictionaries
        for row in rows:
            product = {
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            }
            products.append(product)
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return []
    except Exception as e:
        print(f"Error reading from database: {e}")
        return []
    
    return products

def filter_product_by_id(products, product_id):
    """Filter products by ID"""
    if not product_id:
        return None
    
    for product in products:
        prod_id = product.get('id')
        if prod_id is not None and str(prod_id) == str(product_id):
            return product
    return None

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQL based on query parameters"""
    # Get query parameters
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Initialize variables
    products_list = []
    error_message = None
    filtered_product = None
    
    # Check for invalid source
    valid_sources = ['json', 'csv', 'sql']
    if source not in valid_sources:
        error_message = "Wrong source"
        return render_template('product_display.html', 
                             error_message=error_message,
                             source=source)
    
    # Read data based on source
    if source == 'json':
        products_list = read_json_products()
    elif source == 'csv':
        products_list = read_csv_products()
    elif source == 'sql':
        products_list = read_sql_products()
    
    # Check if data was loaded
    if not products_list:
        if source == 'sql':
            error_message = "Database error or no products found"
        else:
            error_message = "No data available"
        
        return render_template('product_display.html',
                             error_message=error_message,
                             source=source)
    
    # Filter by ID if provided
    if product_id:
        filtered_product = filter_product_by_id(products_list, product_id)
        if not filtered_product:
            error_message = "Product not found"
            return render_template('product_display.html',
                                 error_message=error_message,
                                 source=source,
                                 product_id=product_id)
    
    # Render template with data
    return render_template('product_display.html',
                         products=products_list,
                         filtered_product=filtered_product,
                         source=source,
                         product_id=product_id,
                         error_message=error_message)

@app.route('/about')
def about():
    """Render the about page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Render the contact page"""
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
