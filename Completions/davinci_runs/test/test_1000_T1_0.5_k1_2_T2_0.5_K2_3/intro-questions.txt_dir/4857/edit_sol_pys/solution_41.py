
import sys

def main():
    length, weight = map(int, sys.stdin.readline().strip().split())
    if length == 1:
        print(chr(weight + 96))
    elif length == 2:
        if weight > 26:
            print("impossible")
        else:
            print(chr(weight/2 + 96) + chr(weight - weight/2 + 96))
    elif length == 3:
        if weight > 26 * 2:
            print("impossible")
        else:
            print(chr(weight/3 + 96) + chr(weight - weight/3 + 96) + chr(weight - weight/3 - weight/3 + 96))
    else:
        if weight > 26 * length:
            print("impossible")
        else:
            print(chr(weight/length + 96) + chr(weight - weight/length + 96) + chr(weight - weight/length - weight/length + 96) + chr(weight - weight/length - weight/length - weight/length + 96))

main()
