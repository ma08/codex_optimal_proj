
l = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for i in range(1, len(l)):
    print(l[i], l[i-1], l[i] % l[i-1])
