import sys



def main():
    for line in sys.stdin:
        line = line.strip()
        if len(line) > 2 and len(set(line)) > 2:
            print(len(line) - 2)


if __name__ == '__main__':
    main()
