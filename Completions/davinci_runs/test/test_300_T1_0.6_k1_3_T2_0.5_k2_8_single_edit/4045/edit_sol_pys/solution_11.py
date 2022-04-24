# comment

import sys

def main():
    n = int(input())
    s = input()
    t = input()
    if s == 'aa' or t == 'aa' or (s == 'bb' and t == 'bb'):
        print('NO')
        return
    if n == 1:
        if s == 'ab' or s == 'bc' or s == 'ca':
            print(s[0] + t[0] + s[1])
        else:
            print(t[0] + s[0] + t[1])
    elif n == 2: # comment
        if (s == 'ab' and t == 'bc') or (s == 'bc' and t == 'ab'):
            print('YES')
            print('c' * n + 'a' * n + 'b' * n)
        elif (s == 'ab' and t == 'ca') or (s == 'ca' and t == 'ab'):
            print('YES')
            print('b' * n + 'c' * n + 'a' * n)
        elif (s == 'bc' and t == 'ca') or (s == 'ca' and t == 'bc'):
            print('YES')
            print('a' * n + 'b' * n + 'c' * n)
        else:
            print('NO')
    elif n == 3:
        if (s == 'ab' and t == 'bc') or (s == 'bc' and t == 'ab'):
            print('YES')
            print('c' * n + 'a' * n + 'b' * n)
        elif (s == 'ab' and t == 'ca') or (s == 'ca' and t == 'ab'):
            print('YES')
            print('b' * n + 'c' * n + 'a' * n)
        elif (s == 'bc' and t == 'ca') or (s == 'ca' and t == 'bc'):
            print('YES')
            print('a' * n + 'b' * n + 'c' * n)
        else:
            print('NO')
    elif n == 4:
        if (s == 'ab' and t == 'bc') or (s == 'bc' and t == 'ab'):
            print('YES')
            print('c' * n + 'a' * n + 'b' * n)
        elif (s == 'ab' and t == 'ca') or (s == 'ca' and t == 'ab'):
            print('YES')
            print('b' * n + 'c' * n + 'a' * n)
        elif (s == 'bc' and t == 'ca') or (s == 'ca' and t == 'bc'):
            print('YES')
            print('a' * n + 'b' * n + 'c' * n)
        else:
            print('NO')
    elif n == 5:
        if (s == 'ab' and t == 'bc') or (s == 'bc' and t == 'ab'):
            print('YES')
            print('c' * n + 'a' * n + 'b' * n)
        elif (s == 'ab' and t == 'ca') or (s == 'ca' and t == 'ab'):
            print('YES')
            print('b' * n + 'c' * n + 'a' * n)
        elif (s == 'bc' and t == 'ca') or (s == 'ca' and t == 'bc'):
            print('YES')
            print('a' * n + 'b' * n + 'c' * n)
        else:
            print('NO')
    elif n == 6:
        if (s == 'ab' and t == 'bc') or (s == 'bc' and t == 'ab'):
            print('YES')
            print('c' * n + 'a' * n + 'b' * n)
        elif (s == 'ab' and t == 'ca') or (s == 'ca' and t == 'ab'):
            print('YES')
            print('b' * n + 'c' * n + 'a' * n)
        elif (s == 'bc' and t == 'ca') or (s == 'ca' and t == 'bc'):
            print('YES')
            print('a' * n + 'b' * n + 'c' * n)
        else:
            print('NO')
    elif n == 7:
        if (s == 'ab' and t == 'bc') or (s == 'bc' and t == 'ab'):
            print('YES')
            print('c' * n + 'a' * n + 'b' * n)
        elif (s == 'ab' and t == 'ca') or (s == 'ca' and t == 'ab'):
            print('YES')
            print('b' * n + 'c' * n + 'a' * n)
        elif (s == 'bc' and t == 'ca') or (s == 'ca' and t == 'bc'):
            print('YES')
            print('a' * n + 'b' * n + 'c' * n)
        else:
            print('NO')
    elif n == 8:
        if (s == 'ab' and t == 'bc') or (s == 'bc' and t == 'ab'):
            print('YES')
            print('c' * n + 'a' * n + 'b' * n)
        elif (s == 'ab' and t == 'ca') or (s == 'ca' and t == 'ab'):
            print('YES')
            print('b' * n + 'c' * n + 'a' * n)
        elif (s == 'bc' and t == 'ca') or (s == 'ca' and t == 'bc'):
            print('YES')
            print('a' * n + 'b' * n + 'c' * n)
        else:
            print('NO')
    elif n == 9:
        if (s == 'ab' and t == 'bc') or (s == 'bc' and t == 'ab'):
            print('YES')
            print('c' * n + 'a' * n + 'b' * n)
        elif (s == 'ab' and t == 'ca') or (s == 'ca' and t == 'ab'):
            print('YES')
            print('b' * n + 'c' * n + 'a' * n)
        elif (s == 'bc' and t == 'ca') or (s == 'ca' and t == 'bc'):
            print('YES')
            print('a' * n + 'b' * n + 'c' * n)
        else:
            print('NO')
    elif n == 10:
        if (s == 'ab' and t == 'bc') or (s == 'bc' and t == 'ab'):
            print('YES')
            print('c' * n + 'a' * n + 'b' * n)
        elif (s == 'ab' and t == 'ca') or (s == 'ca' and t == 'ab'):
            print('YES')
            print('b' * n + 'c' * n + 'a' * n)
        elif (s == 'bc' and t == 'ca') or (s == 'ca' and t == 'bc'):
            print('YES')
            print('a' * n + 'b' * n + 'c' * n)
        else:
            print('NO')
    else:
        print('NO')


if __name__ == '__main__':
    main()
