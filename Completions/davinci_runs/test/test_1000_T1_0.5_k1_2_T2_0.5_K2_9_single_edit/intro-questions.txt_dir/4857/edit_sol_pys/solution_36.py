

import sys

def main():
    l, w = map(int, sys.stdin.readline().strip().split())
    if l == 1:
        print(chr(w + 96))
    elif l == 2:
        if w > 26:
            print("impossible")
        else:
            print(chr(int(w/2) + 96) + chr(w - int(w/2) + 96))
    elif l == 3:
        if w > 26*2:
            print("impossible")
        else:
            print(chr(int(w/3) + 96) + chr(w - int(w/3) + 96) + chr(w - int(w/3) - int(w/3) + 96))
    else:
        if w > 26*l:
            print("impossible")
        else:
            print(chr(int(w/l) + 96) + chr(w - int(w/l) + 96) + chr(w - int(w/l) - int(w/l) + 96) + chr(w - int(w/l) - int(w/l) - int(w/l) + 96))

main()
