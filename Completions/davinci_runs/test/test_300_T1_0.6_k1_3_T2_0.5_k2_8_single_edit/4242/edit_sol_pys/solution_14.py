
from fractions import gcd

def main():
    inputstring = input()
    a, b, k = map(int, inputstring.split())
    g = gcd(a,b)
    for i in range(k-1):
        g = gcd(g, min(a,b))
        if g == 1:
            break
    print(g)

if __name__ == "__main__":
    main()
