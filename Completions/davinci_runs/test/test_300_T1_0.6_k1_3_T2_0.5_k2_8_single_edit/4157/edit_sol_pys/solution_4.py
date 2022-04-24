

    # Input the value of n, the number of elements in the array
def main():

    # Input the array elements
    n = int(input())
    a = [int(x) for x in input().split()]

    # Sort the array in descending order.
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

    # Print the answer.
    print(' '.join(str(x) for x in answer))


if __name__ == '__main__':
    main()
