#!/usr/bin/env python3
import sys
import json
import re
import math

TIMING_RE = re.compile(r"took (\d+) ms")

def main():
    data = json.load(sys.stdin)
    lines = data["lines"]

    timings = []
    for line in lines:
        m = TIMING_RE.search(line)
        if m:
            timings.append(int(m.group(1)))

    if len(timings) == 0:
        print(json.dumps({"error": "No timings found"}))
        return

    mean = sum(timings) / len(timings)
    variance = sum((x - mean) ** 2 for x in timings) / len(timings)
    stddev = math.sqrt(variance)

    print(json.dumps({
        "timings": timings,
        "mean": mean,
        "stddev": stddev
    }))

if __name__ == "__main__":
    main()
