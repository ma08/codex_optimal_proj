

n = int(input())
helium = sorted(list(map(int, input().split())))

if helium[0] == 0:
    print("impossible")
else:
    print(int(helium[0]/n))
