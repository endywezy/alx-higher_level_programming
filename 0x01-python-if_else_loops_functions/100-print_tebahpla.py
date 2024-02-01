#!/usr/bin/python3
# 100-print_tebahpla.py

output_str = ""
for i in range(ord('z'), ord('A') - 1, -1):
    output_str += "{}".format(chr(i) if i % 2 == 0 else chr(i - 26))

print(output_str)
