#!/usr/bin/env python
# Small automation: log rotation

# Write a function:

# def rotate_logs(directory_path, max_files):
# Requirements:
# Inside the directory, log files follow this naming pattern:

# app.log
# app.log.1
# app.log.2
# ...


# Implement a simple log rotation algorithm:
# If app.log.(max_files) exists, delete it.
# Shift all logs upward by one:
# app.log.(max_files - 1) → app.log.(max_files)
# app.log.(max_files - 2) → app.log.(max_files - 1)
# ...
# app.log.1 → app.log.2


# Finally rename:

# app.log → app.log.1
# You can assume the directory exists.
# Only use os functions. Do not use shutil or external libraries.
# If a file does not exist during rotation, skip it.

import os
import argparse

def rotate_files(directory_path, max_files):
    highest = os.path.join(directory_path, f"app.log.{max_files}")
    if os.path.exists(highest):
        os.remove(highest)
        
    for i in range(max_files - 1, 0, -1):
        src = os.path.join(directory_path, f"app.log.{i}")
        dst = os.path.join(directory_path, f"app.log.{i+1}")
        if os.path.exists(src):
            os.rename(src, dst)
            
    base = os.path.join(directory_path, "app.log")
    first = os.path.join(directory_path, "app.log.1")
    if os.path.exists(base):
        os.rename(base, first)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--max_files", type=int, required=True)
    args = parser.parse_args()
    
    rotate_files(args.path, args.max_files)
    
    

if __name__ == "__main__":
    main()