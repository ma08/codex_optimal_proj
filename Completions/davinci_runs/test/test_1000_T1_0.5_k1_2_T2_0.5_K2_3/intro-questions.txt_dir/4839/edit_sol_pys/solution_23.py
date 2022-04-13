
n = int(input()) 
helium = list(map(int, input().split()))
helium.sort()

if helium[0] == 0:
    print("impossible")
else:
    print(helium[0]/n)
