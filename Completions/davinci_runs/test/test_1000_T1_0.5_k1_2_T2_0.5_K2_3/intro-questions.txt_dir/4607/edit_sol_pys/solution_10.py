

a = int(input())
x = 0
for i in range(1, a + 1):
    if i == int(str(i)[-1]):
        x += 1
print(x)
