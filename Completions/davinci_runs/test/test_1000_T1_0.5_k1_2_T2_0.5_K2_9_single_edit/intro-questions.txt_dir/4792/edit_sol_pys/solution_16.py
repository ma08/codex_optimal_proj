import sys

def main():
    name = sys.stdin.readline().strip()
    compact = name[0]
    for i in range(1, len(name)):
        if name[i] != compact[-1]:
            compact += name[i]
    print(compact)

if __name__ == '__main__':
    main()
