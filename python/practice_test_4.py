#!/usr/bin/env python

# Build a command line tool that supports two commands:

# Command 1
# python tool.py logs --file log.txt --level ERROR

# Behavior:

# Print all lines from the file that contain the given level substring
# For example, if level is ERROR, print all lines containing ERROR.

# Command 2
# python tool.py stats --file log.txt

# Behavior:

# Count how many times INFO, WARN, and ERROR appear in the file

# Print a dictionary like:

# {"INFO": 10, "WARN": 3, "ERROR": 5}


import argparse

def cmd_logs(file, stats):
    print("command logs")
    
def cmd_states(file):
    print("command stats")

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")
    
    logs_parser = sub.add_parser("logs")
    logs_parser.add_argument("--file", required=True)
    logs_parser.add_argument("--level", required=True)
    
    stats_parser = sub.add_parser("stats")
    stats_parser.add_argument("--file", required=True)
    
    args = parser.parse_args()
    
    
    if args.command == "logs":
        cmd_logs(args.file, args.level)
    elif args.command == "stats":
        cmd_states(args.file)     

if __name__ == "__main__":
    main()