
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b) 

def main():
    n = int(input())
    t = [int(input()) for _ in range(n)]
    ans = 1
    for i in t:
        ans = lcm(ans, i)
    print(ans)

if __name__ == '__main__':
    main()
