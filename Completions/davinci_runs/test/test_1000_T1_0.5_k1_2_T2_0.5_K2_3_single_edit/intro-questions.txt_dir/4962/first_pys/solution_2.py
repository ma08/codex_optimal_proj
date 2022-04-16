

import sys
import heapq

def main():
    N, L = map(int, sys.stdin.readline().split())
    drawers = [[] for i in range(L)]
    for i in range(N):
        A, B = map(int, sys.stdin.readline().split())
        drawers[A-1].append(B-1)
        drawers[B-1].append(A-1)
    heap = []
    for i in range(L):
        heapq.heappush(heap, (-len(drawers[i]), i))
    items = []
    while heap:
        count, index = heapq.heappop(heap)
        if count < -1:
            heapq.heappush(heap, (count+1, index))
            continue
        items.append(index)
        for i in drawers[index]:
            if i not in items:
                heapq.heappush(heap, (-len(drawers[i]), i))
    for i in range(N):
        A, B = map(int, sys.stdin.readline().split())
        A, B = A-1, B-1
        if A in items:
            print("LADICA")
        elif B in items:
            print("LADICA")
        else:
            print("SMECE")

main()