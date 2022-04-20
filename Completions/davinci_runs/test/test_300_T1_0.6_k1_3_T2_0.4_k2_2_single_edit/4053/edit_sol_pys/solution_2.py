
import sys

def main():
    n = int(sys.stdin.readline())
    strings = [sys.stdin.readline().strip() for i in range(2*n-2)]
    strings = [strings[i] + strings[i+1] for i in range(0, len(strings), 2)]
    print(strings)
    for s in strings:
        for i in range(n-1):
            if s[:i] not in strings:
                sys.stdout.write("P")
                break
        else:
            sys.stdout.write("S")

if __name__ == "__main__":
    main()
