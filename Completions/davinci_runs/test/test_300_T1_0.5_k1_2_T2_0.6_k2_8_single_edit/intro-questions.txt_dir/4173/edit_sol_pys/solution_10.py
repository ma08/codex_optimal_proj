
for _ in range(int(input())):
    n,a,b=int(input().split())
    print(n*a if n*a<b else (n//2)*b+(n%2)*a)
