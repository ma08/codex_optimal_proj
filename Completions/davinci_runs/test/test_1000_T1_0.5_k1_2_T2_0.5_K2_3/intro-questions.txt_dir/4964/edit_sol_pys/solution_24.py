

import sys

def main():
    n, h, l = map(int, sys.stdin.readline().split())
    horror = list(map(int, sys.stdin.readline().split()))
    horror_set = set(horror) # set of horror movie index
    horror_index = [0] * n # index of the movie with the largest distance from horror movies
    for i in horror:
        horror_index[i] = 0 # set horror movie index to 0, because it is a horror movie
    for i in range(l):
        a, b = map(int, sys.stdin.readline().split())
        if a in horror_set: # if movie a is horror movie
            horror_index[b] = 0 # set movie b's index to 0, because it is connected to horror movie
        elif b in horror_set:
            horror_index[a] = 0
    for i in range(n):
        if horror_index[i] == 0:
            continue # if movie i's index is 0, it is a horror movie, so skip
        horror_index[i] = float('inf') # set movie i's index to infinity
        for j in range(l):
            a, b = map(int, sys.stdin.readline().split())
            if a == i: # if movie i is connected to movie a
                horror_index[i] = min(horror_index[i], horror_index[b] + 1)
            elif b == i: # if movie i is connected to movie b
                horror_index[i] = min(horror_index[i], horror_index[a] + 1)
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
