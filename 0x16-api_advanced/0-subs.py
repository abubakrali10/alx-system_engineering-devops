#!/usr/bin/python3
"""fetch the number of subscribers on subreddit"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers of a given subreddit"""
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Agent v1.0'}
    res = requests.get(api_url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        results = res.json().get('data')
        subscribers = results.get("subscribers")
        return subscribers
    return 0
