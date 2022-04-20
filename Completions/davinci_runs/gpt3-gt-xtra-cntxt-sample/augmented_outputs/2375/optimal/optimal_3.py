def find_longest_palindrome(arr):
    """
    Function to find the longest palindrome in an array
    :param arr: array to find palindrome in
    :return: length of longest palindrome
    """
    n = len(arr)
    # create 2d array of size n*n
    table = [[0 for _ in range(n)] for _ in range(n)]

    # all strings of length 1 are palindromes
    max_length = 1
    for i in range(n):
        table[i][i] = True

    # check for strings of length 2
    start = 0
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            table[i][i + 1] = True
            start = i
            max_length = 2

    # check for strings greater than length 2
    for k in range(3, n + 1):
        for i in range(n - k + 1):
            j = i + k - 1
            if table[i + 1][j - 1] and arr[i] == arr[j]:
                table[i][j] = True
                if k > max_length:
                    start = i
                    max_length = k

    return max_length


if __name__ == "__main__":
    # take in number of test cases
    t = int(input())
    # iterate over test cases
    for _ in range(t):
        # take in array length
        n = int(input())
        # take in array
        arr = list(map(int, input().split()))
        # print the length of the longest palindrome
        print(find_longest_palindrome(arr))