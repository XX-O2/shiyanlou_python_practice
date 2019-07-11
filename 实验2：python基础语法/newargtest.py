#!/usr/bin/env python3

import sys

contents = sys.argv[1:]

for content in contents:
    if len(content)>3:
        print(content)
