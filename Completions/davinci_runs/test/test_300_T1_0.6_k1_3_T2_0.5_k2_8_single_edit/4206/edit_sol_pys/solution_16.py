

input_value = input()

if len(input_value) == 1:
    print(1)
else:
    count = 0
    for i in range(1, len(input_value)):
        if int(input_value[:i]) % 3 == 0:
            count += 1
    print(count)
