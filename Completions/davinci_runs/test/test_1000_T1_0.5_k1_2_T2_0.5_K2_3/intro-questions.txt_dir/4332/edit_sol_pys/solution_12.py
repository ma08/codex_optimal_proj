
N = int(input())

if N % sum([int(x) for x in list(str(N))]) == 0:  # N % sum(map(int, list(str(N))))でも可
    print("Yes")
else:
    print("No")
