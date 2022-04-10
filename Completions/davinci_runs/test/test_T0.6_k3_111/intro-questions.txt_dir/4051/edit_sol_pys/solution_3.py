
n = int(input())
list = list(map(int,input().split()))
if n == 1:
    print("YES")
else:
    list.sort()
    if list[0] >= list[1]:
        print("NO")
    else:
        i = 1
        while i < n-1:
            if list[i] - list[i-1] >= 2:
                print("NO")
                break
            i+=1
        else:
            print("YES")
