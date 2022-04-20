


def main():
    n = int(input())
    a = [int(i) for i in input().split()]

    # create a list of tuples (value, index)
    a_indexed = [(a[i], i) for i in range(n)]

    # sort it by value
    a_indexed.sort()

    # create a list of tuples (value, index, is_left)
    # is_left is True if the element is on the left, False otherwise
    a_indexed_left = [(a_indexed[i][0], a_indexed[i][1], True) for i in range(n)]
    a_indexed_right = [(a_indexed[i][0], a_indexed[i][1], False) for i in range(n)]

    # sort it by the index
    a_indexed_left.sort(key=lambda x: x[1])
    a_indexed_right.sort(key=lambda x: x[1])

    # create a list of tuples (value, index, is_left, is_included)
    # is_included is True if the element is included in the result, False otherwise
    a_indexed_left_included = [(a_indexed_left[i][0], a_indexed_left[i][1], a_indexed_left[i][2], False) for i in range(n)]
    a_indexed_right_included = [(a_indexed_right[i][0], a_indexed_right[i][1], a_indexed_right[i][2], False) for i in range(n)]

    # include the first element (the leftmost one) in the result
    a_indexed_left_included[0] = (a_indexed_left_included[0][0], a_indexed_left_included[0][1], a_indexed_left_included[0][2], True)
    a_indexed_right_included[0] = (a_indexed_right_included[0][0], a_indexed_right_included[0][1], a_indexed_right_included[0][2], True)

    # iterate over all elements except the first one
    for i in range(1, n):
        # if the current element is on the left
        if a_indexed_left_included[i][2] == True:
            # if the previous element is included in the result
            if a_indexed_left_included[i - 1][3] == True:
                # if the current element is greater than the previous one, include it in the result
                if a_indexed_left_included[i][0] > a_indexed_left_included[i - 1][0]:
                    a_indexed_left_included[i] = (a_indexed_left_included[i][0], a_indexed_left_included[i][1], a_indexed_left_included[i][2], True)
        # if the current element is on the right
        else:
            # if the previous element is included in the result
            if a_indexed_right_included[i - 1][3] == True:
                # if the current element is greater than the previous one, include it in the result
                if a_indexed_right_included[i][0] > a_indexed_right_included[i - 1][0]:
                    a_indexed_right_included[i] = (a_indexed_right_included[i][0], a_indexed_right_included[i][1], a_indexed_right_included[i][2], True)

    # count the number of elements included in the result
    result_left = sum(i[3] for i in a_indexed_left_included)
    result_right = sum(i[3] for i in a_indexed_right_included)

    # if the result obtained by taking the leftmost element is greater than or equal to the result obtained by taking the rightmost element,
    # print the result obtained by taking the leftmost element
    if result_left >= result_right:
        print(result_left)
        for i in a_indexed_left_included:
            if i[3] == True:
                print('L', end='')
    # if the result obtained by taking the leftmost element is less than the result obtained by taking the rightmost element,
    # print the result obtained by taking the rightmost element
    else:
        print(result_right)
        for i in a_indexed_right_included:
            if i[3] == True:
                print('R', end='')


if __name__ == '__main__':
    main()