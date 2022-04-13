

def main():
    N = int(input())
    s = list(input())
    if len(s) >= 4:
        if s[0:4] == ['Y', 'A', 'K', 'I']:
            s[0:4] = ['y', 'a', 'k', 'i']
    ans = ''
    for i in range(len(s)):
        ans += s[i]
    if ans == 'yak1':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
