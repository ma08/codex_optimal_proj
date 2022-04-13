

def swap(s, i, j):
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:] # [:i] - от начала до i, [i+1:j] - от i+1 до j, [j+1:] - от j+1 до конца строки

n1, n2 = map(int, input().split()) # n1, n2 = 2, 3
row1 = input()
row2 = input()
t = int(input())

for i in range(t):
    if row1[0] != row2[0]:
        row1 = swap(row1, 0, 1)
        row2 = swap(row2, 0, 1)
    else:
        row1 = swap(row1, 0, 1)
        row2 = swap(row2, 1, 2)

print(row1 + row2)
