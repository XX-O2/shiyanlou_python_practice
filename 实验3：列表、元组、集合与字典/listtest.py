#!/usr/bin/env python3
import sys

a_lists = sys.argv[1:]
more_3 = []
less_3 = []
for a in a_lists:
    if len(a)<=3:
        less_3.append(a)
    else:
        more_3.append(a)
print(' '.join(less_3))
print(' '.join(more_3))
