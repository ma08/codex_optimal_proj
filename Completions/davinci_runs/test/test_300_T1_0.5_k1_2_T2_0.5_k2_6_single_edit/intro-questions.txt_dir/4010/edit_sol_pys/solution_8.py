
def get_input_file():
    return open("input.txt")


def get_number_of_test_cases():
    return int(input())


def get_number_of_elements():
    return int(get_input_file().readline())


def get_elements():
    return [int(x) for x in get_input_file().readline().split()]


def is_palindrome(array):
    return str(array) == str(array)[::-1]


def get_all_subsequences_of_array(array):
    return [array[i:j] for i in range(len(array)) for j in range(i + 1, len(array) + 1)]



def solve_test_case(test_case_number, number_of_elements, elements):
    for subsequence in get_all_subsequences_of_array(elements):
        if len(subsequence) >= 3 and is_palindrome(subsequence):
            return "YES"
    return "NO"


def solve_problem():
    number_of_test_cases = get_number_of_test_cases()
    for test_case_number in range(1, number_of_test_cases + 1):
        number_of_elements = get_number_of_elements()
        elements = get_elements()
        output = solve_test_case(test_case_number, number_of_elements, elements)
        print(output)


solve_problem()
