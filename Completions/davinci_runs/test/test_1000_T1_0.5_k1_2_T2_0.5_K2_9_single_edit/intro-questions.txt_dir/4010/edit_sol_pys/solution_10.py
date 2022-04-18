
def get_input():
    return open("input.txt", "r").read().splitlines()


def write_output(output):
    open("output.txt", "w").write(output)


def get_number_of_test_cases(input_lines, current_line_number):
    return int(input_lines[current_line_number])


def get_array_length(input_lines, current_line_number):
    return int(input_lines[current_line_number])


def get_array(input_lines, current_line_number, array_length):
    return [int(x) for x in input_lines[current_line_number].split()]


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
    input_lines = get_input()
    current_line_number = 0
    number_of_test_cases = get_number_of_test_cases(input_lines, current_line_number)
    current_line_number += 1
    output = ""
    for test_case_number in range(1, number_of_test_cases + 1):
        array_length = get_array_length(input_lines, current_line_number)
        current_line_number += 1
        array = get_array(input_lines, current_line_number, array_length)
        current_line_number += 1
        output = solve_test_case(test_case_number, array_length, array)
        output += output + "\n"
    write_output(output)


solve_problem()
