

import sys

def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(N):
        if i != 0:
            if S[i] == S[i-1]:
                count += 0
            else:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
