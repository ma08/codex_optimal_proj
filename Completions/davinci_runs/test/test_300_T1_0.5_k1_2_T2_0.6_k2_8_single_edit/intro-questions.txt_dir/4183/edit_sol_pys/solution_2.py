def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)



def lcm(a, b):

    return a * b // gcd(a, b)

def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = 1
    for t in T:
        ans = lcm(ans, t)
    print(ans)

if __name__ == '__main__':
    main()
