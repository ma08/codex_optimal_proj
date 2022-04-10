

n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print("1", "2")
else:
    # Find the index of the largest number in the list
    largest_ind = a.index(max(a))
    # Find the second largest number in the list
    second_largest_num = sorted(a)[-2]
    # Find the index of the second largest number in the list
    second_largest_ind = a.index(second_largest_num)
    # If the second largest number is at index 0, then the index of the largest number is 1
    if second_largest_ind == 0:
        print("1", second_largest_ind + 1)
    # If the second largest number is at the index of the largest number, print the next index
    elif second_largest_ind == largest_ind:
        print(second_largest_ind + 1, second_largest_ind + 2)
    # Otherwise, print the indexes of the largest number and the second largest number
    else:
        print(largest_ind + 1, second_largest_ind + 1)
