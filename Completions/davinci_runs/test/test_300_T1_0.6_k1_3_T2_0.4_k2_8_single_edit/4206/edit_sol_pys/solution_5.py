

input_str = input()

if len(input_str) == 1:
    print(1)
else:
    count = 0
    for i in range(1, len(input_str)):
        if int(input_str[:i]) % 3 == 0:
            count += 1
    print(count)
