
n = int(input())
rav = list(map(int,input().split()))
if n == 1:
    print("YES")
else:
    rav.sort()
    if rav[0] >= rav[1]:
        print("NO")
    else:
        i = 1
        while i < n-1:
            if rav[i] - rav[i-1] >= 2:
                print("NO")
                break
            i+=1
        else:
            print("YES")