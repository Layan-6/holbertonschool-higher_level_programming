#!/usr/bin/python3
"""
Task 2: Creating a Dynamic Template with Loops and Conditions in Flask
"""
from flask import Flask, render_template
import json
import os

app = Flask(__name__)

def load_items_from_json():
    """Load items from JSON file"""
    json_file = 'items.json'
    
    # Check if JSON file exists
    if not os.path.exists(json_file):
        print(f"Warning: {json_file} not found. Using empty list.")
        return []
    
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            # Assuming the JSON has a key 'items' containing the list
            return data.get('items', [])
    except json.JSONDecodeError:
        print(f"Error: {json_file} contains invalid JSON. Using empty list.")
        return []
    except Exception as e:
        print(f"Error reading {json_file}: {e}")
        return []

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

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
    """Render the items page with dynamic content"""
    # Load items from JSON file
    items_list = load_items_from_json()
    
    # Pass items to the template
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
