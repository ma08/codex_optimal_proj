

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    """
    if len(ints) == 0:
        return (None, None)
    min = ints[0]
    max = ints[0]
    for i in ints:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)
