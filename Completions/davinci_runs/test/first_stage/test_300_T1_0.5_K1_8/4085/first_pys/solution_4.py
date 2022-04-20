

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def main():
    t = int(input())
    for i in range(0, t):
        n = int(input())
        divisors = [int(x) for x in input().split(" ")]
        divisors.sort()
        if n == 1:
            print(divisors[0] * 2)
        else:
            lcm_ans = lcm(divisors[0], divisors[1])
            if lcm_ans == divisors[0] * divisors[1]:
                print(lcm_ans)
            else:
                print(-1)

if __name__ == "__main__":
    main()