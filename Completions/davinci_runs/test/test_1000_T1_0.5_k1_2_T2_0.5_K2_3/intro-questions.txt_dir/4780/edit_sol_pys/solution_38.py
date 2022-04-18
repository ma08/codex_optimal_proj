

def swap(s, i, j):  # s - string, i, j - indices of chars in string
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]  # swap chars at indices i and j in string s

n1, n2 = map(int, input().split())  # n1 - number of chars in row1, n2 - number of chars in row2
row1 = input()  # first row
row2 = input()  # second row
t = int(input())  # number of swaps to do

for i in range(t):  # do swaps
    if row1[0] != row2[0]:
        row1 = swap(row1, 0, 1)
        row2 = swap(row2, 0, 1)
    else:
        row1 = swap(row1, 0, 1)
        row2 = swap(row2, 1, 2)

print(row1 + row2)
