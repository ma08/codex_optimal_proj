

def main(filename):
    lines = 0
    for line in open(filename):
        lines += 1
    print(lines)

if __name__ == "__main__":
    main("file.py")
