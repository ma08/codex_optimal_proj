

import heapq
heap = [1, 2, 3, 4, 5, 6, 7]
heapq.heapify(heap)
print(heap)
heapq.heappush(heap, 10)
print(heap)
print(heapq.heappop(heap))
print(heap)
