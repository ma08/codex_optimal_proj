

import sys
import heapq

n, a, b, c = map(int, sys.stdin.readline().split())
l = [int(sys.stdin.readline()) for _ in range(n)]

l.sort(reverse=True)

h = []

for i in range(n):
    heapq.heappush(h, (l[i], 1, l[i]))

# print(h)

for _ in range(n):
    bamboo, count, length = heapq.heappop(h)
    # print(bamboo, count, length)
    if length == a:
        if b in h:
            if c in h:
                print(count)
                sys.exit()
            else:
                heapq.heappush(h, (bamboo, count+10, length+b))
        else:
            if c in h:
                heapq.heappush(h, (bamboo, count+10, length+c))
            else:
                heapq.heappush(h, (bamboo, count+10, length+b))
                heapq.heappush(h, (bamboo, count+10, length+c))
    elif length == b:
        if c in h:
            print(count)
            sys.exit()
        else:
            heapq.heappush(h, (bamboo, count+10, length+c))
    elif length == c:
        print(count)
        sys.exit()
    else:
        heapq.heappush(h, (bamboo, count+1, length+1))
        if length > 1:
            heapq.heappush(h, (bamboo, count+1, length-1))
        if length > a:
            heapq.heappush(h, (bamboo, count+10, length+a))
        elif length > b:
            heapq.heappush(h, (bamboo, count+10, length+b))
        elif length > c:
            heapq.heappush(h, (bamboo, count+10, length+c))

print(-1)