

from fractions import gcd

def main():
    inputstring = input()
    a, b, k = map(int, inputstring.split())
    g = gcd(a,b)
    print(g*(k-1))

if __name__ == "__main__":
    main()
