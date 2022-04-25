

n = int(input())
filename = input()

count = 0
for i in range(2, n):
    if filename[i-2] == filename[i-1] and filename[i-1] == filename[i]:
        count += 1

print(count)
