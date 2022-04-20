

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def main():
    t = int(input())
    for _ in range(t):
        a, b, c = [int(x) for x in input().split()]
        res = 0
        while True:
            if b % a == 0 and c % b == 0:
                break
            if b % a != 0 and c % b != 0:
                if b % a == 0:
                    c += 1
                elif c % b == 0:
                    a += 1
                else:
                    a += 1
                    b += 1
                    c += 1
            elif b % a != 0:
                a += 1
            else:
                c += 1
            res += 1
        print(res)
        print(a, b, c)

main()