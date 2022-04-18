
import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(sys.stdin.readline()) for i in range(n)]
    print(max(a))

main()
