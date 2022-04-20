

# Version 1

def solution(n):
    # Your code here
    digits = list(str(n))
    while len(digits) > 1:
        next_sum = 0
        for i in digits:
            next_sum += int(i) ** 2
        digits = list(str(next_sum))
    return digits[0]

# Version 2

def solution(n):
    # Your code here
    digits = list(str(n))
    while len(digits) > 1:
        next_sum = 0
        for i in digits:
            next_sum += int(i) ** 2
        digits = list(str(next_sum))
    return digits[0]
