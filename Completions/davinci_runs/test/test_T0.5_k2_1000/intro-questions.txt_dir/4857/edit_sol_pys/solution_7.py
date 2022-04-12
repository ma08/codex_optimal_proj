

import sys

def main():
    l, w = map(int, sys.stdin.readline().strip().split())
    if l == 1:
        print(chr(w + 96).upper())
    elif l == 2:
        if w > 26:
            print("impossible")
        else:
            print(chr(int(w/2) + 96).upper() + chr(w - int(w/2) + 96).upper())
    elif l == 3:
        if w > 26*2:
            print("impossible")
        else:
            print(chr(int(w/3) + 96).upper() + chr(w - int(w/3) + 96).upper() + chr(w - int(w/3) - int(w/3) + 96).upper())
    else:
        if w > 26*l:
            print("impossible")
        else:
            print(chr(int(w/l) + 96).upper() + chr(w - int(w/l) + 96).upper() + chr(w - int(w/l) - int(w/l) + 96).upper() + chr(w - int(w/l) - int(w/l) - int(w/l) + 96).upper())

main()
