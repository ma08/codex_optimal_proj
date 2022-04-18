

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem B

if __name__ == '__main__':
    string = str(input())
    substring = ''
    result = 0

    for s in string:
        if s in ['A', 'C', 'G', 'T']:
            substring += s
            result = max(result, len(substring))
        else:
            substring = ''

    print(result)