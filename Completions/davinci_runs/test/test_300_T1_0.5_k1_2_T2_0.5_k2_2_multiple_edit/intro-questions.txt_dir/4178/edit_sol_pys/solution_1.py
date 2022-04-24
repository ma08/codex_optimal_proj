# this is a test

def main():
    n = int(input())  # number of elements
    heights = list(
        map(int, input().split())
    )  # list of all elements

    for i in range(1, n):
        if heights[i - 1] > heights[i]:  # if previous element is greater than current element
            heights[i] += 1

    for i in range(1, n):
        if heights[i - 1] > heights[i]:  # if previous element is greater than current element
        # if the for loop does not break, then print Yes
            print('No')
            break  # break the for loop
    else:
        print('Yes')


if __name__ == '__main__':
    main()
