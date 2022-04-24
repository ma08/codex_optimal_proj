


def get_number_of_test_cases():
    return int(input())


def get_sequence_length():
    return int(input())


def get_sequence(sequence_length):
    return [int(x) for x in input().split()]


def is_sequence_palindrome(sequence):
    return sequence == sequence[::-1]


def get_all_subsequences(sequence):
    return [sequence[i:j] for i in range(len(sequence)) for j in range(i + 1, len(sequence) + 1)]


def solve_test_case(sequence_length, sequence):
    for subsequence in get_all_subsequences(sequence):
        if len(subsequence) >= 3 and is_sequence_palindrome(subsequence):
            return "YES"
    return "NO"


def solve_problem():
    number_of_test_cases = get_number_of_test_cases()
    for test_case_number in range(1, number_of_test_cases + 1):
        sequence_length = get_sequence_length()
        sequence = get_sequence(sequence_length)
        output = solve_test_case(sequence_length, sequence)
        print(output)


solve_problem()
