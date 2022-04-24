

def sgsn(n): # sgsn is an abbreviation of "saya gak suka nomor"
    count = 0
    for i in range(1, n+1):
        if '7' in str(i) and '5' in str(i) and '3' in str(i):
            count += 1
    return count

n = int(input())
print(sgsn(n))
