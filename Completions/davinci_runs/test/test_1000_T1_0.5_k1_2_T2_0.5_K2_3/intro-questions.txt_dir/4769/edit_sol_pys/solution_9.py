
#include <cstdio>
import sys

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        word = sys.stdin.readline().strip()
        length = len(word)
        for i in range(1, length//2 + 1):
            if word[:i] == word[i:2*i]:
                print(word[:i])
                break
        else:
            print(-1)

main()
