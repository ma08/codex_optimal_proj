

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    n = int(input())
    s = input()
    t = input()
    if s == t:
        print('same')
    elif s.lower() == t.lower():
        print('case-insensitive')
    else:
        print('different')

if __name__ == '__main__':
    main()
