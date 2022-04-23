

a,b,c = map(int, input().split())

count = 0
while b >= a and count <= c:
    b -= a
    count += 1
print(count)
