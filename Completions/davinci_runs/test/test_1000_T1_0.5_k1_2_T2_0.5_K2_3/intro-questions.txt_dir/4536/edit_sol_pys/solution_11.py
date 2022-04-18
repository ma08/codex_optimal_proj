
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    plus = 1
    for i in range(len(digits) - 1, -1, -1):
        if plus == 1:
            if digits[i] + 1 == 10:
                digits[i] = 0
            else:
                digits[i] += 1
                plus = 0
        else:
            break
    if plus == 1:
        digits.insert(0, 1)
    return digits


print(plusOne([9, 9, 9]))
