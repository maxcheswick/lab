#!/usr/bin/env python
# You are given an application log file with lines like:

# 2025-11-20 12:15:22 INFO User login successful user_id=44
# 2025-11-20 12:17:01 WARN Login attempt failed user_id=91
# 2025-11-20 12:19:30 ERROR Database timeout for request_id=abc123
# 2025-11-20 12:20:01 ERROR Database timeout for request_id=abc124
# 2025-11-20 12:21:12 INFO User logout user_id=44


# Write a Python script that:
# Reads a log file path from the command line.
# Prints all lines with level ERROR.
# Prints a summary dictionary showing the count of INFO, WARN, and ERROR lines.
# Also prints the total number of unique request_ids seen in ERROR lines.
# Assume request_id always appears as request_id=<value> on ERROR lines.
# Do not use external libraries except the standard library.

import argparse
import re

def parse_file(file):
    error_lines = []
    counts = {"ERROR": 0, "INFO": 0, "WARN": 0}
    request_ids = set()
    
    with open(file) as f:
        for line in f:
            parse = line.split()
            level = parse[2]
            
            if level in counts:
                counts[level] += 1
                
            if level == "ERROR":
                clean = line.rstrip()
                error_lines.append(clean)
                
                m = re.search(r"index_ids=(\w+)", clean)
                if m:
                    request_ids.add(group(1))
                    
    print("Counts")
    print(counts)
    
    print("\nError lines")
    for l in error_lines:
        print(l)
        
    print("\nUnique IDs")
    print(len(request_ids))
                        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    args = parser.parse_args()
    
    parse_file(args.file)

if __name__ == "__main__":
    main()