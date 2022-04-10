n = int(input())
arr = list(map(int,input().split()))
arr.sort()
if arr[0] >= arr[1]:
    print("NO")
else:
    i = 1
    while i < n-1:
        if arr[i] - arr[i-1] >= 2:
            print("NO")
            break
        i+=1
    else:
        print("YES")
