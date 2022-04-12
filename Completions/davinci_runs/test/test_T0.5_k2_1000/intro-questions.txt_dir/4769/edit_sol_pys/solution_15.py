
#
# Solution 

def is_multigram(word):
    for i in range(1, len(word)):
        if sorted(word[:i]) == sorted(word[i:]):
            return True
    return False

def get_multigram_root(word):
    for i in range(1, len(word)):
        if sorted(word[:i]) == sorted(word[i:]):
            return word[:i]
    return -1

if __name__ == '__main__':
    word = input()
    if is_multigram(word):
        print(get_multigram_root(word))
    else:
        print(-1)
