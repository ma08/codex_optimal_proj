

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    S = list(sys.stdin.readline().rstrip())
    S.sort()
    print(''.join(S))
    return

if __name__ == "__main__":
    main()
