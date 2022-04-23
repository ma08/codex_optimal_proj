

n,w = map(int, input().split())
a = list(map(int, input().split()))
def check(x):
    b = [0]*n
    b[0] = x
    flag = True
    for i in range(1,n):
        b[i] = b[i-1] + a[i-1]
        if b[i] < 0 or b[i] > w:
            flag = False
            break
    return flag

k = 0
for i in range(w+1):
    if check(i):
        k += 1
print(k)
