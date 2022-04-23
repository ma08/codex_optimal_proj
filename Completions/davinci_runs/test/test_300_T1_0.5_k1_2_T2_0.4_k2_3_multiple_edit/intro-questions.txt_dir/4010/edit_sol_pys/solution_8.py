


def get_number_of_test_cases():
    return int(input()) # O(1)


def get_array_length(test_case_number):
    return int(input()) # O(1)


def get_array(array_length):
    return [int(x) for x in input().split()] # O(n)


def is_palindrome(string):
    return string == string[::-1] # O(n)


def get_all_substrings(string):
    return [string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)] # O(n^3)


def solve_test_case(test_case_number, array_length, array):
    for substring in get_all_substrings(array):
        if len(substring) >= 3 and is_palindrome(substring):
            return "YES"
    return "NO"


def solve_problem():
    number_of_test_cases = get_number_of_test_cases()
    for test_case_number in range(1, number_of_test_cases + 1):
        array_length = get_array_length(test_case_number)
        array = get_array(array_length)
        output = solve_test_case(test_case_number, array_length, array)
        print(output)


solve_problem()
