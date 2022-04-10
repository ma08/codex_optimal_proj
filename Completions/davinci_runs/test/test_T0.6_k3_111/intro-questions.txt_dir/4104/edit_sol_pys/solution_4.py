
import sys

def main():
    num = sys.stdin.readline().strip() # strip() removes the newline character
    num = num.split('-')
    num = list(map(int, num))
    total = 0
    for n in range(len(num)):
        total += num[n]
    print(total)

main()
