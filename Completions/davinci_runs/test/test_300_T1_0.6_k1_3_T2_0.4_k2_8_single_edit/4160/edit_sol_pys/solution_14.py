
x = int(input())
a = 100
years = 0
while a < x:
    a += a // 100
    years += 1
print(years)
