

# SOLUTION
# The solution is to iterate through the array and check if the elements to the left and right of the current element are the same.
# If they are, check if the elements to the left and right of the current element are the same, and so on.
# This is done recursively, and so the function is called recursively.
# The maximum length of the array is 5000, so a maximum of 5000 recursive calls will be made.
# The maximum length of the array is 5000, so a maximum of 5000 recursive calls will be made.
# The time complexity is O(n^2).
# The space complexity is O(1).

def check_palindrome(arr, index, length):
    """
    Checks if the elements of arr from index to index + length - 1 are a palindrome.
    """
    if length == 1:
        return True
    if length == 2:
        return arr[index] == arr[index + length - 1]
    if arr[index] != arr[index + length - 1]:
        return False
    return check_palindrome(arr, index + 1, length - 2)


def check_subsequence(arr, index):
    """
    Checks if arr[index] is part of a palindromic subsequence of length at least 3.
    """
    # Check if the elements to the left of arr[index] are the same.
    i = index - 1
    while i >= 0 and arr[i] == arr[index]:
        i -= 1
    # Check if the elements to the right of arr[index] are the same.
    j = index + 1
    while j < len(arr) and arr[j] == arr[index]:
        j += 1
    # Check if arr[i:j] is a palindrome.
    return check_palindrome(arr, i + 1, j - i - 1)


def check_arr(arr):
    """
    Checks if arr has a palindromic subsequence of length at least 3.
    """
    for index in range(len(arr)):
        if check_subsequence(arr, index):
            return True
    return False


# Read input.
t = int(input())
results = []
for _ in range(t):
    input()
    arr = list(map(int, input().split()))
    results.append(check_arr(arr))

# Print output.
for result in results:
    print('YES' if result else 'NO')