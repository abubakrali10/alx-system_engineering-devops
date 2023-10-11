#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    """returns a list of titles of all hot articles for a given subreddit"""
    api_url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'My Reddit Scraper'}
    params = {'after': after, 'count': count, 'limit': 100}
    res = requests.get(api_url, headers=headers,
                       params=params, allow_redirects=False)

    if res.status_code != 200:
        return None

    results = res.json().get('data')
    after = results.get('after')
    count += results.get('dist')

    for c in results.get('children'):
        hot_list.append(c.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
