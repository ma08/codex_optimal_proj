a = []
r, n = map(int, input().split())

for i in range(1, r+1):
    a = map(int, input().split())
    if i not in a:
        print(i)
        break
else:
    print("too late")
