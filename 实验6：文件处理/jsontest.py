#!/usr/bin/env python3

import json

data = [
        {
            'user_id':1000,
            'name':'Shiyan',
            'pass':10,
            'study_time':50,
            },
        {
            'user_id':2000,
            'name':'Lou',
            'pass':15,
            'study_time':171,
            }
        ]

with open('/tmp/jsontest.json','w') as file:
    for a in data:
        json.dump(a,file)
