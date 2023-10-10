#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def top_ten(subreddit):
    """prints titles of first 10 hot posts listed for a given subreddit"""
    api_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Agent v1.1'}
    params = {'limit': 10}
    res = requests.get(api_url, headers=headers,
                       params=params, allow_redirects=False)

    if res.status_code == 200:
        results = res.json().get('data')
        [print(p.get('data').get('title')) for p in results.get('children')]
    else:
        print('None')
