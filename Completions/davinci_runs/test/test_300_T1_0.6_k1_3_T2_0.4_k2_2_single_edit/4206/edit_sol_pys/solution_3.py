

input_data = input()

if len(input_data) == 1:
    print(1)
else:
    count = 0
    for i in range(1, len(input_data)):
        if int(input_data[:i]) % 3 == 0:
            count += 1
    print(count)
