

import math

def main():
    a, b = map(int, input().split())
    if a == b:
        print(a * math.ceil(a / 0.08))
    else:
        print(-1)

if __name__ == '__main__':
    main()