#!/usr/bin/python3
""" API querying module """
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Queries the API fcor list containing the titles of all hot articles """
    subs = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                        params={"after": after, "count": count},
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if subs.status_code >= 400:
        return None

    hl = hot_list + [child.get("data").get("title")
                     for child in subs.json()
                     .get("data")
                     .get("children")]

    info = subs.json()
    if info.get("data").get("after"):
        return recurse(subreddit, hl, info.get("data").get("count"),
                       info.get("data").get("after"))
    return hl
