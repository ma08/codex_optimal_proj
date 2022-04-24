

def is_divisible_by_three(n):
    return sum([int(x) for x in list(str(n))]) % 3 == 0

def max_divisible_three_cuts(s):
    count = 0
    for i in range(len(str(s))):
        for j in range(i + 1, len(str(s)) + 1):
            if is_divisible_by_three(int(str(s)[i:j])):
                count += 1
    return count


print(max_divisible_three_cuts(3121))
print(max_divisible_three_cuts(6))
print(max_divisible_three_cuts(1000000000000000000000000000000000))
print(max_divisible_three_cuts(201920181))
