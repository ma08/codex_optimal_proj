

import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        k, l, s = [int(n) for n in sys.stdin.readline().split()]
        keyboard = sys.stdin.readline().strip()
        target = sys.stdin.readline().strip()
        if l > s:
            print("Case #%d: %s" % (i + 1, 0.0))
        else:
            max_ = 0
            for i in range(s - l + 1):
                if target in keyboard[i:i + l]:
                    max_ += 1
            print("Case #%d: %s" % (i + 1, max_))

main()
