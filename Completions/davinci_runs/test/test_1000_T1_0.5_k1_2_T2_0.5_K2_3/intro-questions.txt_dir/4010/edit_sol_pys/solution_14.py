


def get_input():
    return open("input.txt", "r")
def get_output():
    return open("output.txt", "w")


def get_number_of_test_cases(input):
    return int(input())


def get_array_length(input):
    return int(input())


def get_array(input):
    return [int(x) for x in input().split()]


def is_array_palindrome(array):
    return array == array[::-1]


def get_all_subsequences(array):
    return [array[i:j] for i in range(len(array)) for j in range(i + 1, len(array) + 1)]


def solve_test_case(array):
    for subsequence in get_all_subsequences(array):
        if len(subsequence) >= 3 and is_array_palindrome(subsequence):
            return "YES"
    return "NO"


def solve_problem(input, output):
    number_of_test_cases = get_number_of_test_cases(input)
    for test_case_number in range(1, number_of_test_cases + 1):
        array_length = get_array_length(input)
        array = get_array(input)
        output.write("Case #{}: {}\n".format(test_case_number, solve_test_case(array)))


solve_problem(get_input(), get_output())
