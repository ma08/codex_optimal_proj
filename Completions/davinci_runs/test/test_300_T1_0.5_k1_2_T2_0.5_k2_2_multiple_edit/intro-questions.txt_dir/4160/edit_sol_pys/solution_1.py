

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for x in range(c, d+1):
    print('\t', x, end='')
print()
for y in range(a, b+1):
    print(y, end='\t')
    for x in range(c, d+1):
        print(x * y, end='\t')
    print()
