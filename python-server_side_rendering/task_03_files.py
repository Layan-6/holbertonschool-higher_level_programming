#!/usr/bin/python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""
from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_products():
    """Read products from JSON file"""
    json_file = 'products.json'
    
    if not os.path.exists(json_file):
        return []
    
    try:
        with open(json_file, 'r') as f:
            # Handle both formats: list of objects or single object with products key
            data = json.load(f)
            
            if isinstance(data, dict) and 'products' in data:
                return data['products']
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
                # Convert id to int and price to float if possible
                row_copy = {}
                for key, value in row.items():
                    key = key.strip()
                    value = value.strip() if isinstance(value, str) else value
                    
                    if key == 'id' and value.isdigit():
                        row_copy[key] = int(value)
                    elif key == 'price':
                        try:
                            row_copy[key] = float(value)
                        except ValueError:
                            row_copy[key] = value
                    else:
                        row_copy[key] = value
                products.append(row_copy)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    
    return products

def filter_product_by_id(products, product_id):
    """Filter products by ID"""
    for product in products:
        # Try to match id as string or integer
        if str(product.get('id', '')) == str(product_id):
            return product
    return None

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

@app.route('/products')
def products():
    """Display products from JSON or CSV based on query parameters"""
    # Get query parameters
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Initialize variables
    products_list = []
    error_message = None
    filtered_product = None
    
    # Read data based on source
    if source == 'json':
        products_list = read_json_products()
    elif source == 'csv':
        products_list = read_csv_products()
    else:
        # Invalid source
        error_message = f"Wrong source '{source}'. Please use 'json' or 'csv'."
        return render_template('product_display.html', 
                             error_message=error_message,
                             source=source)
    
    # Filter by ID if provided
    if product_id:
        filtered_product = filter_product_by_id(products_list, product_id)
        if not filtered_product:
            error_message = f"Product with ID '{product_id}' not found."
            return render_template('product_display.html',
                                 error_message=error_message,
                                 source=source,
                                 product_id=product_id)
    
    # If no products found (empty file)
    if not products_list and not error_message:
        error_message = f"No products found in {source.upper()} file."
    
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

@app.route('/items')
def items():
    """Render the items page"""
    # You can keep this or adapt it
    return "Items page - See task_02_logic.py for implementation"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
