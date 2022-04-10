

import sys

def main():
    n = int(input())
    s = input()
    print(solve(n, s))

def solve(n, s):
    """
    >>> solve(3, '121')
    '021'
    >>> solve(6, '000000')
    '001122'
    >>> solve(6, '211200')
    '211200'
    >>> solve(6, '120110')
    '120120'
    """
    d = {'0': 0, '1': 0, '2': 0}
    for i in s:
        d[i] += 1
    if d['0'] == d['1'] and d['1'] == d['2']:
        return s
    if d['0'] == d['1']:
        return s[:d['0']] + '2' * d['2']
    if d['0'] == d['2']:
        return s[:d['0']] + '1' * d['1']
    if d['1'] == d['2']:
        return '0' * d['0'] + s[-d['1']:]
    if d['0'] < d['1']:
        if d['0'] < d['2']:
            return '0' * (d['1'] - d['0']) + s[d['1'] - d['0']:]
        else:
            return s[:d['0']] + '2' * (d['1'] - d['2']) + s[-d['2']:]
    else:
        if d['1'] < d['2']:
            return s[:d['1']] + '0' * (d['0'] - d['1']) + s[-d['1']:]
        else:
            return s[:d['1']] + '0' * (d['0'] - d['2']) + '1' * (d['2'] - d['1']) + s[-d['1']:]

if __name__ == '__main__':
    main()