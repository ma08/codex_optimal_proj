

n, m = map(int, input().split())

if n == 1:
    print(1)
    exit()

if n == 2:
    print(min(4, (m+1)//2))
    exit()

if m < 7:
    print(min(4, m))
    exit()

print(m-2)
