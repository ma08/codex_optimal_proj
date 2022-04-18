def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    word = input()
    if is_palindrome(word):
        print('Yes')
    else:
        print('No')
