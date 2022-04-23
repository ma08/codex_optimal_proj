#!/usr/bin/env python

import os
import sys

# file = open("/etc/passwd", "r")

# for line in file:
#     print(line)

# file.close()

with open("/etc/passwd", "r") as file:
    for line in file:
        print(line)

file.close()
