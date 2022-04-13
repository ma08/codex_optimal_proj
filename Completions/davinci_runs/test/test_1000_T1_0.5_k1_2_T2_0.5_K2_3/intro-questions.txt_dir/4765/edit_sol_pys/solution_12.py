

# SOLUTION 

def perket(n, a):
    if n == 1:
        return abs(a[0][0] - a[0][1])
    m = 10**9
    for i in range(n):
        for j in range(i+1, n):
            m = min(m, abs((a[i][0]*a[j][0]) - (a[i][1] + a[j][1])))
    return m

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
print(perket(n, a))
