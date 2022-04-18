

import sys
def main():
    n = int(input())
    a = [input() for i in range(n)]
    score = 0
    for i in range(n):
        if a[i] == 'A':
            score += 1
    print(score)

if __name__ == '__main__':
    main()
