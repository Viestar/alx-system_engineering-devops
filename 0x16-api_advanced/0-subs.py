#!/usr/bin/python3
""" API querying module """
import requests


def number_of_subscribers(subreddit):
    """Queries the API for the total number of a subreddit subscribers """
    subs = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if subs.status_code >= 300:
        return 0

    return subs.json().get("data").get("subscribers")
