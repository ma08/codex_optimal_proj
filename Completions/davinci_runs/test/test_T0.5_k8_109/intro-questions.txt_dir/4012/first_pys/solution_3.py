

#-----Solution-----

def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
    return x 

def solution(a,b,c):
    res = 0
    if a == b == c:
        return 0, str(a)+" "+str(b)+" "+str(c)
    if a == b:
        if a == 1:
            if c%a == 0:
                return 1, str(a)+" "+str(b)+" "+str(c)
            else:
                return 2, str(a)+" "+str(b)+" "+str(c-1)
        else:
            return 1, str(a)+" "+str(b)+" "+str(c)
    elif b == c:
        if b == 1:
            if a%b == 0:
                return 1, str(a)+" "+str(b)+" "+str(c)
            else:
                return 2, str(a-1)+" "+str(b)+" "+str(c)
        else:
            return 1, str(a)+" "+str(b)+" "+str(c)
    elif a == c:
        if a == 1:
            if b%a == 0:
                return 1, str(a)+" "+str(b)+" "+str(c)
            else:
                return 2, str(a)+" "+str(b-1)+" "+str(c)
        else:
            return 1, str(a)+" "+str(b)+" "+str(c)
    else:
        gcd = find_gcd(a,b)
        if c%gcd == 0:
            return res, str(a)+" "+str(b)+" "+str(c)
        else:
            if a == 1:
                res += 1
                a += 1
            else:
                a += 1
            gcd = find_gcd(a,b)
            if c%gcd == 0:
                return res, str(a)+" "+str(b)+" "+str(c)
            else:
                if b == 1:
                    res += 1
                    b += 1
                else:
                    b += 1
                gcd = find_gcd(a,b)
                if c%gcd == 0:
                    return res, str(a)+" "+str(b)+" "+str(c)
                else:
                    if c == 1:
                        res += 1
                        c += 1
                    else:
                        c += 1
                    gcd = find_gcd(a,b)
                    if c%gcd == 0:
                        return res, str(a)+" "+str(b)+" "+str(c)
                    else:
                        return res, str(a)+" "+str(b)+" "+str(c-1)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a,b,c = map(int, input().split())
        res, ans = solution(a,b,c)
        print(res)
        print(ans)