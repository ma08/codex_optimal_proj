
def get_input():
    return open("input.txt", "r")


def get_output():
    return open("output.txt", "w")


def get_number_of_test_cases():
    return int(input())


def get_subsequence_length(test_case_number):
    return int(input())


def get_subsequence(subsequence_length):
    return [int(x) for x in input().split()]


def is_subsequence_palindrome(subsequence):
    return subsequence == subsequence[::-1]


def get_all_subsequences(subsequence):
    return [subsequence[i:j] for i in range(len(subsequence)) for j in range(i + 1, len(subsequence) + 1)]


def solve_test_case(test_case_number, subsequence_length, subsequence):
    for subsequence in get_all_subsequences(subsequence):
        if len(subsequence) >= 3 and is_subsequence_palindrome(subsequence):
            return "YES"
    return "NO"


def solve_problem():
    number_of_test_cases = get_number_of_test_cases()
    for test_case_number in range(1, number_of_test_cases + 1):
        subsequence_length = get_subsequence_length(test_case_number)
        subsequence = get_subsequence(subsequence_length)
        output = solve_test_case(test_case_number, subsequence_length, subsequence)
        print(output)


solve_problem()
