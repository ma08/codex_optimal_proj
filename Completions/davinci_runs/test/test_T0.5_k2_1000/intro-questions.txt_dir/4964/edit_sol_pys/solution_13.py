

import sys

def main():
    n, h, l = map(int, sys.stdin.readline().split())
    horror = set(map(int, sys.stdin.readline().split()))
    horror_index = [0] * n # 0 is not horror, 1 is horror
    for i in horror: # set horror
        horror_index[i] = 1
    for i in range(l):
        a, b = map(int, sys.stdin.readline().split())
        if a in horror:
            horror_index[b] = 1
        elif b in horror:
            horror_index[a] = 1
    for i in range(n):
        if horror_index[i] == 1:
            continue
        horror_index[i] = float('inf') # infinity (float)
        for j in range(l):
            a, b = map(int, sys.stdin.readline().split())
            if a == i:
                horror_index[i] = min(horror_index[i], horror_index[b] + 1)
            elif b == i:
                horror_index[i] = min(horror_index[i], horror_index[a] + 1)
        if horror_index[i] == float('inf'): # if not connected
            horror_index[i] = -1
    max_hi = max(horror_index)
    max_indices = []
    for i in range(n):
        if horror_index[i] == max_hi:
            max_indices.append(i)
    print(min(max_indices))

if __name__ == '__main__':
    main()
