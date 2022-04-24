

import os
import subprocess
import sys

def get_sub_files(path):
    sub_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            sub_files.append(os.path.join(root, file))
    return sub_files

l = [[] for i in range(N)]
for i in range(M):
    l[city[i][0] - 1].append(city[i][1])

for i in range(N):
    l[i].sort()

for i in range(M):
    print("%06d%06d" % (city[i][0], l[city[i][0] - 1].index(city[i][1]) + 1))
