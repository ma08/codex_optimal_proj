

def main():
    n, m, k = map(int, input().split()) # n: number of books, m: number of offers, k: number of books to buy 
    a = list(map(int, input().split())) # a: list of prices of each book
    offers = []
    for _ in range(m): # m times
        offers.append(list(map(int, input().split())))
    
    a.sort()
    b = a[:]
    for offer in offers:
        for i in range(offer[1]):
            b[i] = min(b[i], a[offer[0] - 1 - i])
    
    res = sum(a[:k])
    for i in range(k):
        res = min(res, sum(b[:i]) + sum(a[i:k]))
    
    print(res)

if __name__ == "__main__":
    main()
