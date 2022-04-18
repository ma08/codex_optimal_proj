from collections import deque


def main():
    n, r = map(int, input().split())
    a = deque()
    b = deque()
    for i in range(n):
        ai, bi = map(int, input().split())
        a.appendleft(ai)
        b.appendleft(bi)
    l = deque()
    l.appendleft(r)
    for i in range(n):
        l.appendleft(l[0]+b[i])
    l.popleft()
    for i in range(n):
        if a[i] > l[i]:
            print("NO")
            return
    print("YES")
    return

if __name__ == '__main__':
    main()
