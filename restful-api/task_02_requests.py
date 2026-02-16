#!/usr/bin/python3
"""
Fetch posts from JSONPlaceholder and
either print titles or save selected fields to a CSV file.
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and
    print the HTTP status code and each post title."""
    url = "https://jsonplaceholder.typicode.com/posts"
    reponse = requests.get(url)
    print(f"Status Code: {reponse.status_code}")
    if reponse.status_code == 200:
        data = reponse.json()
        for item in data:
            print(item["title"])


def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and
    save id, title, and body fields into posts.csv."""
    url = "https://jsonplaceholder.typicode.com/posts"
    reponse = requests.get(url)
    print(f"Status Code: {reponse.status_code}")
    if reponse.status_code == 200:
        data = reponse.json()
        posts = []
        for item in data:
            post = {
                "id": item["id"],
                "title": item["title"],
                "body": item["body"]
                }
            posts.append(post)

        fieldnames = ["id", "title", "body"]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)
