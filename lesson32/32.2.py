import requests
import json

base_url = 'https://api.pushshift.io/reddit/comment/search/'
subreddit = input('Enter what you are searching ')


def get_data(url, params):
    return requests.get(url, params).json()


data = get_data(base_url, {"subreddit": subreddit, "size": "5", "sort": "desc"})

with open('data.txt', 'w') as file_name:
    json.dump(data, file_name, indent=4)


