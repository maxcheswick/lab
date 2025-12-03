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
    counter = {"ERROR": 0, "INFO": 0, "WARN": 0}
    error_lines = []
    request_id = set()
    
    with open(file) as f:
        for line in f:
            parts = line.split()
            if len(parts) < 3:
                continue

            level = parts[2]
            
            if level in counter:
                counter[level] += 1
                
            if level == "ERROR":
                error_lines.append(line)
                
                m = re.search(r"request_id=(\w+)", line)
                if m:
                    request_id.add(m.group(1))
                    # request_id = sorted(request_id)
                    

                
    print("Counter")
    print(counter)
    
    print("\nError List")
    for l in error_lines:
        print(l)
    
    print("\nRequest ID")
    print(request_id)
    
    print("\nUnique IDs")
    print(len(request_id))
    
                

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    args = parser.parse_args()
    
    parse_file(args.file)


if __name__ == "__main__":
    main()
