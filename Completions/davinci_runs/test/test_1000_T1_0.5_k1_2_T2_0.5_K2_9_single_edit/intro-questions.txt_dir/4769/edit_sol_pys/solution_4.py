

def is_multigram(word):
    """
    Returns boolean value whether word is multigram or not
    """
    for i in range(1, len(word)):
        if sorted(word[:i]) == sorted(word[i:]):
            return True
    return False

    """
    Returns the root word of a multigram
    """
def get_multigram_root(word):
    for i in range(1, len(word)):
        if sorted(word[:i]) == sorted(word[i:]):
            return word[:i]
    return -1

    """
    Driver function
    """
if __name__ == '__main__':
    word = input()
    if is_multigram(word):
        print(get_multigram_root(word))
    else:
        print(-1)
