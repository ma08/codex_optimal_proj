

input = list(input())

count = 0
for i in range(len(input)):
    if int(input[i]) % 3 == 0:
        count += 1
print(count)
