
import sys


def main():
    l, w = map(int, sys.stdin.readline().split())
    if l < w or l > w * 26:
        print("impossible")
        return
    word = []
    for i in range(l):
        if l >= 26:
            word.append("z")
            l -= 26
        else:
            word.append(chr(l + 96))
            l = 0
    print("".join(word))


if __name__ == "__main__":
    main()
