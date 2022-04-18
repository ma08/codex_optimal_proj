
r, n = map(int, input().split())

if n != r:
    for i in range(1, r+1):
        if i not in map(int, input().split()):
            print(i)
            break
    else:
        print("too late")
else:
    print(input())
