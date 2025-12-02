# Write a small CLI tool that has two subcommands
# logs → filter
# stats → count

import argparse

def main():
    parser = argparse.ArgumentParser("DevOps CLI")
    sub = parser.add_argument(dest="cmd")
    
    p_logs = sub.add_parser("logs")
    p_logs.add_argument("--file")
    p_logs.add_argument("--level")
    
    p_states = sub.add_parser("stats")
    p_states.add_argument("--file")
    
    args = parser.parse_args()
    
    if args.cmd == "logs":
        with open(args.file) as f:
            for line in f:
                if args.level in line:
                    print(line.rstrip())
    elif args.cmd == "stats":
        from collections import Counter
        c = Counter()
        with open(args.file) as f:
            for line in f:
                parts = line.split()
                c[parts[2]] += 1
        print(c)                
        
if __name__ == "__main__":
    main()