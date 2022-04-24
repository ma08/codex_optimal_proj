

def bamboo_magic(A, B, C, bamboos):
    """
    :type A: int
    :type B: int
    :type C: int
    :type bamboos: list
    :rtype: int
    """
    # initialization
    bamboos.sort()
    bamboos.reverse()
    magic_points = 0
    # check if there is a bamboo of length A
    if A in bamboos:
        # remove it to get the bamboos that are shorter than A
        bamboos.remove(A)
    # for each bamboo of length b in bamboos that's shorter than A
    for i in range(len(bamboos)):
        # if b is shorter than A - B
        if bamboos[i] < A - B:
            # decrease its length by 1
            bamboos[i] -= 1
            # increase the magic point
            magic_points += 1
        # if b is shorter than A - C
        if bamboos[i] < A - C:
            # decrease its length by 1
            bamboos[i] -= 1
            # increase the magic point
            magic_points += 1
        # if b is shorter than A
        if bamboos[i] < A:
            # increase its length by 1
            bamboos[i] += 1
            # increase the magic point
            magic_points += 1
    # check if there is a bamboo of length B
    if B in bamboos:
        # remove it to get the bamboos that are shorter than B
        bamboos.remove(B)
    # for each bamboo of length b in bamboos that's shorter than B
    for i in range(len(bamboos)):
        # if b is shorter than B - C
        if bamboos[i] < B - C:
            # decrease its length by 1
            bamboos[i] -= 1
            # increase the magic point
            magic_points += 1
        # if b is shorter than B
        if bamboos[i] < B:
            # increase its length by 1
            bamboos[i] += 1
            # increase the magic point
            magic_points += 1
    # check if there is a bamboo of length C
    if C in bamboos:
        # remove it to get the bamboos that are shorter than C
        bamboos.remove(C)
    # for each bamboo of length b in bamboos that's shorter than C
    for i in range(len(bamboos)):
        # if b is shorter than C
        if bamboos[i] < C:
            # increase its length by 1
            bamboos[i] += 1
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
