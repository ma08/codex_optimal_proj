

n = int(input())
l = input()
r = input()

def get_compatible(a, b):
    if a == '?' or b == '?':
        return True
    return a == b

matches = []
for i in range(n):
    for j in range(n):
        if get_compatible(l[i], r[j]):
            matches.append((i, j))

print(len(matches))
for i, j in matches:
    print(i+1, j+1)