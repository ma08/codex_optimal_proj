

import sys

def find_substring_length(s, t):
    """
    Find the maximum possible length of the substring you can remove so that $t$ is still a subsequence of $s$.

    Parameters
    ----------
    s : str
        String $s$ consisting of at least $1$ and at most $2 \cdot 10^5$ lowercase Latin letters.
    t : str
        String $t$ consisting of at least $1$ and at most $2 \cdot 10^5$ lowercase Latin letters.

    Returns
    -------
    int
        The maximum possible length of the substring you can remove so that $t$ is still a subsequence of $s$.
    """

    # Initialize:
    #   length of the maximum possible length of the substring you can remove so that $t$ is still a subsequence of $s$
    max_substring_length = 0

    # Initialize:
    #   length of the current substring under consideration
    curr_substring_length = 0

    # Initialize:
    #   list of indices of the letter in $t$ corresponding to the last letter of the current substring under consideration
    last_letter_indices = [-1] * 26

    # Initialize:
    #   list of indices of the letter in $t$ corresponding to the last letter of the current substring under consideration
    #   (if the letter is not in $t$ then its index is -1)
    last_letter_indices_in_t = [-1] * 26

    for letter_index, letter in enumerate(s):
        # Update:
        #   length of the current substring under consideration
        curr_substring_length += 1

        # Update:
        #   list of indices of the letter in $t$ corresponding to the last letter of the current substring under consideration
        last_letter_indices[ord(letter) - ord('a')] = letter_index

    for letter_index, letter in enumerate(t):
        # Update:
        #   list of indices of the letter in $t$ corresponding to the last letter of the current substring under consideration
        #   (if the letter is not in $t$ then its index is -1)
        last_letter_indices_in_t[ord(letter) - ord('a')] = letter_index

    for letter_index in last_letter_indices_in_t:
        # If the letter is not in $t$ then its index is -1
        if letter_index == -1:
            continue

        # Update:
        #   length of the current substring under consideration
        curr_substring_length = max(curr_substring_length, letter_index - last_letter_indices[ord(t[letter_index]) - ord('a')])

    # Update:
    #   length of the maximum possible length of the substring you can remove so that $t$ is still a subsequence of $s$
    max_substring_length = max(max_substring_length, len(s) - curr_substring_length)

    return max_substring_length

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    print(find_substring_length(s, t))