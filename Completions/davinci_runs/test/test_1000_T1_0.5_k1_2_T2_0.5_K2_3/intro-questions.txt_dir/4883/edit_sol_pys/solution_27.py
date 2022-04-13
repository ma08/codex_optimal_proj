import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    lookup = {}
    for _ in range(n):
        a, b = sys.stdin.readline().split()  # a is the original word and b is the corrected word
        lookup[a] = b  # mapping the original word to the corrected word
    for _ in range(m):
        a, b = sys.stdin.readline().split()  # a is the word and b is the corrected word
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
