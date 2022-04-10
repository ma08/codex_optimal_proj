
import sys

def main():
    n, m, d = map(int, sys.stdin.readline().split())
    c = list(map(int, sys.stdin.readline().split()))
    river = [0] * n
    i = 0

    for platform_size in c:
        if i + platform_size + d > n:
            i = 0
        river[i:i + platform_size] = [i + 1] * platform_size
        i += platform_size

    if 0 in river:
        print('NO')
        return

    print('YES')
    print(' '.join(map(str, river)))

main()
