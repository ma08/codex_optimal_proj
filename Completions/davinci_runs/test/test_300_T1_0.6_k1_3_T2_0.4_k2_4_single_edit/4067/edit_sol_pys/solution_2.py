
def main():
    n = int(input())
    s = input()
    d = {'0':0, '1':0, '2':0}
    for c in s:
        d[c] += 1
    if d['1'] < d['2']:
        d['1'] += 1
        d['2'] -= 1
    elif d['1'] > d['2']:
        d['1'] -= 1
        d['2'] += 1
    print('0' * d['0'] + '1' * d['1'] + '2' * d['2'])

if __name__ == '__main__':
    main()
