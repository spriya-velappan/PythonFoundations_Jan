"""
title: script2
author: sxv3240
date: 1/10/2019 3:38 PM
"""


import subprocess

print("inside script2")

choice = input("to get output from script1.py type 'yes': ")
if choice.lower() == 'yes':
    run_code = subprocess.run(["python", "script1.py"], capture_output=True)
    print(run_code.stdout.decode("utf-8"))
else:
    print("thanks for your choice")