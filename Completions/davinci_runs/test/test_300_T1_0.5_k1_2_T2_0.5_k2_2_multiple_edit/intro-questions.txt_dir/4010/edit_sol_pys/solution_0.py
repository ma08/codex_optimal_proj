


def get_input():
    return open("input.txt", "r")
def get_output():
    return open("output.txt", "w")


def get_number_of_test_cases():
    return int(get_input().readline())


def get_sequence_length(test_case_number):
    return int(get_input().readline())


def get_sequence(sequence_length):
    return [int(x) for x in get_input().readline().split()]


def is_sequence_palindrome(sequence):
    return sequence == sequence[::-1]


def get_all_subsequences(sequence):
    return [sequence[i:j] for i in range(len(sequence)) for j in range(i + 1, len(sequence) + 1)]


def solve_test_case(test_case_number, sequence_length, sequence):
    for subsequence in get_all_subsequences(sequence):
        if len(subsequence) >= 3 and is_sequence_palindrome(subsequence):
            return "YES"
    return "NO"


def solve_problem():
    number_of_test_cases = get_number_of_test_cases()
    for test_case_number in range(1, number_of_test_cases + 1):
        sequence_length = get_sequence_length(test_case_number)
        sequence = get_sequence(sequence_length)
        output = solve_test_case(test_case_number, sequence_length, sequence)
        get_output().write(output + "\n")


solve_problem()
