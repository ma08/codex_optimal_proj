
import sys

def main():
    x = int(sys.stdin.readline())
    shell = sys.stdin.readline().strip()
    if shell == 'out':
        if x % 2 == 0:
            print(x // 2)
        else:
            print((x + 1) // 2)
    elif shell == 'in':
        if x % 2 == 0:
            print(x - 1)
        else:
            print(x)
main()
