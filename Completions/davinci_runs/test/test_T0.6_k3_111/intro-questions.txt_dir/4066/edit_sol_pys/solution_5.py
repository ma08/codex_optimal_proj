

n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(1, 2)
else:
    # Find the index of the smallest number in the list
    smallest_ind = a.index(min(a))
    # Find the second smallest number in the list
    second_smallest_num = sorted(a)[1]
    # Find the index of the second smallest number in the list
    second_smallest_ind = a.index(second_smallest_num)
    # If the second smallest number is at index 0, then the index of the smallest number is 1
    if second_smallest_ind == 0:
        print(1, second_smallest_ind + 1)
    # If the second smallest number is at the index of the smallest number, print the next index
    elif second_smallest_ind == smallest_ind:
        print(second_smallest_ind + 1, second_smallest_ind + 2)
    # Otherwise, print the indices of the smallest number and the second smallest number
    else:
        print(smallest_ind + 1, second_smallest_ind + 1)
