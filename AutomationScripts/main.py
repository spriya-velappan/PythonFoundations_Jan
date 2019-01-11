"""
title: main
author: sxv3240
date: 1/10/2019 3:36 PM
"""

import subprocess
from subprocess import PIPE

def main():

    print("=== From the Main App ===")

    run_code = subprocess.Popen(["python", "script2.py"], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    code_IO = run_code.communicate(input='yes'.encode())
    for lines in code_IO:
        print(lines.decode("utf-8"))

if __name__ == '__main__':
    main()