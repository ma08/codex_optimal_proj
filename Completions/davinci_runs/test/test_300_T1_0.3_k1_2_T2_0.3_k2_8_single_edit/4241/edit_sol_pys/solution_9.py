
import sys

def main():
    s = sys.stdin.readline().rstrip()  # read the first line
    t = sys.stdin.readline().rstrip()  # read the second line

    print(min_changes(s, t))

def min_changes(s, t):
    """
    Returns the minimum number of characters in s that need to be changed
    to make t a substring of s.
    """
    # Create a list of indices of the characters in s that match the first character in t.
    indices = [i for i, c in enumerate(s) if c == t[0]]
    # If there are no characters in s that match the first character in t, then we need to change len(s) characters.
    if not indices:
        return len(s)
    # If there are characters in s that match the first character in t, then we need to check if t is a substring of s starting at each index in indices.
    else:
        for i in indices:
            # If t is a substring of s starting at index i, then we need to change i characters.
            if is_substring(s, t, i):
                return i
        # If t is not a substring of s starting at any index in indices, then we need to change len(s) - indices[-1] characters.
        return len(s) - indices[-1]


def is_substring(s, t, i):
    """
    Returns True if t is a substring of s starting at index i,
    otherwise returns False.
    """
    # If the length of s starting at index i is less than the length of t, then t cannot be a substring of s starting at index i.
    if len(s) - i < len(t):
        return False
    # If the length of s starting at index i is greater than or equal to the length of t, then check if the characters in s starting at index i match the characters in t.
    else:
        for j in range(len(t)):
            if s[i + j] != t[j]:
                return False
        return True


if __name__ == '__main__':
    main()
