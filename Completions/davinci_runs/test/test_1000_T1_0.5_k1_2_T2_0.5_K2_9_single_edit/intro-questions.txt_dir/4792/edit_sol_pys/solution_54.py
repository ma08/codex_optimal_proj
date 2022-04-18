
import sys

def main():
    names = sys.stdin.readline().strip()
    compact = names[0]
    for i in range(1, len(names)):
        if names[i] != compact[-1]:
            compact += names[i]
    print(compact, end='')

main()
