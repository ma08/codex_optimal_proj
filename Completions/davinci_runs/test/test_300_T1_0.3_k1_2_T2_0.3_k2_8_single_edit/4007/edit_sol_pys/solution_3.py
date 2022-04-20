
n = int(input())
f = list(map(int, input().split()))

for i in range(n):
    if f[i] == 0:  # if the number is not in the list
        for j in range(1, n+1):  # iterate through the list
            if j not in f:  # if the number is not in the list
                f[i] = j  # assign the number to the list
                break  # break the loop

print(*f)
