
import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    files = set()
    for i in range(M):
        file = sys.stdin.readline().strip()
        files.add(file)
        if len(files) == N:
            print(file)
            break

if __name__ == '__main__':
    main()
