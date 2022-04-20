

def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        res = 0
        while a * b * c != 0 and not (b % a == 0 and c % b == 0) and not (a == b and b == c):
            if a == b:
                if c % 2 == 0:
                    c //= 2
                else:
                    c += 1
            elif b == c:
                if a % 2 == 0:
                    a //= 2
                else:
                    a += 1
            elif a == c:
                if b % 2 == 0:
                    b //= 2
                else:
                    b += 1
            elif a > b:
                if b % 2 == 0:
                    b //= 2
                else:
                    b += 1
            elif b > c:
                if c % 2 == 0:
                    c //= 2
                else:
                    c += 1
            elif c > a:
                if a % 2 == 0:
                    a //= 2
                else:
                    a += 1
            res += 1
        print(res)

if __name__ == '__main__':
    main()
