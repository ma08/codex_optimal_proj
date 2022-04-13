

N = int(input())  # number of sticks
L = list(map(int, input().split()))  # length of sticks
 
L.sort()

if L[0] + L[1] > L[-1]:
    print("Yes")
else:
    print("No")
