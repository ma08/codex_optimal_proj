
def get_input():
    return open("input.txt", "r")


def get_output():
    return open("output.txt", "w")


def get_number_of_test_cases():
    return int(input())


def get_array_length(test_case_number):
    return int(input())


def get_array(array_length):
    return [int(x) for x in input().split()]


def is_array_palindrome(array):
    return array == array[::-1]


def get_all_subarrays(array):
    return [array[i:j] for i in range(len(array)) for j in range(i + 1, len(array) + 1)]


def solve_test_case(test_case_number, array_length, array):
    for subarray in get_all_subarrays(array):
        if len(subarray) >= 3 and is_array_palindrome(subarray):
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
