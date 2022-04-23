

def can_be_palindrome(string):
    """
    Checks if a string can be a palindrome.
    """
    import collections
    string_dict = collections.Counter(string)
    odds = 0
    for key, value in string_dict.items():
        if value % 2 != 0:
            odds += 1
            if odds > 1:
                return False
    return True

def get_palindrome(string):
    """
    Returns a palindrome from a string.
    """
    import collections
    string_dict = collections.Counter(string)
    palindrome = ""
    for key, value in string_dict.items():
        palindrome += key * (value / 2)
    for key, value in string_dict.items():
        if value % 2 != 0:
            palindrome += key
            break
    return palindrome + palindrome[::-1]

def get_minimum_palindrome(string):
    """
    Returns the minimum number of characters to change to make a string a palindrome.
    """
    palindrome = get_palindrome(string)
    if palindrome == string:
        return 0
    else:
        return 1

def main():
    """
    Main function.
    """
    string = raw_input()
    print get_minimum_palindrome(string)

if __name__ == "__main__":
    main()
