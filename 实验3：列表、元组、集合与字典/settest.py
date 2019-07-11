#!/usr/bin/env python3
import sys

a_lists = sys.argv[1:]
b = set()

for a in a_lists:
    b.add(a)
print(' '.join(b))
