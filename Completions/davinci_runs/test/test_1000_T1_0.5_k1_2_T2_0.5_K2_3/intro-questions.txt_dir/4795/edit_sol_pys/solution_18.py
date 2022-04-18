n = int(input())
result = 0
for i in range(n):
    number = input()
    for j in range(1, len(number)):
        if int(number[j]) != 0:
            result += int(number[:j]) ** int(number[j])
            break
print(result)
