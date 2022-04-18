

input = int(input())

if input == 1:
    print(1)
else:
    count = 0
    for i in range(1, input):
        if i % 3 == 0:
            count += 1
    print(count)
