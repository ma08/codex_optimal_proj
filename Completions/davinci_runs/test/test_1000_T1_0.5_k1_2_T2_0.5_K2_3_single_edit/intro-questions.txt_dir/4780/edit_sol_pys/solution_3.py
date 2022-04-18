

def swap(s, i, j):
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:], s[:j] + s[i] + s[j+1:i] + s[j] + s[i+1:]

n1, n2 = map(int, input().split())
row1 = input()
row2 = input()
t = int(input())

for i in range(t):
    if row1[0] != row2[0]:
        row1, row2 = swap(row1, 0, 1)
    else:
        row1, row2 = swap(row1, 0, 1)

print(row1 + row2)
