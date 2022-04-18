

def main():
    s = input()
    if len(s) == 1:
        print(s)
        return
    s = s[1:-1]
    s = s.split('|')
    l = []
    for i in s:
        l.extend(i.split('&'))
    l = list(set(l))
    l.sort()
    print('(' + '&'.join(l) + ')')

if __name__ == '__main__':
    main()
