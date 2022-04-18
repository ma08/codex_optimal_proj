import string


def is_pangram(s):
    s = s.lower()  # convert to lower case
    for c in string.ascii_lowercase:
        if c not in s:
            return False
    return True


print(is_pangram(input()))
