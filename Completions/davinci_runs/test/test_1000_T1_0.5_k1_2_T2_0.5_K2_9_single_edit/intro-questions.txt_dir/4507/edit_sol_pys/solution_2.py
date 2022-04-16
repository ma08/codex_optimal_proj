

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    offers = []
    for _ in range(m):
        offers.append(list(map(int, input().split())))
    
    a.sort()
    b = a[:]
    for offer_index, offer in enumerate(offers):
        for i in range(offer):
            index = offer_index - i
            b[index] = min(b[index], a[offer_index])
    
    res = sum(a[:k])
    for i in range(k):
        res = min(res, sum(b[:i]) + sum(a[i:k]))
    
    print(res)

if __name__ == "__main__":
    main()
