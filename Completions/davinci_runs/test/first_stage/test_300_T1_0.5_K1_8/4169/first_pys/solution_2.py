
import heapq

def main():
    n, m = map(int, input().split())
    a_b = sorted([tuple(map(int, input().split())) for _ in range(n)])
    # print(a_b)

    # heapq.heapify(a_b)
    # print(a_b)

    # print(heapq.heappop(a_b))
    # print(heapq.heappop(a_b))
    # print(heapq.heappop(a_b))
    # print(heapq.heappop(a_b))
    # print(heapq.heappop(a_b))
    # print(heapq.heappop(a_b))

    # print(heapq.heappush(a_b, (2, 3)))
    # print(heapq.heappush(a_b, (1, 3)))
    # print(heapq.heappush(a_b, (1, 3)))
    # print(heapq.heappush(a_b, (1, 3)))
    # print(heapq.heappush(a_b, (1, 3)))
    # print(heapq.heappush(a_b, (1, 3)))

    total_cost = 0
    while m > 0:
        # print(a_b)
        # print(m)
        # print(total_cost)
        a, b = heapq.heappop(a_b)
        if m - b >= 0:
            total_cost += a * b
            m -= b
        else:
            total_cost += a * m
            m = 0
    print(total_cost)

if __name__ == "__main__":
    main()