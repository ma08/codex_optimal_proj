
import heapq

def get_median(heap_low, heap_high):
    if len(heap_low) > len(heap_high):
        return -heap_low[0]
    elif len(heap_low) < len(heap_high):
        return heap_high[0]
    else:
        return (heap_high[0] - heap_low[0]) / 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    heap_low = []
    heap_high = []
    for i in a:
        heapq.heappush(heap_low, -i)
        heapq.heappush(heap_high, -heapq.heappop(heap_low))
        if len(heap_low) < len(heap_high):
            heapq.heappush(heap_low, -heapq.heappop(heap_high))
        print(get_median(heap_low, heap_high))

if __name__ == "__main__":
    main()
