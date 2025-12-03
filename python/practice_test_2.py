#!/usr/bin/env python
# You are given a JSON file representing a list of services deployed in the environment.
# Example structure:

# [
#   {"name": "auth-service", "version": "3.1.0", "status": "healthy"},
#   {"name": "billing-service", "version": "1.5.0", "status": "degraded"},
#   {"name": "crm-api", "version": "2.7.3", "status": "healthy"},
#   {"name": "events-worker", "version": "4.0.1", "status": "unhealthy"}
# ]

# Write a Python function that:
# Loads the JSON.
# Returns a sorted list of service names where status is not healthy.
# The sort order should be alphabetical.

import json
import argparse

def parse_json(file):
    clean = []
    with open(file) as f:
        data = json.load(f)
        clean = sorted(svc["name"] for svc in data if svc["status"] != "healthy")
        
        # for svc in data:
        #     if svc["status"] != "healthy":
        #         clean.append(svc["name"])
                
    # clean = sorted(clean)
    print(clean)
                
        

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    args = parser.parse_args()
    
    parse_json(args.file)

if __name__ == "__main__":
    main()