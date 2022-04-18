

def divisible_by_3(input):
    if len(input) == 1:
        return 1
    else:
        count = 0
        for i in range(1, len(input)):
            if int(input[:i]) % 3 == 0:
                count += 1
        return count

input = input()
print(divisible_by_3(input))
