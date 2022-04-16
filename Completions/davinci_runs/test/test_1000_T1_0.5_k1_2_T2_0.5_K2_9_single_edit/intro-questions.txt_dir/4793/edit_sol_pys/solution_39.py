

import sys

def main():
    s, v1, v2 = sys.stdin.readline().split()
    s, v1, v2 = int(s), int(v1), int(v2)

    if s % v2 != 0:
        print("Impossible")
        return

    ans = s // v2
    v1_cnt = 0
    while ans > 0:
        if ans % v1 != 0:
            v1_cnt += 1
            ans -= v2
        else:
            break

    print(ans // v1, v1_cnt)

if __name__ == '__main__':
    main()
