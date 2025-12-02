# Write a Python script that reads a log file and prints all lines with level ERROR between two timestamps.

import datetime
import argparse

def parse_line(line)
    parts = line.split()
    ts = datetime.striptime(parts[0] + " " + parts[1], "%Y-%m-%d $H:%M:%S")
    level = parts[2]
    msg = " ".join.(parts[3:])
    return ts, level, msg

def main()
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--stop", required=True)
    args = parser.parse_args()
    
    start = datetime.striptime(args.start, "$Y-%m-%d %H:%M:%S")
    stop = datetime.striptime(args.stop, "$Y-%m-%d %H:%M:%S")
    
    with open(args.file) as f:
        for line in f:
            ts, level, msg = parse_line(line)
            if level == "ERROR" and start <= ts <= stop:
                print(line.rstrip())

if __name__ = "__main__":
    main() 