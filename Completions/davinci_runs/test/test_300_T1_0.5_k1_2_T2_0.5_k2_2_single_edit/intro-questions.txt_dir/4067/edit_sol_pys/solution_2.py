
import sys

def main():
    N = int(input())
    s = input()
    assert N % 3 == 0

    count0 = s.count('0')
    count1 = s.count('1')
    count2 = s.count('2')

    if count0 == count1 == count2:
        print(s)
        sys.exit(0)

    n = N // 3
    if count0 == n and count1 == n:
        print(s.replace('2', '0', 1))
        sys.exit(0)
    if count0 == n and count2 == n:
        print(s.replace('1', '0', 1))
        sys.exit(0)
    if count1 == n and count2 == n:
        print(s.replace('0', '1', 1))
        sys.exit(0)

        sys.exit(0)

    if count0 == n:
        print(s.replace('1', '0', 1))
        sys.exit(0)
    if count1 == n:
        print(s.replace('2', '1', 1))
        sys.exit(0)
    if count2 == n:
        print(s.replace('0', '2', 1))
        sys.exit(0)

    if count0 > count1:
        print(s.replace('0', '2', 1))
        sys.exit(0)
    if count0 > count2:
        print(s.replace('0', '1', 1))
        sys.exit(0)
    if count1 > count0:
        print(s.replace('1', '0', 1))
        sys.exit(0)
    if count1 > count2:
        print(s.replace('1', '2', 1))
        sys.exit(0)
    if count2 > count0:
        print(s.replace('2', '0', 1))
        sys.exit(0)
    if count2 > count1:
        print(s.replace('2', '1', 1))
        sys.exit(0)

main()
