

import sys

def main():
    n = int(input())
    s = input()

    ans = []
    for i in range(n):
        if s[i] == 'E':
            ans.append('S')
        else:
            ans.append('E')
    print(''.join(ans))

if __name__ == "__main__":
    main()
