

def get_number_of_operations(a, b, c):
    res = 0
    a_divisor = a
    b_divisor = b
    c_divisor = c
    while True:
        if a_divisor == 0 and b_divisor == 0 and c_divisor == 0:
            return res
        elif a_divisor == 0 and b_divisor == 0 and c_divisor > 0:
            res += c_divisor
            c_divisor = 0
        elif a_divisor == 0 and b_divisor > 0 and c_divisor == 0:
            res += b_divisor
            b_divisor = 0
        elif a_divisor == 0 and b_divisor > 0 and c_divisor > 0:
            if b_divisor > c_divisor:
                res += b_divisor - c_divisor
                b_divisor = c_divisor
            elif b_divisor < c_divisor:
                res += c_divisor - b_divisor
                c_divisor = b_divisor
            else:
                pass
        elif a_divisor > 0 and b_divisor == 0 and c_divisor == 0:
            res += a_divisor
            a_divisor = 0
        elif a_divisor > 0 and b_divisor == 0 and c_divisor > 0:
            if a_divisor > c_divisor:
                res += a_divisor - c_divisor
                a_divisor = c_divisor
            elif a_divisor < c_divisor:
                res += c_divisor - a_divisor
                c_divisor = a_divisor
            else:
                pass
        elif a_divisor > 0 and b_divisor > 0 and c_divisor == 0:
            if a_divisor > b_divisor:
                res += a_divisor - b_divisor
                a_divisor = b_divisor
            elif a_divisor < b_divisor:
                res += b_divisor - a_divisor
                b_divisor = a_divisor
            else:
                pass
        elif a_divisor > 0 and b_divisor > 0 and c_divisor > 0:
            if a_divisor > b_divisor:
                if a_divisor > c_divisor:
                    res += a_divisor - c_divisor
                    a_divisor = c_divisor
                elif a_divisor < c_divisor:
                    res += c_divisor - a_divisor
                    c_divisor = a_divisor
                else:
                    pass
            elif a_divisor < b_divisor:
                if b_divisor > c_divisor:
                    res += b_divisor - c_divisor
                    b_divisor = c_divisor
                elif b_divisor < c_divisor:
                    res += c_divisor - b_divisor
                    c_divisor = b_divisor
                else:
                    pass
            else:
                pass


def get_triple(a, b, c):
    a_divisor = a
    b_divisor = b
    c_divisor = c
    while True:
        if a_divisor == 0 and b_divisor == 0 and c_divisor == 0:
            return a, b, c
        elif a_divisor == 0 and b_divisor == 0 and c_divisor > 0:
            c -= c_divisor
            c_divisor = 0
        elif a_divisor == 0 and b_divisor > 0 and c_divisor == 0:
            b -= b_divisor
            b_divisor = 0
        elif a_divisor == 0 and b_divisor > 0 and c_divisor > 0:
            if b_divisor > c_divisor:
                b -= b_divisor - c_divisor
                b_divisor = c_divisor
            elif b_divisor < c_divisor:
                c -= c_divisor - b_divisor
                c_divisor = b_divisor
            else:
                pass
        elif a_divisor > 0 and b_divisor == 0 and c_divisor == 0:
            a -= a_divisor
            a_divisor = 0
        elif a_divisor > 0 and b_divisor == 0 and c_divisor > 0:
            if a_divisor > c_divisor:
                a -= a_divisor - c_divisor
                a_divisor = c_divisor
            elif a_divisor < c_divisor:
                c -= c_divisor - a_divisor
                c_divisor = a_divisor
            else:
                pass
        elif a_divisor > 0 and b_divisor > 0 and c_divisor == 0:
            if a_divisor > b_divisor:
                a -= a_divisor - b_divisor
                a_divisor = b_divisor
            elif a_divisor < b_divisor:
                b -= b_divisor - a_divisor
                b_divisor = a_divisor
            else:
                pass
        elif a_divisor > 0 and b_divisor > 0 and c_divisor > 0:
            if a_divisor > b_divisor:
                if a_divisor > c_divisor:
                    a -= a_divisor - c_divisor
                    a_divisor = c_divisor
                elif a_divisor < c_divisor:
                    c -= c_divisor - a_divisor
                    c_divisor = a_divisor
                else:
                    pass
            elif a_divisor < b_divisor:
                if b_divisor > c_divisor:
                    b -= b_divisor - c_divisor
                    b_divisor = c_divisor
                elif b_divisor < c_divisor:
                    c -= c_divisor - b_divisor
                    c_divisor = b_divisor
                else:
                    pass
            else:
                pass

if __name__ == "__main__":
    t = int(input())
    for i in range(0, t):
        a, b, c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        res = get_number_of_operations(a, b, c)
        a, b, c = get_triple(a, b, c)
        print(res)
        print(a, b, c)
