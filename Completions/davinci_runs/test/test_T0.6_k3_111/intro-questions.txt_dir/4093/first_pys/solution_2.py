

for i in range(int(input())):
    n, m = map(int, input().split())
    a = m//n
    b = m%n
    print(n*a*(a+1)//2 + b*(a+1))