

import sys

def main():
    n, h, l = map(int, sys.stdin.readline().split())
    horror = list(map(int, sys.stdin.readline().split()))
    horror_set = set(horror)
    horror_index = [0] * (n + 1)
    for i in range(n):
        if i in horror_set:
            horror_index[i] = 0
        else:
            horror_index[i] = float('inf')
    for i in range(l):
        a, b = map(int, sys.stdin.readline().split())
        horror_index[b] = min(horror_index[b], horror_index[a] + 1)
        horror_index[a] = min(horror_index[a], horror_index[b] + 1)
    for i in range(n):
        if horror_index[i] == float('inf'):
            horror_index[i] = -1
    max_hi = max(horror_index)
    max_indices = []
    for i in range(n):
        if horror_index[i] == max_hi:
            max_indices.append(i)
    print(min(max_indices))

if __name__ == '__main__':
    main()
