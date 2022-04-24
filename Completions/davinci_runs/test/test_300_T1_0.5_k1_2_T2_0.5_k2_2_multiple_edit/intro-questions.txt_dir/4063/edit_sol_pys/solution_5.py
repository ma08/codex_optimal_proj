
# Import
import sys
import math
import os
import glob
import re
import operator

# Functions
def input():
    return sys.stdin.readline().strip()

def get_file_list(dir_name):
    return glob.glob(dir_name+'/*')

def get_file_name(file_name):
    return re.findall(r'/([a-zA-Z0-9_]+).txt', file_name)[0]

def get_file_size(file_name):
    return os.path.getsize(file_name)

# Main
N = int(input())
d = list(map(int, input().split()))

# Get file list
file_list = get_file_list('.')

# Make dictionary
file_dict = dict()
for file_name in file_list:
    file_dict[get_file_name(file_name)] = get_file_size(file_name)

# Solve
for i in range(N//2):
    if d[i] == d[N//2]:
        count += 1
    elif d[i] < d[N//2]:
        break

print(count)
