
def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            return False
    return True

if __name__ == "__main__":
    print(is_palindrome(input()))
