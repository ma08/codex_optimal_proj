n, k = [int(x) for x in input().split()]


if k == 1:
    print("YES")
    print(n * "a")
    exit(0)

p = [1] + [int(x) for x in input().split()]
q = [2] + [int(x) for x in input().split()]

letters = list(map(chr, range(97, 97 + k)))

s = [None] * n
s[q[0] - 1] = letters[0]

for i in range(1, n + 1):
    if s[p[i] - 1] is None:
        s[p[i] - 1] = s[p[i - 1] - 1]
    if s[q[i] - 1] is None:
        s[q[i] - 1] = s[q[i - 1] - 1]
    if s[p[i] - 1] == s[q[i] - 1]:
        print("NO")
        exit(0)

for i in range(k, n + 1):
    if s[p[i] - 1] is None:
        s[p[i] - 1] = letters[i % k]
    if s[q[i] - 1] is None:
        s[q[i] - 1] = letters[i % k]

print("YES")
print("".join(s))
