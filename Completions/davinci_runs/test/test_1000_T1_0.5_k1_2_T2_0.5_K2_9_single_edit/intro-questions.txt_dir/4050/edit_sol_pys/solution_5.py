

def main():
    with open("input.txt", "r") as f:
        n = int(f.readline())
        a = [int(s) for s in f.readline().split()]

    with open("output.txt", "w") as f:
        f.write("%d\n" % len(a))
        f.write(" ".join(map(str, a)))

if __name__ == "__main__":
    main()
