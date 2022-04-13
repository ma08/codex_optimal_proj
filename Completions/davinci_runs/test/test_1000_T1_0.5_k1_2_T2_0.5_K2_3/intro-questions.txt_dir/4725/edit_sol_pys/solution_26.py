
def find_max_min(numbers):
    if max(numbers) == min(numbers):
        return [max(numbers)]
    return [min(numbers), max(numbers)]
