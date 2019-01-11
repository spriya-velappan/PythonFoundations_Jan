"""
title: json_manipulation.py
author: sxv3240
date: 1/10/2019 9:28 AM
"""


import time
import csv
import json

with open('medical.json', 'r') as medical_rooms:
    data = json.load(medical_rooms)
    print(data)
    print(type(data))
    pretty_output=json.dumps(data, indent=10)

    print(pretty_output)

    for room_name in data:
        print(room_name)

    for room_name in data:
            print(f"{room_name} is in room {data[room_name]['room-number']}")

    for room_name in data:
        data[room_name]['price'] = data[room_name]['price'] * 0.5
        print(f"{room_name} is in room {data[room_name]['price']}")

    with open('medical.json', 'r') as medical_rooms:
        data = json.load(medical_rooms)

    for room_name in data:
        data[room_name]['price'] = data[room_name]['price'] * 0.5
        print(f"{data[room_name]['price']}")

    with open('medical.json', 'w') as medical_rooms:
        json.dump(data, medical_rooms, indent=4)