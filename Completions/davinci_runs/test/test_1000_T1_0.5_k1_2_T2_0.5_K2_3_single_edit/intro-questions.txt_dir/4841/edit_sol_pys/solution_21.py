

n = int(input())
a = input().split()
if a[0] != "mumble":
    for i in range(n):
        if a[i] != "mumble" and int(a[i]) != i+1:
            print("something is fishy")
            exit()

print("makes sense")
