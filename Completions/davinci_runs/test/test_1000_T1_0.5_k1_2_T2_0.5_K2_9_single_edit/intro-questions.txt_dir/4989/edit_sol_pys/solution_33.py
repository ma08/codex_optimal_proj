
def main():
    """
    Main function
    """
    number_of_pieces = int(input())
    pieces = [int(x) for x in input().split()]
    print(max_sum_recursive(pieces, 0, len(pieces) - 1))


def max_sum_recursive(pieces, left_index, right_index):
    """
    Recursively computes the maximum sum of integers that can be obtained by playing optimally
    """
    if left_index == right_index:
        return pieces[left_index]
    else:
        return max(pieces[left_index] + min(max_sum_recursive(pieces, left_index + 2, right_index), max_sum_recursive(pieces, left_index + 1, right_index - 1)), pieces[right_index] + min(max_sum_recursive(pieces, left_index + 1, right_index - 1), max_sum_recursive(pieces, left_index, right_index - 2)))

main()
