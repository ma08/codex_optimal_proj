

# SOLUTION

# The idea is to find the number that is at the given position
# Then find the digit at the given position
# The number at the given position can be found by using binary search

q = int(input())
for i in range(q):
    k = int(input())
    start = 1
    end = 2**31 - 1
    while start <= end:
        mid = (start + end) // 2
        if (mid * (mid + 1)) // 2 < k:
            start = mid + 1
        else:
            end = mid - 1
    # print(start)
    num = start
    num_digits = len(str(num))
    # print(num_digits)
    # print((num * (num + 1)) // 2 - (num_digits * 45))
    # print(k - ((num * (num + 1)) // 2 - (num_digits * 45)))
    # print(str(num)[k - ((num * (num + 1)) // 2 - (num_digits * 45)) - 1])
    print(str(num)[k - ((num * (num + 1)) // 2 - (num_digits * 45)) - 1])