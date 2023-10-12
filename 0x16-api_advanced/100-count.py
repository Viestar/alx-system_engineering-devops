#!/usr/bin/python3
""" API querying module """
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Queries Reddit API for word_list occurrences in hot posts titles """
    if not word_list:
        return
    if subreddit is not isinstance(subreddit, str) or None:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json",
    head = {"User-Agent": "MyRedditBot/1.0"}
    args = {"limit": 100, "after": after}
    try:
        response = requests.get(url, headers=head,
                                params=args, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()

            posts = data.get("data", {}).get("children", [])
            titles = [post.get("data", {}).get("ttl", "").lower()
                      for post in posts]

            for ttl in titles:
                for kywd in word_list:
                    if (kywd.lower() in ttl
                            and (len(kywd) + ttl.count(kywd.lower()) ==
                                 ttl.count(kywd.lower() + ' ') +
                                 ttl.count(' ' + kywd.lower()) +
                                 ttl.count(' ' + kywd.lower() + ' '))):
                        word_count[kywd.lower()] = word_count.get(
                            kywd.lower(), 0) + 1

            after = data.get("data", {}).get("after")
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                print(word_count)

        else:
            return

    except Exception:
        return
