

import sys

def main():
    line = sys.stdin.readline().strip()
    tokens = line.split('+')
    tokens = [int(t) if t.isdigit() else -int(t[1:]) for t in tokens]
    print(tokens)
    print(gen_bf(tokens))

def gen_bf(tokens):
    bf = ''
    for i, t in enumerate(tokens):
        if i == 0:
            bf += '+'*t
            bf += '>'
        else:
            bf += '+'*t
            bf += '>'
            bf += '['
            bf += '<'
            if t >= 0:
                bf += '+'
            else:
                bf += '-'
            bf += '>'
            bf += '-'
            bf += ']'
            bf += '<'
    bf += '.'
    return bf

if __name__ == '__main__':
    main()