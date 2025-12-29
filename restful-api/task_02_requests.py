#!/usr/bin/env python3
"""
2. Consuming and processing data from an API using Python
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder API and print status code and titles
    """
    # Fetch data from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Print status code
    print(f"Status Code: {response.status_code}")
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON data
        posts = response.json()
        
        # Print all post titles
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch posts from JSONPlaceholder API and save to CSV file
    """
    # Fetch data from JSONPlaceholder
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON data
        posts = response.json()
        
        # Structure data into list of dictionaries
        structured_posts = []
        for post in posts:
            structured_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_posts.append(structured_post)
        
        # Write to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csv_file:
            # Define fieldnames (column headers)
            fieldnames = ['id', 'title', 'body']
            
            # Create DictWriter object
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            # Write headers
            writer.writeheader()
            
            # Write all rows
            writer.writerows(structured_posts)
        
        print("Data has been saved to posts.csv")
