
input = input.strip()
input = input()

if len(input) == 1:
    print(0)
else:
    count = 0
    for i in range(1, len(input)):
        if int(input[:i]) % 3 == 0:
            count += 1
    print(count)
