

n = int(input())
a = list(map(int, input().split()))

# check if all heights are the same
if len(set(a)) == 1:
    print("YES")
else:
    # check if there are any gaps
    for i in range(n-1):
        if a[i] != a[i+1]:
            print("NO")
            break
    else:
        print("YES")