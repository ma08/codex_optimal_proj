

import math

def get_nth_string(n, k): 

    if n == 3:
        if k == 1:
            return "abb"
        else:
            return "bab"

    # Calculate the number of strings with the first 'a' in the first position
    num_with_first_a_in_first_pos = (n-2) * (n-3) // 2

    if k <= num_with_first_a_in_first_pos:
        # The first 'a' is in the first position
        return "a" + get_nth_string(n-1, k)

    # The first 'a' is not in the first position
    return "b" + get_nth_string(n-1, k-num_with_first_a_in_first_pos)


if __name__ == "__main__":
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n, k = [int(x) for x in input().split()]
        print(get_nth_string(n, k))
