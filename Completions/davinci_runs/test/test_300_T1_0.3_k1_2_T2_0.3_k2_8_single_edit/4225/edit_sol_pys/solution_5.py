
import heapq

def main():
    a, b, c, k = map(int, input().split())
    h = []
    heapq.heappush(h, (-a, 1)) # (value, multiple)
    heapq.heappush(h, (-b, 0)) # (value, multiple)
    heapq.heappush(h, (-c, -1)) # (value, multiple)
    s = 0
    for i in range(k):
        t = heapq.heappop(h)
        s += -t[0] * t[1]
        heapq.heappush(h, (t[0] + 1, t[1]))
    print(s)

if __name__ == '__main__':
    main()
