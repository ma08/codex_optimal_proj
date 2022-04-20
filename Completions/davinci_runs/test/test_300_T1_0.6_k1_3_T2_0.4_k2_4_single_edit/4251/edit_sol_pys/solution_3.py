
n,m = [int(x) for x in input().split()]
matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)
matrix.sort(key=lambda x: -min(x))
#print(matrix)
def is_valid(k, matrix):
    for i in range(m):
        for j in range(n-1):
            if abs(matrix[j][i] - matrix[j+1][i]) < k:
                return False
    return True
l,r = 0,10**9
while l < r:
    m = (l+r)//2
    if is_valid(m, matrix):
        r = m
    else:
        l = m+1
print(r)
