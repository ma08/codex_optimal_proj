N = int(input())

for i in range(N // 4 + 1):  # 4の倍数になるまで回す
    for j in range(N // 7 + 1):  # 7の倍数になるまで回す
        if N == i * 4 + j * 7:
            print("Yes")
            exit(0)
print("No")
