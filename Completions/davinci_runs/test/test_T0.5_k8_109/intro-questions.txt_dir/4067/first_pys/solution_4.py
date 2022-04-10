

def min_balanced_ternary_string(s):
    # count the number of 0's, 1's, and 2's
    count_0 = s.count('0')
    count_1 = s.count('1')
    count_2 = s.count('2')
    # if the counts are equal, the string is already balanced
    if count_0 == count_1 and count_1 == count_2:
        return s
    # if the counts are not equal, we need to replace the extra character with the missing character
    # the missing character is the one with the lowest count
    missing_char = min(count_0, count_1, count_2)
    # the extra character is the one with the highest count
    extra_char = max(count_0, count_1, count_2)
    # the index of the extra character is the index of the first occurrence of the extra character,
    # sorted by the index of the first occurrence of the missing character
    extra_index = sorted(range(len(s)), key=lambda i: s[i] == missing_char).pop()
    # replace the extra character with the missing character
    s = s[:extra_index] + missing_char + s[extra_index+1:]
    # the string is now balanced
    return s

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(min_balanced_ternary_string(s))