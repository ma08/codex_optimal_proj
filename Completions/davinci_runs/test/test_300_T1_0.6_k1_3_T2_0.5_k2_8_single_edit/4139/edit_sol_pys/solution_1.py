

def sgsn(n):
    count = 0
    for i in range(1, n+1):  # n+1 because we have to count n also
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            count += 1
    return count

n = int(input())  # input n
print(sgsn(n))  # print the result
