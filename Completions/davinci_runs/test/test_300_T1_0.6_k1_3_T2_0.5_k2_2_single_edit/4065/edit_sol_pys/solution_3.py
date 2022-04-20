

def getMaxContest(a, k):
    a.sort()
    n = len(a) - 1

a = list(map(int, input().split()))
print(getMaxContest(a))
