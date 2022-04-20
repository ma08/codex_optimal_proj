
def main():
    n, k = map(int, input().split())  # n is the number of elements in the list, k is the number of operations
    a = list(map(int, input().split()))  # a is the list of elements
    a.sort()  # sort the list
    # print(a)
    ans = 0
    for i in range(n):  # i is the index of the first element in the subarray
        for j in range(i, n):  # j is the index of the last element in the subarray
            if a[j] - a[i] <= 5:  # if the difference between the last and the first element is less than or equal to 5
                ans = max(ans, j - i + 1)  # update the answer
            else:
                break  # if the difference is greater than 5, break the loop

    print(ans)  # print the answer


if __name__ == '__main__':
    main()
