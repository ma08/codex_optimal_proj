

import sys

numdays = int(sys.stdin.readline())
temp = sys.stdin.readline().split(' ')

mintemp = 100
minday = 0
for i in range(0, numdays - 2):
    if int(temp[i]) + int(temp[i + 1]) + int(temp[i + 2]) < mintemp:
        mintemp = int(temp[i]) + int(temp[i + 1]) + int(temp[i + 2])
        minday = i + 1

print(minday, temp[minday])
