#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    # Print status code
    print("Status Code:", response.status_code)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse fetched data into JSON object
        posts = response.json()
        
        # Iterate through the parsed JSON data and print out the titles of all the posts
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        posts = response.json()
        
        # Structure data into a list of dictionaries
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        # Write data to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for post in data:
                writer.writerow(post)
        
        print("Posts successfully fetched and saved to posts.csv")
    else:
        print("Failed to fetch posts. Status Code:", response.status_code)
