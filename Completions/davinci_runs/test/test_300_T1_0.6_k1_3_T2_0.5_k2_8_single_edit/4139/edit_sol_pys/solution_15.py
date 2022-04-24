

def sgsn(n):
    count = 0
    for i in range(1, n+1):
        if '7' in str(i) or '5' in str(i) or '3' in str(i):
            count += 1
    return count

n = int(input())
print(sgsn(n))
