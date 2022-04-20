


def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    # The only way to get a number greater than
    # its predecessor is to multiply it by 2.

    # So we can determine the order of the array
    # by multiplying the previous number by 2.
    # If we get an array that is greater than the

    # current number, we divide the current number
    # by 3 and add it to the array.


    # Sort the array in descending order
    a.sort(reverse=True)


    answer = []

    for i in a:
        if len(answer) == 0 or i <= answer[-1]:
            answer.append(i)

        elif i > answer[-1] * 2:
            answer.append(i)
        else:

            while i < answer[-1] * 2:
                i = i * 3
            answer.append(i)

    # Print the answer
    print(' '.join(str(x) for x in answer))


if __name__ == '__main__':
    main()
