n = int(input())
ravi = list(map(int,input().split()))
if n == 1:
    print("YES")
else:
    ravi.sort()
    if ravi[0] >= ravi[1]:
        print("NO")
    else:
        i = 1
        while i < n-1:
            if ravi[i] - ravi[i-1] >= 2:
                print("NO")
                break
            i+=1
        else:
            print("YES")
