def main():
    for line in sys.stdin:
        words = line.split()
        if len(words) == len(set(words)):
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()
