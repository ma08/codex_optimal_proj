

a = int(input('Input a: '))
b = int(input('Input b: '))
c = int(input('Input c: '))
x = int(input('Input x: '))
count = 0
for i in range(a + 1):
    for j in range(b + 1):
        for k in range(c + 1):
            if i * 500 + j * 100 + k * 50 == x:
                count += 1
print(count)
