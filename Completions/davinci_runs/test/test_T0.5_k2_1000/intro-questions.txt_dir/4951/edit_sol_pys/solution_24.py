
import sys


def main():
    lines = []
    for line in sys.stdin.readlines():
        lines.append(line.strip())

    lines = [(tuple(line.split()[:-1]), line.split()[-1]) for line in lines[1:]]

    for i, line in enumerate(lines):
        if line[0] != ():
            for assumption in line[0]:
                if assumption not in [line[1] for line in lines[:i]]:
                    print(i+1)
                    return
    print("correct")

if __name__ == "__main__":
    main()
