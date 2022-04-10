

# cook your dish here
a,b,c = map(int, input().split())
ans = 1
while a>=1 and b>=1 and c>=1:
    ans = ans + 1
    a -= 1
    b -= 1
    c -= 1
print(ans)