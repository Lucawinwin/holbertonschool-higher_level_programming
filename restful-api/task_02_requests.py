#!/usr/bin/python3
 

import requests
import csv


# Recover fetches all post from JSONPlaceholder and print status code
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    print("status_code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        
        for post in posts:
            print(post["title"])

    else:
        print("failed to fetch posts")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        structured_data = [{
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
            } for post in posts]


        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])

            writer.writeheader()

            writer.writerows(structured_data)

        print("The posts.csv file has been successfully created!")


    if __name__ == "__main__":
        fetch_and_print_posts()
        fetch_and_save_posts()
