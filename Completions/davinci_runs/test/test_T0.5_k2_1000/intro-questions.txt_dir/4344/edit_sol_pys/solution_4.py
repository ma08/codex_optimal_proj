a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, len(a)):
    if i % 2 == 0:
        a[i] = 0
print(a)
