
# Python 2.7.12

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    a, b = map(int, raw_input().split())
    g = gcd(a, b)
    a /= g
    b /= g
    if a == b:
        print 4 * a
    else:
        print 2 * (a + b)

main()
