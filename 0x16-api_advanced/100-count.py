#!/usr/bin/python3
""" API querying module """
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Queries Reddit API for word_list occurrences in hot posts titles """

    user_info = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                             params={"after": after},
                             headers={"User-Agent": "My-User-Agent"},
                             allow_redirects=False)
    if user_info.status_code == 200:
        user_info_json = user_info.json()

        hot_list = [child.get("data").get("title")
                    for child in user_info_json
                    .get("data")
                    .get("children")]
        if hot_list:

            word_list = list(dict.fromkeys(word_list))

            if word_count == {}:
                word_count = {word: 0 for word in word_list}

            for title in hot_list:
                split_words = title.split(' ')
                for word in word_list:
                    for s_word in split_words:
                        if s_word.lower() == word.lower():
                            word_count[word] += 1

            if user_info_json.get("data").get("after"):
                return count_words(subreddit, word_list, word_count,
                                   user_info_json.get("data").get("after"))

            else:
                sorted_counts = sorted(
                    word_count.items(), key=lambda kv: kv[0])
                sorted_counts = sorted(word_count.items(),
                                       key=lambda kv: kv[1], reverse=True)
                for key, value in sorted_counts:
                    if value != 0:
                        print(f"{key}: {value}")
        return None
    return None
