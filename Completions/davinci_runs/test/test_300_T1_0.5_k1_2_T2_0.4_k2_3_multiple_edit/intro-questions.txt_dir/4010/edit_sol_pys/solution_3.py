


def get_input():
    return open("input.txt", "r").read()


def get_output():
    return open("output.txt", "w")


def get_number_of_test_cases(input):
    return int(input.split("\n")[0])


def get_array_length(input, test_case_number):
    return int(input.split("\n")[test_case_number])


def get_array(input, test_case_number):
    return [int(x) for x in input.split("\n")[test_case_number].split()]


def is_array_palindrome(array):
    return array == array[::-1]


def get_all_subarrays(array):
    return [array[i:j] for i in range(len(array)) for j in range(i + 1, len(array) + 1)] # O(n^3)


def solve_test_case(test_case_number, array_length, array):
    for subarray in get_all_subarrays(array):
        if len(subarray) >= 3 and is_array_palindrome(subarray):
            return "YES"
    return "NO"


def solve_problem():
    input = get_input()
    number_of_test_cases = get_number_of_test_cases(input)
    for test_case_number in range(1, number_of_test_cases + 1):
        array_length = get_array_length(input, test_case_number)
        array = get_array(input, test_case_number)
        output = solve_test_case(test_case_number, array_length, array)
        print(output)


solve_problem()
