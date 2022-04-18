

N = int(input())

for i in range(N//4+1): # 4
    for j in range(N//7+1): # 7
        if N == i*4 + j*7:
            print("Yes")
            exit()
print("No")
