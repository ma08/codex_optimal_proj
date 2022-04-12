import sys, string

def main():
    for line in sys.stdin:
        name = line.strip()
        compact = name[0]
        for i in range(1, len(name)):
            if name[i] != compact[-1]:
                compact += name[i]
        print(compact)

main()
