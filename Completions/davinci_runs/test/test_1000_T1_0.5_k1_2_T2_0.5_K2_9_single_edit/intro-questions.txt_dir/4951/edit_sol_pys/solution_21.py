


import sys

def main():
    lines = []
    for line in sys.stdin.readlines():
        lines.append(line.strip())

    lines = lines[1:]
    lines = [line.split() for line in lines]
    lines = [(line[:-1], line[-1]) for line in lines]
    lines = [(tuple(line[0]), line[1]) for line in lines]

    for i, line in enumerate(lines):
        if line[0] == ():
            continue
        for assumption in line[0]:
            if assumption not in [line[1] for line in lines[:i]]:
                print(i+1)
                return
    print("correct")

if __name__ == "__main__":
    main()
