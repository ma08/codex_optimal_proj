
import sys

def main():
    num = sys.stdin.readline().strip().split('-')
    num = list(map(int, num))
    total = 0
    for n in range(len(num)):
        total += num[n]
    print(total)

main()
