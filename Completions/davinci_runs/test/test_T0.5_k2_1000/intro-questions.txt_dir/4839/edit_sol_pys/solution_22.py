
n = int(input())
helicopter = list(map(int, input().split()))
helicopter.sort()

if helicopter[0] == 0:
    print("impossible")
else:
    print(helicopter[0]/n)
