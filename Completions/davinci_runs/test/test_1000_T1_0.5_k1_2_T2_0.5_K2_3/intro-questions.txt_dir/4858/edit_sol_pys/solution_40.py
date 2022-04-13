
def findLastWord(s):
    return ''.join(sorted(s, key=lambda x: (-ord(x), x)))
