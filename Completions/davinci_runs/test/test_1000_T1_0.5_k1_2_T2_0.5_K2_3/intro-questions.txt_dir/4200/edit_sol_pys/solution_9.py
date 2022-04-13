

def main():
    N = int(input())
    s = list(input())
    if len(s) >= 3:
        if s[0:3] == ['Y', 'A', 'K']:
            s[0:3] = ['y', 'a', 'k']
    ans = ''
    for i in range(len(s)):
        ans += s[i]
    if ans == 'yaki':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
