#Count all log levels in a file and print totals.


def count_levels(file):
    counts = {}
    with open(file) as f:
        for line in f:
            parts = line.split()
            level = parts[2]
            counts[level] = counts.get(level, 0) + 1
    return counts

if __name__ == "__main__":
    out = count_levels("app.log")
    for level, counts in out.items():
        print(level, counts)
        
