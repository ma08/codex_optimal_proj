
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    count = 0
    for i in range(n):
        if a[i] % 2 == 0:
            while a[i] % 2 == 0:
                a[i] /= 2
                count += 1
    print(count)

main()

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    a.reverse()
    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]
    print(alice, bob)


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    a.reverse()
    alice = 0
    bob = 0
    for i in range(n):
        if i % 2 == 0:
            alice += a[i]
        else:
            bob += a[i]
    print(alice, bob)

main()
main()
