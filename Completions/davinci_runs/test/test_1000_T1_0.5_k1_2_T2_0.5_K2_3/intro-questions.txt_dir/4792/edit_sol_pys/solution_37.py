
import sys

def main():
    filename = sys.stdin.readline().strip()
    compact = filename[0]
    for i in range(1, len(filename)):
        if filename[i] != compact[-1]:
            compact += filename[i]
    print(compact)

main()
