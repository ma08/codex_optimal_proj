import sys

def main():
    n = int(sys.stdin.readline().strip())
    q = [int(i) for i in sys.stdin.readline().strip().split()]
    p = [0] * (n+1)
    for i in range(n-1):
        if q[i] == 0:
            p[i] = p[i+1] = i+2
        elif q[i] > 0:
            if p[i] == 0:
                p[i] = i+2
            p[i+1] = p[i] + q[i]
        else:
            if p[i+1] == 0:
                p[i+1] = i+3
            p[i] = p[i+1] + q[i]
    if p[0] == 0:
        p[0] = 2
    if p[-1] == 0:
        p[-1] = n+1
    if p[0] < 2 or p[-1] > n+1:
        print(-1)
    else:
        for i in range(n-1):
            if p[i] == p[i+1]:
                print(-1)
                return
        print(*p)

if __name__ == "__main__":
    main()
