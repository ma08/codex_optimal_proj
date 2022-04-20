
input = input()

if len(input) == 1:
    print(1)
else:
    count = 0
    for i in range(0, len(input)):
        if int(input[:i+1]) % 3 == 0:
            count += 1
    print(count)
