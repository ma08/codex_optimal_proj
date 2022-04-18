
import sys

def main():
    l, w = map(int, sys.stdin.readline().strip().split())
    if l == 1:
        print(chr(w + 96))
    elif l == 2:
        if w > 26:
            print("impossible")
        else:
            print(chr(w//2 + 96) + chr(w - w//2 + 96))
    elif l == 3:
        if w > 26*2:
            print("impossible")
        else:
            print(chr(w//3 + 96) + chr(w - w//3 + 96) + chr(w - w//3 - w//3 + 96))
    else:
        if w > 26*l:
            print("impossible")
        else:
            print(chr(w//l + 96) + chr(w - w//l + 96) + chr(w - w//l - w//l + 96) + chr(w - w//l - w//l - w//l + 96))

main()
