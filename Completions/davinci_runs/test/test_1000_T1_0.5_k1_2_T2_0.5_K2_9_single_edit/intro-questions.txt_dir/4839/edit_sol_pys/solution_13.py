from statistics import median

n = int(input())
helium = list(map(int, input().split()))

if helium[0] == 0:
    print("impossible")
else:
    print(median(helium)/n)
