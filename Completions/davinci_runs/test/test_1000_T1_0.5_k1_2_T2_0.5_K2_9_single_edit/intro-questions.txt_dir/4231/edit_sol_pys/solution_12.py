

def main():
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for i in range(N):
        m = int(input())
        if m < 400:
            a += 1
        elif m < 800:
            b += 1
        elif m < 1200:
            c += 1
        elif m < 1600:
            d += 1
        elif m < 2000:
            e += 1
        else:
            e += 1
    if a > 0:
        a = 1
    if b > 0:
        b = 1
    if c > 0:
        c = 1
    if d > 0:
        d = 1
    if e > 0:
        e = 1
    print(a+b+c+d+e, a+b+c+d+e+e)

if __name__ == '__main__':
    main()
