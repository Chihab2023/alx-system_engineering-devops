#!/usr/bin/python3
"""
Queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns number of total subscribers.
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get('data', {})
    return data.get('subscribers', 0)
