
import sys

def main():
    P, N = [int(i) for i in input().split()]
    parts = {}
    i = 1
    for line in sys.stdin.readlines():
        line = line.strip()
        if line in parts:
            parts[line] = min(parts[line], i)
        else:
            parts[line] = i
        i += 1
    if len(parts) == P:
        print(max(parts.values()))
    else:
        print("paradox avoided")

main()
