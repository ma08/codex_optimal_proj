def find_max_min(numbers):
    '''
    Function to find the maximum and minimum number in a list.
    '''
    if len(numbers) == 0:
        return numbers
    max_number = numbers[0]
    min_number = numbers[0]
    for i in range(1, len(numbers)):
        if max_number < numbers[i]:
            max_number = numbers[i]
        if min_number > numbers[i]:
            min_number = numbers[i]
    if max_number == min_number:
        return [max_number]
    return [min_number, max_number]

def find_max_min(numbers):
    if len(numbers) == 0:
        return numbers
    max_number = numbers[0]
    min_number = numbers[0]
    for i in range(1, len(numbers)):
        if max_number < numbers[i]:
            max_number = numbers[i]
        if min_number > numbers[i]:
            min_number = numbers[i]
    if max_number == min_number:
        return [max_number]
    return [min_number, max_number]
