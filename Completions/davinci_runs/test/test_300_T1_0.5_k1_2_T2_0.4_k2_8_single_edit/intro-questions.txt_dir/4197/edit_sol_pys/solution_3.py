
from collections import defaultdict

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(list)
    for i, j in enumerate(a):
        d[j].append(i+1)
    for i in range(m):
        l, r = map(int, input().split())
        if l in d:
            if len(d[l]) > 0:
                for j in d[l]:
                    if j <= r:
                        print(j)
                        break
                else:
                    print(-1)
            else:
                print(-1)
        else:
            print(-1)


if __name__ == '__main__':
    main()
