import sys

def main():
    n = int(sys.stdin.readline())
    languages = set()
    for i in range(n):
        line = sys.stdin.readline().rstrip().split()
        languages.update(line[2:])
    print(n - len(languages))

main()
