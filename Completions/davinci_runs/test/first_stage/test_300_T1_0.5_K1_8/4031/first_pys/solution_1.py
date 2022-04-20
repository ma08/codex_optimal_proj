

n = int(input())
strings = []
for i in range(n):
    strings.append(input())
strings.sort()

for i in range(n-1):
    if not strings[i] in strings[i+1]:
        print("NO")
        exit()

print("YES")
print("\n".join(strings))