
import sys

def main():
    n, m = map(int, sys.stdin.readline().split()) # n = number of mappings, m = number of words to check
    lookup = {}
    for _ in range(n):
        a, b = sys.stdin.readline().split() # a = original letter, b = mapped letter
        lookup[a] = b
    for _ in range(m):
        a, b = sys.stdin.readline().split() # a = original word, b = mapped word
        if len(a) != len(b):
            print("no")
            continue
        for i in range(len(a)):
            if a[i] not in lookup or lookup[a[i]] != b[i]:
                print("no")
                break
        else:
            print("yes")

main()
