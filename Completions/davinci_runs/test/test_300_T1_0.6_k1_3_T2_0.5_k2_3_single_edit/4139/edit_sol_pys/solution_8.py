
#N = int(input())
N = 575

def ShichiGoSan(n):
    return "7" in str(n) and "5" in str(n) and "3" in str(n)

print(len([i for i in range(1,N+1) if ShichiGoSan(i)]))
