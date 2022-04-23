

def sgsn(n, x):
    count = 0
    for i in range(1, n+1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i) and i % x == 0:
            count += 1
    return count

n = int(input())
x = int(input())
print(sgsn(n, x))
