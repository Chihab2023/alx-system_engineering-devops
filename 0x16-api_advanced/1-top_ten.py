#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for
    a given subreddit.
    """
    url = "https://api.reddit.com/r/{}?sort=hot&limit=10".format(subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data', {})
    if 'children' in data:
        for post in data.get('children', []):
            print(post.get('data', {}).get('title'))
    else:
        print(None)
