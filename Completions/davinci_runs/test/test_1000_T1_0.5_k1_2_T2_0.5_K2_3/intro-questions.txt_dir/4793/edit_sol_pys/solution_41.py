
#
import sys

def main():
    s, v1, v2 = [int(x) for x in sys.stdin.readline().split()]

    if s % v2 != 0:
        print("Impossible")
        return
    v2_cnt = 0

    ans = s // v2
    v1_cnt = 0
    while ans > 0:
            v2_cnt += 1
        if ans % v1 != 0:
            v1_cnt += 1
            ans -= v2
        else:
            break

    print(ans // v1, v2_cnt)

if __name__ == '__main__':
    main()
