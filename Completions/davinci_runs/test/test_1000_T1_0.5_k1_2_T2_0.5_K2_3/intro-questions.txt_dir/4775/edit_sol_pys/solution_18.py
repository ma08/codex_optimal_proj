a = input()
b = input()
for i in range(len(b)):
    for j in range(len(a)):
        print(b[i] if a[j] == b[i] else '.', end='')
    print('')
