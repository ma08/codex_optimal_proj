

# A, B, X = map(int, input().split())
A, B, X = 10, 7, 100

def main():
    price = 0
    for n in range(1, 10**9+1):
        price = A*n + B*len(str(n))
        if price > X:
            break
    else:
        n = 0
    print(n-1)

if __name__ == '__main__':
    main()