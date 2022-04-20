

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for s in string:
        if s in ['A', 'C', 'G', 'T']:
            substring += s
            result = max(result, len(substring))
        else:
            substring = ''

    print(result)
