

import sys

def main():
    n = int(input())
    s = input()

    # the sorted string and the number of swaps needed to sort it
    sorted_str, num_swaps = sort_string(s)

    # the minimum number of colors needed to sort the string
    min_colors = len(set(sorted_str))

    # the coloring of the string
    coloring = get_coloring(sorted_str, min_colors)

    # print the results
    print(min_colors)
    print(' '.join(map(str, coloring)))


def sort_string(s):
    """
    Returns the sorted string and the number of swaps needed to sort it.
    """
    # the sorted string
    sorted_str = sorted(s)

    # the number of swaps needed to sort it
    num_swaps = 0

    # the number of swaps needed to sort the string
    # will be the sum of the distances of each letter to its sorted position
    for i in range(len(s)):
        num_swaps += abs(i - sorted_str.index(s[i]))

    return (sorted_str, num_swaps)


def get_coloring(sorted_str, min_colors):
    """
    Returns the coloring of the string.
    """
    # the coloring of the string
    coloring = [None] * len(sorted_str)

    # the color of the current letter
    curr_color = 1

    # the first letter of the current color
    first_letter = sorted_str[0]

    # the color of the first letter
    coloring[0] = curr_color

    # iterate through the sorted string
    for i in range(1, len(sorted_str)):
        # if the current letter is the same as the first letter of the current color
        if sorted_str[i] == first_letter:
            # increment the current color
            curr_color = (curr_color + 1) % min_colors
            # if the current color is 0, set it to the minimum color
            if curr_color == 0:
                curr_color = min_colors
            # set the first letter of the current color to the current letter
            first_letter = sorted_str[i]
        # set the color of the current letter to the current color
        coloring[i] = curr_color

    return coloring


if __name__ == "__main__":
    main()