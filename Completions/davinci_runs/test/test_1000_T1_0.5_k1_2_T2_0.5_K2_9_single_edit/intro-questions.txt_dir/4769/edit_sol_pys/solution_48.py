

import sys

def main():
    word = sys.stdin.readline().strip()
    length = len(word)
    if length % 2 == 0:
        for i in range(1, length//2 + 1):
            if word[:i] == word[i:2*i]:
                print(word[:i])
                return
    print(-1)

main()
