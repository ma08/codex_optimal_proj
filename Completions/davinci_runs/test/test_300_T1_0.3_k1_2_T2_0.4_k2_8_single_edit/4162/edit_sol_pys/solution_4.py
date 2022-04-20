
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    lcm = a[0] 
    for i in range(1, n): 
        lcm = lcm * a[i] // gcd(lcm, a[i]) 
    print(lcm)

def gcd(a, b): 
    while b: 
        a, b = b, a % b 
    return a

if __name__ == '__main__':
    main()
