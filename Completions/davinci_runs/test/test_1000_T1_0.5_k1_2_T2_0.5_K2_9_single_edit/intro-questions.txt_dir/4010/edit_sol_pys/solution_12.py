
def get_input():
    return open("input.txt", "r")


def get_output():
    return open("output.txt", "w")


def get_number_of_test_cases(input_file):
    return int(input_file.readline())


def get_array_length(test_case_number, input_file):
    return int(input_file.readline())


def get_array(array_length, input_file):
    return [int(x) for x in input_file.readline().split()]


def is_array_palindrome(array):
    return array == array[::-1]


def get_all_subsequences(array):
    return [array[i:j] for i in range(len(array)) for j in range(i + 1, len(array) + 1)]


def solve_test_case(test_case_number, array_length, array):
    for subsequence in get_all_subsequences(array):
        if len(subsequence) >= 3 and is_array_palindrome(subsequence):
            return "YES"
    return "NO"


def solve_problem():
    input_file = get_input()
    output_file = get_output()
    number_of_test_cases = get_number_of_test_cases(input_file)
    for test_case_number in range(1, number_of_test_cases + 1):
        array_length = get_array_length(test_case_number, input_file)
        array = get_array(array_length, input_file)
        output = solve_test_case(test_case_number, array_length, array)
        output_file.write(output)


solve_problem()
