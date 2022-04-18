def swap(s, i, j):
    return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

n1 = int(input())
n2 = int(input())
row1 = input()
row2 = input()
t = int(input()) + 1

for i in range(t):
    if row1[0] != row2[0]:
        row1 = swap(row1, 0, 1)
        row2 = swap(row2, 0, 1)
    else:
        row1 = swap(row1, 0, 1)
        row2 = swap(row2, 1, 2)

print(row1 + row2)
