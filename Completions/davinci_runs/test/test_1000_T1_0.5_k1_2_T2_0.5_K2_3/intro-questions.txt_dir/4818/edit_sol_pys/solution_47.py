import sys
import math

def main():
    n, m = map(int, sys.stdin.readline().split())
    tasks_list = map(int, sys.stdin.readline().split())
    intervals_list = map(int, sys.stdin.readline().split())
    tasks_list.sort()
    intervals_list.sort()
    tasks_list.append(math.inf) # or float('inf')
    intervals_list.append(math.inf) # or float('inf')
    i = 0
    j = 0
    count = 0
    while i < n and j < m:
        if tasks_list[i] <= intervals_list[j]:
            count += 1
            i += 1
        j += 1
    print(count)

main()
