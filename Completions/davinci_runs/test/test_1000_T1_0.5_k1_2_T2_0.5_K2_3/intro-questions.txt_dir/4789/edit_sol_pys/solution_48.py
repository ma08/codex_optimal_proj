
import sys

def main():
    K = int(sys.stdin.readline().strip())
    desks = [int(x) for x in sys.stdin.readline().split()]
    count = 0
    for i in range(K):
        count += 1
        if desks[i] < i + 1:
            count += i + 1 - desks[i]
    print(count)

main()
