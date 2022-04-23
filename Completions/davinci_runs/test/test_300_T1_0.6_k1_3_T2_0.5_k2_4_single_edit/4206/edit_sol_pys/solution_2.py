

input1 = input()

if len(input1) == 1:
    print(1)
else:
    count = 0
    for i in range(1, len(input1)):
        if int(input1[:i]) % 3 == 0:
            count += 1
    print(count)
