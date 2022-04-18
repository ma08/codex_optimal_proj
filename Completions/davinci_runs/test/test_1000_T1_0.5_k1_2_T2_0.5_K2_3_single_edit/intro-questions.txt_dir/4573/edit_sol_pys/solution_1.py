
import heapq

def get_median(l, heap_low, heap_high):
    if len(heap_low) > len(heap_high) or (len(heap_low) == len(heap_high) and l % 2 == 0):
        return -heap_low[0]
    else:
        return heap_high[0]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    heap_low = []
    heap_high = []
    for i in range(n):
        b = get_median(i, heap_low, heap_high)
        if a[i] > b:
            heapq.heappush(heap_high, a[i])
        else:
            heapq.heappush(heap_low, -a[i])
        if len(heap_low) < len(heap_high):
            heapq.heappush(heap_low, -heapq.heappop(heap_high))
        elif len(heap_low) > len(heap_high) + 1:
            heapq.heappush(heap_high, -heapq.heappop(heap_low))
    for i in range(n):
        b = get_median(i, heap_low, heap_high)
        if a[i] > b:
            heapq.heappush(heap_high, a[i])
        else:
            heapq.heappush(heap_low, -a[i])
        if len(heap_low) < len(heap_high):
            heapq.heappush(heap_low, -heapq.heappop(heap_high))
        elif len(heap_low) > len(heap_high) + 1:
            heapq.heappush(heap_high, -heapq.heappop(heap_low))
        print(get_median(n, heap_low, heap_high))

if __name__ == "__main__":
    main()
