
import sys

def main():
    K = int(sys.stdin.readline().strip())
    desks = sorted([int(sys.stdin.readline().strip()) for _ in xrange(K)])
    count = 0
    for i in xrange(K):
        count += 1
        if desks[i] < i+1:
            count += i - desks[i]
    print(count)

main()
