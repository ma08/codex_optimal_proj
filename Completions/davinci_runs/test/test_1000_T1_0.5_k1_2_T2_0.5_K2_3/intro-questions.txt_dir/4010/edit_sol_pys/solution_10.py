


def get_input():
    return open("input.txt", "r")


def get_output():
    return open("output.txt", "w")


def get_number_of_test_cases(input):
    return int(input.readline())


def get_subsequence_length(test_case_number, input):
    return int(input.readline())


def get_subsequence(subsequence_length, input):
    return [int(x) for x in input.readline().split()]


def is_subsequence_palindrome(subsequence):
    return subsequence == subsequence[::-1]


def get_all_subsequences(subsequence):
    return [subsequence[i:j] for i in range(len(subsequence)) for j in range(i + 1, len(subsequence) + 1)]


def solve_test_case(test_case_number, subsequence_length, subsequence, output):
    for subsequence in get_all_subsequences(subsequence):
        if len(subsequence) >= 3 and is_subsequence_palindrome(subsequence):
            output.write("YES\n")
            return
    output.write("NO\n")


def solve_problem(input, output):
    number_of_test_cases = get_number_of_test_cases(input)
    for test_case_number in range(1, number_of_test_cases + 1):
        subsequence_length = get_subsequence_length(test_case_number, input)
        subsequence = get_subsequence(subsequence_length, input)
        solve_test_case(test_case_number, subsequence_length, subsequence, output)


solve_problem(get_input(), get_output())
