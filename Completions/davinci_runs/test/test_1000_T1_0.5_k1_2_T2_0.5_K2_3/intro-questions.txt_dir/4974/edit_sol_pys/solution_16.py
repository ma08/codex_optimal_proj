
n, m = map(int, input().split())

for i in range(1, n+1):
    if i not in map(int, input().split()):
        print(i)
        break
else:
    print("too late")
