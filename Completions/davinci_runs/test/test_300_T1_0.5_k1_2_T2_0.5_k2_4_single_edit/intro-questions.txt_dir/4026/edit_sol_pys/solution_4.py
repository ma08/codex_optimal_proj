

t = int(input())

for i in range(t):
    n = int(input())
    
    arr = []
    
    for j in range(n):
        arr.append(input().split())
        
    for j in range(n - 1):
        for k in range(n - 1):
            if arr[j][k] == arr[j + 1][k] and arr[j][k] == arr[j][k + 1] and arr[j][k] == arr[j + 1][k + 1]:
                print("YES")
                break
            else:
                print("NO")
                break
        break
    
