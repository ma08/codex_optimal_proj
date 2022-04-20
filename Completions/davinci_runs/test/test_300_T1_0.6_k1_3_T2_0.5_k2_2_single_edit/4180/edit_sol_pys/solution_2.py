#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by techno at 28/05/19
# Feature:  # Enter feature name here
# Environment:  # Enter environment name here
# Development Language: Python 3.6.5
# Date: 28/05/19
# Time: 20:20
# Package:  # Enter package name here
# Reference: https://www.youtube.com/watch?v=mGm5i5xhxm8
# -------------------------------------------------------------------------------
# Imports
# -------------------------------------------------------------------------------
# Code
import sys

N = int(input())

# get the number of 1000-yen bills
num_of_bills = N // 1000

# get the amount of change
change = 1000 * num_of_bills - N


# -------------------------------------------------------------------------------
# End of file
print(change)
