

from fractions import gcd

def main():
    inputstring = input()
    a, b, k = map(int, inputstring.split())
    g = gcd(a,b)
    if g == 1:
        print(1)
        return
    g = gcd(g, min(a,b))
    print(g)

if __name__ == "__main__":
    main()
