

def sgsn(n, k):
    count = 0
    for i in range(1, n+1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i) and i % k == 0:
            count += 1
    return count

n, k = map(int, input().split())
print(sgsn(n, k))
