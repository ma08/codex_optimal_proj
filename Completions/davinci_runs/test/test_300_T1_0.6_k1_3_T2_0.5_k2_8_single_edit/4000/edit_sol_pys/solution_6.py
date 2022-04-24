
import sys
import queue

def main():
    n = int(sys.stdin.readline())
    graph = [[] for _ in xrange(n + 1)]
    for _ in xrange(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    res = 0
    for i in xrange(1, n + 1):
        max_1, max_2 = 0, 0
        dist_1 = [0] * (n + 1)
        q = queue.Queue()
        q.put(i)
        while not q.empty():
            u = q.get()
            for v in graph[u]:
                if dist_1[v] == 0:
                    dist_1[v] = dist_1[u] + 1
                    if dist_1[v] > max_1:
                        max_2 = max_1
                        max_1 = dist_1[v]
                    elif dist_1[v] > max_2:
                        max_2 = dist_1[v]
                    q.put(v)
        for j in xrange(1, n + 1):
            if dist_1[j] == max_2:
                max_3 = 0
                dist_2 = [0] * (n + 1)
                q = queue.Queue()
                q.put(j)
                while not q.empty():
                    u = q.get()
                    for v in graph[u]:
                        if dist_2[v] == 0:
                            dist_2[v] = dist_2[u] + 1
                            if dist_2[v] > max_3:
                                max_3 = dist_2[v]
                            q.put(v)
                if max_1 + max_2 + max_3 - 3 > res:
                    res = max_1 + max_2 + max_3 - 3
                    a = i
                    b = j
                    c = 0
                    for k in xrange(1, n + 1):
                        if dist_2[k] == max_3:
                            c = k
                            break
    print(res)
    print(a, b, c)

if __name__ == "__main__":
    main()
