

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    offers = []
    for _ in range(m):
        offers.append(list(map(int, input().split())))
    
    a.sort(reverse=True)
    b = a.copy()
    for offer in offers:
        for i in range(offer[1]):
            b[i] = min(b[i], a[offer[0] - 1 - i])
    
    res = sum(a[:k])
    for i in range(k):
        res = min(res, sum(b[:i]) + sum(a[i:k]))
    
    print(res)

if __name__ == "__main__":
    main()
