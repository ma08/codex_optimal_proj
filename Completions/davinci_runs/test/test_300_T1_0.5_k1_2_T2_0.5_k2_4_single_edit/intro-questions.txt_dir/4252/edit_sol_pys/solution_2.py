

n = int(input())
file_name = input()

count = 0
for i in range(2, n+1):
    if file_name[i-2:i+1] == "xxx":
        count += 1

print(count)
