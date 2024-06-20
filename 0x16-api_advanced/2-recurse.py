#!/usr/bin/python3
"""
Function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.
"""

import requests


def recurse(subreddit, hot_list=None, after=""):
    """
    Returns a list containing the titles of all hot articles
    for a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    url = "https://api.reddit.com/r/{}?sort=hot&after={}".format(subreddit, after)
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])

    if not children:
        return hot_list if hot_list else None

    hot_list.extend([post.get("data", {}).get("title") for post in children])
    after = data.get("after")

    if not after:
        return hot_list

    return recurse(subreddit, hot_list, after)
