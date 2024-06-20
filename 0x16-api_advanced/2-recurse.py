#!/usr/bin/python3
"""Module for task 2."""

import requests


def recurse(subreddit, hot_list=None, count=0, after=None):
    """
    Queries the Reddit API and returns all hot posts
    of the subreddit.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"count": count, "after": after}
    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url, params=params, headers=headers, allow_redirects=False)

    if response.status_code >= 400:
        return None

    data = response.json().get("data", {})
    hot_list += [child.get("data", {}).get("title") for child in data.get("children", [])]

    after = data.get("after")
    if not after:
        return hot_list

    return recurse(subreddit, hot_list, count, after)
