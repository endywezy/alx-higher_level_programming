#!/usr/bin/python3
# 100-print_tebahpla.py
# Brennan D Baraban <375@holbertonschool.com>

"""Print the alphabet in reverse order alternating upper- and lower-case."""
for c in range(ord('z'), ord('a') - 1, -1):
    print(chr(c), end="" if (ord('z') - c) % 64 < 32 else "\n")
