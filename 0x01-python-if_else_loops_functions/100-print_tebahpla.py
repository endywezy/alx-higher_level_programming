#!/usr/bin/python3
# 100-print_tebahpla.py

for i in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(i) if i % 2 == 0 else chr(i - 32)), end="")

