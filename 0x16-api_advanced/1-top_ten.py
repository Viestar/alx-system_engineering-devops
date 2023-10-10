#!/usr/bin/python3
""" API querying module """
import requests


def top_ten(subreddit):
    """Queries the API for titles of the first 10 hot reddit posts """
    subs = requests.get(f"https://www.reddit.com/r/{subreddit} \
                        /hot.json?limit=10",
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if subs.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in subs.json().get("data").get("children")]
