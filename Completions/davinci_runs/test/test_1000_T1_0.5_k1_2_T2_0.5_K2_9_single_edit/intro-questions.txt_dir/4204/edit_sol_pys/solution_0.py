
s = input()
k = int(input())

for i in range(1, 10):
    s = s.replace(str(i), str(i)*i)

print(s[k-1])
