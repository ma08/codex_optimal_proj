

input_ = input()

if len(input_) == 1:
    print(1)
else:
    count = 0
    for i in range(1, len(input_)):
        if int(input_[:i]) % 3 == 0:
            count += 1
    print(count)
