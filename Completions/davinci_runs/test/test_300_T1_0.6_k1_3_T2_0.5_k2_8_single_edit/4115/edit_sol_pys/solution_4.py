

def can_be_palindrome(word):
    """
    Checks if a word can be a palindrome.
    """
    import collections
    word_dict = collections.Counter(word)
    odds = 0
    for key in word_dict:
        if word_dict[key] % 2 != 0:
            odds += 1
            if odds > 1:
                return False
    return True

def get_palindrome(word):
    """
    Returns a palindrome from a word.
    """
    import collections
    word_dict = collections.Counter(word)
    palindrome = ''
    for key in word_dict:
        palindrome += key * (word_dict[key] / 2)
    for key in word_dict:
        if word_dict[key] % 2 != 0:
            palindrome += key
            break
    return palindrome + palindrome[::-1]

def get_minimum_palindrome(word):
    """
    Returns the minimum number of characters to change to make a word a palindrome.
    """
    palindrome = get_palindrome(word)
    if palindrome == word:
        return 0
    else:
        return 1

def main():
    """
    Main function.
    """
    word = raw_input()
    print get_minimum_palindrome(word)

if __name__ == "__main__":
    main()
