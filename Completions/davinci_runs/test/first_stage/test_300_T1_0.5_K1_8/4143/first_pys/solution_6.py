

n = int(input())
a,b,c,d,e = map(int, input().split())

ans = n//a
if n%a > 0:
    ans += 1

ans += (ans//b)*(b//c)*(c//d)*(d//e)

if ans%b > 0:
    ans += (ans%b)//c
    if (ans%b)%c > 0:
        ans += ((ans%b)%c)//d
        if ((ans%b)%c)%d > 0:
            ans += (((ans%b)%c)%d)//e
            if (((ans%b)%c)%d)%e > 0:
                ans += 1

print(ans)