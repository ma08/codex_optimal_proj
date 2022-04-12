

import sys

def main():
    l, w = map(int, sys.stdin.readline().split())
    if w < l or w > l*26 or w == 0 or l == 0:
        print("impossible")
        return
    word = []
    for i in range(l):
        if w >= 26:
            word.append("z")
            w -= 26
        else:
            word.append(chr(w+96))
            w = 0
    print("".join(word))

if __name__ == "__main__":
    main()
