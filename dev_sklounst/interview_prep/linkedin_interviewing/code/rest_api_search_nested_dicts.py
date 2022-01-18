#!/usr/bin/env python3

import json
import requests

from typing import Any, Collection,  Dict, Generator, List

my_url = 'https://api.github.com/repos/boto/boto3/commits'
res = requests.get(my_url)
my_json = json.loads(res.content)

with open('./files/dictionary_word_def_for_resign.json', 'r') as file_r:
    _ = file_r.read()
    word_def_resign = json.loads(_)

with open('./files/drugs_info.json', 'r') as file_r:
    _ = file_r.read()
    drugs_info = json.loads(_)

# Goals:
# parse the json object in my_json var and count all occurrences of commits that have not been verified?
# parse the json object in word_def_resign and find the nested key 't'
# support searching for multiple keys?
# get the index(es) of where the key(s) were found?


def search_collection_1(key: str, data: Collection) -> Generator:
    """Given a data object (dict|list) and a key, traverse the data to return the value of that key

    Args:
        data (dict): a python data object of type dict or list
        key (str): a python string that represents the key to be found
    """
    try:
        for k, v in data.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for search in search_collection_1(key, v):
                    yield search
            if isinstance(v, list):
                for item in v:
                    for search in search_collection_1(key, item):
                        yield search
    # if data is a dict, then we get AttributeError since, e.g., List objects do not have an attribute 'items'
    except AttributeError:
        if isinstance(data, list):
            for item in data:
                for search in search_collection_1(key, item):
                    yield search


def search_collection_2(key_name: str, data: Collection) -> Generator:
    if isinstance(data, list):
        for item in data:
            for search in search_collection_2(key_name, item):
                yield search
    if isinstance(data, dict):
        if key_name in data:
            yield data[key_name]
        for item in data.values():
            for search in search_collection_2(key_name, item):
                yield search


def search_keys_in_collection(keys: List, data: Collection) -> Generator:
    """Search data object using a list of keys"""
    for key_name in keys:
        for result in func_selector(key_name, data):
            yield {key_name: result}


def func_selector(key, data, func = 1):
    if func == 1:
        print("Using search_collection_1()")

        return search_collection_1(key, data)
    elif func == 2:
        print("Using search_collection_2()")

        return search_collection_2(key, data)


if __name__ == "__main__":
    func = 2  # choose a solution function to use
    key_to_find = "verified"  # expected values: true|false

    print("\nSearch for 'verified' in a git commit history:")
    for r in func_selector(key_to_find, my_json, func):
        print(r)

    print("\nSearch for 'date' in a git commit history:")
    for r in func_selector('date', my_json, func):
        print(r)

    count_not_verified = 0
    for r in func_selector(key_to_find, my_json, func):
        count_not_verified += 1

    count_commits = 0
    for r in func_selector('commit', my_json, func):
        count_commits += 1

    print(f"\nThere were {count_not_verified} non-verified git commits")
    print(f"\nThere were {count_commits} total git commits")

    print("\nSearch for 't' in a json doc used to define a word (dictionary website content):")
    for r in func_selector('t', word_def_resign, func):
        print(r)

    print("\nSearch for 'name' in a json doc of medicines:")
    for r in func_selector('name', drugs_info, func):
        print(r)

    print("\nSearch for multiple keys in the dictionary word definition object:")
    for r in search_keys_in_collection(['stems', 'id', 'salty', 'offensive', 'if'], word_def_resign):
        print(r)
