import sys

def main():
    n = int(sys.stdin.readline().strip())
    q = [int(x) for x in sys.stdin.readline().strip().split()]
    p = [0] * n
    for i in range(n-1):
        if q[i] == 0:
            p[i] = p[i+1] = i+1
        elif q[i] > 0:
            if p[i] == 0:
                p[i] = i+1
            p[i+1] = p[i] + q[i]
        else:
            if p[i+1] == 0:
                p[i+1] = i+2
            p[i] = p[i+1] + q[i]
    if p[0] == 0:
        p[0] = 1
    if p[-1] == 0:
        p[-1] = n
    if p[0] < 1 or p[-1] > n:
        print(-1)
    else:
        for i in range(n-1):
            if p[i] == p[i+1]:
                print(-1)
                return
        print(*p)

if __name__ == "__main__":
    main()
