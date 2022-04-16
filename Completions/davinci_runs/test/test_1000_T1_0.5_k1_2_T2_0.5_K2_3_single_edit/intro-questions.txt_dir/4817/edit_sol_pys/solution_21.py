

x = int(input())
n = 10 ** (len(str(x)) - 1)
for i in range(9, 0, -1):
    if str(i) in str(x):
        n += i * 10 ** (len(str(x)) - str(x).index(str(i)) - 1)
        break
for i in range(9, 0, -1):
    if str(i) in str(n):
        n += i * 10 ** (len(str(x)) - str(n).index(str(i)) - 1)
        break
if n > x:
    print(n)
else:
    print(0)
