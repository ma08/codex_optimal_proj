

def bamboo_magic(A, B, C, bamboos):
    """
    :type A: int
    :type B: int
    :type C: int
    :type bamboos: list
    :rtype: int
    """
    # initialization
    magic_points = 0
    # check if there is a bamboo of length A
    if A in bamboos:
        # remove it to get the bamboos that are shorter than A
        bamboos.remove(A)
    # for each bamboo of length b in bamboos that's shorter than A
    for b in bamboos:
        # if b is shorter than A - B
        if b < A - B:
            # decrease its length by 1
            b -= 1
            # increase the magic point
            magic_points += 1
        # if b is shorter than A - C
        if b < A - C:
            # decrease its length by 1
            b -= 1
            # increase the magic point
            magic_points += 1
        # if b is shorter than A
        if b < A:
            # increase its length by 1
            b += 1
            # increase the magic point
            magic_points += 1
    # check if there is a bamboo of length B
    if B in bamboos:
        # remove it to get the bamboos that are shorter than B
        bamboos.remove(B)
    # for each bamboo of length b in bamboos that's shorter than B
    for b in bamboos:
        # if b is shorter than B - C
        if b < B - C:
            # decrease its length by 1
            b -= 1
            # increase the magic point
            magic_points += 1
        # if b is shorter than B
        if b < B:
            # increase its length by 1
            b += 1
            # increase the magic point
            magic_points += 1
    # check if there is a bamboo of length C
    if C in bamboos:
        # remove it to get the bamboos that are shorter than C
        bamboos.remove(C)
    # for each bamboo of length b in bamboos that's shorter than C
    for b in bamboos:
        # if b is shorter than C
        if b < C:
            # increase its length by 1
            b += 1
            # increase the magic point
            magic_points += 1
    # return the magic point
    return magic_points

def main():
    """
    :rtype: None
    """
    # read the inputs
    N, A, B, C = map(int, input().split())
    bamboos = list(map(int, [input() for i in range(N)]))
    # print the minimum amount of MP needed
    print(bamboo_magic(A, B, C, bamboos))

if __name__ == '__main__':
    main()
