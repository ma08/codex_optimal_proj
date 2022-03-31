n,k = map(int,input().split()) # n is the number of elements, k is the number of groups

if n%k == 0: # if n is divisible by k
    print("YES")
    for i in range(k): # for each group
        print(n//k,end=" ") # print the number of elements in the group
else:
    print("NO")
