
count = 0
input = input()

if len(input) == 1:
    print(1)
else:
    for i in range(1, len(input)):
        if int(input[:i]) % 3 == 0:
            count += 1
print(count)
