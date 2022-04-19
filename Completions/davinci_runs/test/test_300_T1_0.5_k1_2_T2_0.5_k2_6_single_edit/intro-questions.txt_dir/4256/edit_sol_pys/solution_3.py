
a, b, c = map(int, input().split())
 
ans = 0
while b >= a and ans < c:
    b -= a
    ans += 1
print(ans)
