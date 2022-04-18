
a = input()
b = list(map(int, input().split()))
print(1, end=" ")
for i in range(len(b)):
    print(i+2+b[i], end=" ")
