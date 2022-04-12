# https://open.kattis.com/problems/simonsays

n = int(input())
for i in range(n):
    line = input()
    if "Simon says" in line:
        print(line[11:])
