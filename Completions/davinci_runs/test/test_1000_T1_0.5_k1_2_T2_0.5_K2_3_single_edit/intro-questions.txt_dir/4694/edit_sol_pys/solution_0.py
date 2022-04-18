# ABC081B - Shift only

# input
N = int(input())
a_list = list(map(int, input().split()))

# find the minimum distance
result = float('inf')
while True:
    for i in range(N):
        if a_list[i] % 2 != 0:
            print(result)
            exit()
    result += 1
    for i in range(N):
        a_list[i] = a_list[i] // 2

# output
print(result)
