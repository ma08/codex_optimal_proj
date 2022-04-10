

from math import gcd

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            if m > (a[i]*a[j])/gcd(a[i], a[j]):
                m = (a[i]*a[j])/gcd(a[i], a[j])
                x = i+1
                y = j+1
    print(x, y)

if __name__ == "__main__":
    main()