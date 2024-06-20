#!/usr/bin/python3
"""
Function that queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of given keywords (case-insensitive, delimited
by spaces. Javascript should count as javascript, but java should not).
"""

import requests


def count_words(subreddit, word_list, instances=None, after="", count=0):
    """
    Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    if instances is None:
        instances = {}

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    data = results.get("data", {})
    after = data.get("after")
    count += data.get("dist", 0)

    for child in data.get("children", []):
        title = child.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            word_lower = word.lower()
            times = title.count(word_lower)
            if times > 0:
                instances[word] = instances.get(word, 0) + times

    if after is None:
        if not instances:
            print("")
            return
        sorted_instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in sorted_instances:
            print("{}: {}".format(k, v))
    else:
        count_words(subreddit, word_list, instances, after, count)
