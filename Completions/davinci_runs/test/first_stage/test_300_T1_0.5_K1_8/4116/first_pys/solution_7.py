
import sys

num = int(sys.stdin.readline())

for i in range(1,10):
    for j in range(1,10):
        if num == i*j:
            print("Yes")
            exit()

print("No")