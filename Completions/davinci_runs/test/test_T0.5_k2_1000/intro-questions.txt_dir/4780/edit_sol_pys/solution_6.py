

def swap(s, i, j):  # swap s[i] and s[j] O(n)
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

n1, n2 = map(int, input().split())  # O(1)
row1 = input()  # O(n)
row2 = input()  # O(n)
t = int(input())  # O(1)

for i in range(t):
    if row1[0] != row2[0]:
        row1 = swap(row1, 0, 1)
        row2 = swap(row2, 0, 1)
    else:
        row1 = swap(row1, 0, 1)
        row2 = swap(row2, 1, 2)

print(row1 + row2)
