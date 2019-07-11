#!/usr/bin/env python3
import sys

a_lists = sys.argv[1:]
b = {}
for a in a_lists:
    c1,c2 = a.split(":")
    b[c1]=c2
for key,value in b.items():
    print("ID:"+key+" Name:"+value)
