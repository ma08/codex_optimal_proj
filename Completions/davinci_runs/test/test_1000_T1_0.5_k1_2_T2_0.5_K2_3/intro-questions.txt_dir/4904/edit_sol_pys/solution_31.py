

def main():
    record = input()[1:-1]
    alice, barbara = 0, 0
    for i in range(0, len(record), 2):
        if record[i] == "A":
            alice += int(record[i + 1])
        elif record[i] == "B":
            barbara += int(record[i + 1])
    if alice > barbara:
            print("A")
    elif barbara > alice:
            print("B")


if __name__ == "__main__":
    main()
