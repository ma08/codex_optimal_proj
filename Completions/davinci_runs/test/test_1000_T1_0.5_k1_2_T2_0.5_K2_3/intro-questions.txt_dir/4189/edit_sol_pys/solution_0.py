

def read_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
    main()
