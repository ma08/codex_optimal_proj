

    import sys
    sys.setrecursionlimit(10 ** 7)
    
def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    offers = []
    for _ in range(m):
        offers.append(list(map(int, input().split())))
    
    a.sort()
    b = a[::-1]
    for offer in offers:
        for i in range(offer[1]):
            b[i] = min(b[i], a[-offer[0] + i])
    
    res = sum(a[:k])
    for i in range(k):
        res = min(res, sum(b[:i]) + sum(a[-k+i:]))
    
    print(res)

if __name__ == "__main__":
    main()
