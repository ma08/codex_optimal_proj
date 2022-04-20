

n, x, y = [int(x) for x in input().split()]
n = input()

# 1) count the number of 1s in the first x digits
# 2) count the number of 1s in the first y digits
# 3) subtract to find the number of 1s that we need to add to the first y digits to get a remainder of 10^y
# 4) subtract the number of 1s in the first x digits from the number of 1s needed in the first y digits
# 5) if the result is positive, we need to add 1s to the first x digits
# 6) if the result is negative, we need to add 1s to the first y digits

ones_in_x = sum(int(x) for x in n[:x])
ones_in_y = sum(int(x) for x in n[:y])

ones_needed_y = 10**y - ones_in_y
ones_needed_x = ones_needed_y - ones_in_x

if ones_needed_x > 0:
    print(ones_needed_x)
else:
    print(ones_needed_y)