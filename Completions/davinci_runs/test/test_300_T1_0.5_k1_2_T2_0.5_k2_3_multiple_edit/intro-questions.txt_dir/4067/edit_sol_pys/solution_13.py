
import sys

def main():
    N = int(input())
    s = input()
    assert(N % 3 == 0)

    cnt_0 = s.count('0')
    cnt_1 = s.count('1')
    cnt_2 = s.count('2')

    if cnt_0 == cnt_1 == cnt_2:
        print(s)
        sys.exit(0)

    n = N // 3
    if cnt_0 == n and cnt_1 == n:
        print(s.replace('2', '0', 1))
        sys.exit(0)
    if cnt_0 == n and cnt_2 == n:
        print(s.replace('1', '0', 1))
        sys.exit(0)
    if cnt_1 == n and cnt_2 == n:
        print(s.replace('0', '1', 1))
        sys.exit(0)

        sys.exit(0)

    if cnt_0 == n:
        print(s.replace('1', '0', 1))
        sys.exit(0)
    if cnt_1 == n:
        print(s.replace('2', '1', 1))
        sys.exit(0)
    if cnt_2 == n:
        print(s.replace('0', '2', 1))
        sys.exit(0)

    if cnt_0 > cnt_1:
        print(s.replace('0', '2', 1))
        sys.exit(0)
    if cnt_0 > cnt_2:
        print(s.replace('0', '1', 1))
        sys.exit(0)
    if cnt_1 > cnt_0:
        print(s.replace('1', '0', 1))
        sys.exit(0)
    if cnt_1 > cnt_2:
        print(s.replace('1', '2', 1))
        sys.exit(0)
    if cnt_2 > cnt_0:
        print(s.replace('2', '0', 1))
        sys.exit(0)
    if cnt_2 > cnt_1:
        print(s.replace('2', '1', 1))
        sys.exit(0)

main()
