

def is_completed(wall):
    """
    >>> is_completed([1, 1, 1, 1, 1])
    True
    >>> is_completed([1, 1, 2, 1, 1])
    False
    >>> is_completed([1, 2, 1, 2, 1])
    False
    """
    for i in range(len(wall) - 1):
        if wall[i] != wall[i + 1]:
            return False
    return True

def complete_the_wall(wall):
    """
    >>> complete_the_wall([2, 1, 1, 2, 5])
    [5, 5, 5, 5, 5]
    >>> complete_the_wall([4, 5, 3])
    [4, 5, 3]
    >>> complete_the_wall([10, 10])
    [10, 10]
    """
    while not is_completed(wall):
        for i in range(len(wall) - 1):
            if wall[i] == wall[i + 1]:
                wall[i] += 1
                wall[i + 1] += 1
    return wall


if __name__ == '__main__':
    n = int(input())
    wall = list(map(int, input().split()))
    print("YES" if is_completed(complete_the_wall(wall)) else "NO")