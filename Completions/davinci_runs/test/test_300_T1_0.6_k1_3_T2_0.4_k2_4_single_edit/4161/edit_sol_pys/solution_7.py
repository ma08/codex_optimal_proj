

def gcd(a,b):
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a%b
    return a

def main():
    k = int(input())
    ans = 0
    for a in range(k):
        for b in range(k):
            for c in range(k):
                ans += gcd(a+1, gcd(b+1, c+1))
    print(ans)

if __name__ == '__main__':
    main()
