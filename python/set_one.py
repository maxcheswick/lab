#!/usr/bin/env python

#Return a list of all lines from a file, stripped of trailing newlines.

def read_lines(file):
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(line.rstrip())
            
#Given a string, return a dictionary where keys are words and values are counts.
def count_words(text):
    word_count = {}
    words = text.split()
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
        
# Given a list of dictionaries like:
#     [
#   {"name": "svc1", "status": "ok"},
#   {"name": "svc2", "status": "fail"},
#   {"name": "svc3", "status": "ok"}
# ]
#     Return a sorted list of names where status == "fail".

def failed_names(list_of_dict):
    failed = []
    for item in item(list_of_dict):
        if item["status"] == "fail":
            failed.append(item["name"])
    failed = sorted(failed)
    return failed
        
def failed_names(list_dict):
    return sorted([d["name"] for d in list_dict if d["status"] == "fail"])


# Return the last n lines of a file, stripped of newlines.
def tail(path, n):
    with open(path) as f:
        lines = f.readlines()
    return [line.rstrip() for line in lines[-n:]]

def merge_dicts(d1, d2):
    merge = {}
    for k, v in d1.items():
        merge[k] = v
    for k, v in d2.items():
        merge[k] = v
    return merge

#Return a list of just the levels:
# "2025-11-20 12:15:22 INFO User logged in"
# "2025-11-20 12:17:01 WARN Disk space low"
# "2025-11-20 12:19:30 ERROR Timeout"

def levels(path):
    levels = []
    with open(path) as f:
        for lines in f:
            parts = lines.split()
            levels.append(parts[2])
    return levels

import re
def sum_numbers(text):
    nums = re.findall(r"\d+", text)
    return sum(int(x) for x in nums)
    
#Return only the dicts that contain the key "value".

def return_key(items):
    results = []
    # for d in items:
    #     if "value" in d:
    #         results.append(d)
    return [d for d in items if "value" in d]