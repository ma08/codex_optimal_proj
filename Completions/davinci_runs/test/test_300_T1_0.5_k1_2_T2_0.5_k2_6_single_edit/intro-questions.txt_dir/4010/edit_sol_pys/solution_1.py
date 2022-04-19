


def get_input(filename):
    return open(filename, "r")


def get_output(filename):
    return open(filename, "w")


def get_number_of_test_cases(input_file):
    return int(input_file.readline())


def get_array_length(input_file):
    return int(input_file.readline())


def get_array(input_file, array_length):
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


def solve_problem(input_file, output_file):
    number_of_test_cases = get_number_of_test_cases(input_file)
    for test_case_number in range(1, number_of_test_cases + 1):
        array_length = get_array_length(input_file)
        array = get_array(input_file, array_length)
        output = solve_test_case(test_case_number, array_length, array)
        output_file.write(output + "\n")


solve_problem(get_input("input.txt"), get_output("output.txt"))
