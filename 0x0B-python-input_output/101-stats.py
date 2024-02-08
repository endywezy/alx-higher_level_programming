#!/usr/bin/python3
# 101-stats.py
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("Total file size: {}".format(size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            count += 1

            parts = line.split()
            if len(parts) < 10:
                print("Invalid input format:", line, file=sys.stderr)
                continue

            try:
                file_size = int(parts[-1])
                status_code = parts[-2]
            except ValueError:
                print("Invalid file size:", parts[-1], file=sys.stderr)
                continue

            size += file_size

            if status_code in valid_codes:
                status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if count % 10 == 0:
                print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        sys.exit(1)
