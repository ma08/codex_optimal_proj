from sys import stdin

k = int(stdin.readline())

i = 1
while True:
    if int("7"*i)%k == 0:
        print(i)
        break
    i += 1
