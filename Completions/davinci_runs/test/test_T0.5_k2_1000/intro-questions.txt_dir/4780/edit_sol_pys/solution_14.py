
# SOLUTION

def swap_ants(a, b, t):
    """
    Swaps ants between two lines.

    :param a: List of ants in line A
    :param b: List of ants in line B
    :param t: Number of seconds
    :return: List of ants in line A and B after t seconds
    """

    # Reverse lists if needed
    if t % 2 == 1:
        a, b = b, a

    # Swap ants in lists
    for i in range(t // 2):
        a.insert(i + 1, b[i])
        b.insert(i + 1, a[-i - 1])
        a.pop(-i - 1)
        b.pop(i)

    return a + b


if __name__ == '__main__':
    # Read input
    n1, n2 = [int(x) for x in input().split()]
    a = [x for x in input()]
    b = [x for x in input()]
    t = int(input())

    # Print result
    print(''.join(swap_ants(a, b, t)))
