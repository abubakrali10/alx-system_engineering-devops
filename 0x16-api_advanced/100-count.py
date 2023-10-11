#!/usr/bin/python3
"""Contains the count_words function"""
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    '''Prints counts of given words found in hot posts of a given subreddit.
    '''
    user_agent = {'User-agent': 'test45'}
    res = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                       .format(subreddit, after), headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if res.status_code == 200:
        res = res.json()['data']
        aft = res['after']
        res = res['children']
        for post in res:
            t = post['data']['title'].lower()
            for word in t.split(' '):
                if word in word_list:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, word_list, found_list, aft)
        else:
            result = {}
            for word in found_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for k, v in sorted(result.items(), key=lambda item: item[1],
                               reverse=True):
                print(f'{k}: {v}')
    else:
        return
