#!/usr/bin/python3
# 101-stats.py
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


import sys
from collections import defaultdict

# Function to print statistics
def print_stats(total_size, status_counts):
    print("Total file size:", total_size)
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

# Initialize variables
total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:
    # Read input line by line from stdin
    for line in sys.stdin:
        line_count += 1

        # Split the input line into components
        parts = line.split()
        if len(parts) >= 10:
            status_code = parts[-2]
            file_size = int(parts[-1])
            total_size += file_size
            status_counts[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    # Print statistics on keyboard interruption
    print_stats(total_size, status_counts)
    sys.exit(0)  # Exit gracefully
