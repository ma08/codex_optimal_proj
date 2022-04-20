

def sgsn(n, k):
    count = 0
    for i in range(1, n+1):
        if str(k) in str(i):
            count += 1
    return count

n, k = map(int, input().split())
print(sgsn(n, k))
