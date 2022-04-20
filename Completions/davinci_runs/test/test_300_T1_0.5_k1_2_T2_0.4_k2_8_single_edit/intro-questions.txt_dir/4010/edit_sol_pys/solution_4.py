
def get_input():
    return open("input.txt", "r").read()


def get_output():
    return open("output.txt", "w")


def get_number_of_test_cases(input):
    return int(input.pop(0))


def get_array_length(input):
    return int(input.pop(0))


def get_array(input, array_length):
    return [int(x) for x in input.pop(0).split()]


def is_array_palindrome(array):
    return array == array[::-1]


def get_all_subsequences(array):
    return [array[i:j] for i in range(len(array)) for j in range(i + 1, len(array) + 1)]


def solve_test_case(array):
    for subsequence in get_all_subsequences(array):
        if len(subsequence) >= 3 and is_array_palindrome(subsequence):
            return "YES"
    return "NO"


def solve_problem():
    input = get_input().split("\n")
    output = get_output()
    number_of_test_cases = get_number_of_test_cases(input)
    for test_case_number in range(1, number_of_test_cases + 1):
        array_length = get_array_length(input)
        array = get_array(input, array_length)
        output.write(solve_test_case(array))
        output.write("\n")


solve_problem()
