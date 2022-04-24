


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = list(s1)
    s2 = list(s2)
    s1.sort()
    s2.sort()
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def is_anagram2(s1, s2):
    if len(s1) != len(s2):
        return False
    s1 = list(s1)
    s2 = list(s2)
    for i in range(len(s1)):
        if s1[i] not in s2:
            return False
        else:
            s2.remove(s1[i])
    return True


print(is_anagram('abc', 'bca'))
print(is_anagram2('abc', 'bca'))
