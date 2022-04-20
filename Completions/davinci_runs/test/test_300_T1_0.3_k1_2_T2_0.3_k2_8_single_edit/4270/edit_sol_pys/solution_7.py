
import heapq

def main():
    n = int(input())
    arr = [int(x) for x in input().split()]
    heapq.heapify(arr)
    while len(arr) > 1:
        heapq.heappush(arr, (heapq.heappop(arr) + heapq.heappop(arr)) / 2)
    print(arr[0])

if __name__ == '__main__':
    main()
