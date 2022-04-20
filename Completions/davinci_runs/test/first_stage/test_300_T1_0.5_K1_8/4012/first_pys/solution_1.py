

t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    if b % a == 0 and c % b == 0:
        print(0)
        print(a, b, c)
    else:
        res = 0
        while True:
            if a == b and b == c:
                break
            if a == b:
                if c % b == 0:
                    break
                else:
                    c -= 1
                    res += 1
                    continue
            if b % a == 0:
                if c % b == 0:
                    break
                else:
                    c -= 1
                    res += 1
                    continue
            if c % b == 0:
                if b % a == 0:
                    break
                else:
                    a += 1
                    res += 1
                    continue
            if b % a == 0 and c % b == 0:
                break
            if c % b != 0:
                c -= 1
                res += 1
            if b % a != 0:
                a += 1
                res += 1
        print(res)
        print(a, b, c)