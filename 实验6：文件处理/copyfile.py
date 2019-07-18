#!/usr/bin/env python3

filename = "/home/shiyanlou/shiyanlou.txt"

with open("/home/shiyanlou/shiyanlou_copy.txt","w") as file1:
    with open("/home/shiyanlou/shiyanlou.txt","r") as file2:
        Lines = file2.readlines()
        #i=1
        #for line in Lines:
            #a = str(i) +" "+line
            #file1.write(a)
            #i+=1
        for a,b in enumerate(Lines):
            file1.write('{} {}'.format(a+1,b))
