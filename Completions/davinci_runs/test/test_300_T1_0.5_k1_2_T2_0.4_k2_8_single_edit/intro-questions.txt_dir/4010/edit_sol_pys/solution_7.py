
def get_input():
    return open("input.txt", "r").readlines()


def get_output():
    return open("output.txt", "w")


def get_number_of_test_cases(lines):
    return int(lines[0])


def get_array_length(lines, test_case_number):
    return int(lines[test_case_number])


def get_array(lines, test_case_number, array_length):
    return [int(x) for x in lines[test_case_number + 1].split()]


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
    lines = get_input()
    number_of_test_cases = get_number_of_test_cases(lines)
    for test_case_number in range(1, number_of_test_cases + 1):
        array_length = get_array_length(lines, test_case_number)
        array = get_array(lines, test_case_number, array_length)
        output = solve_test_case(test_case_number, array_length, array)
        print(output)


solve_problem()
