

def main():
    record = input()
    alice, barbara = 0, 0
    for i in range(len(record)):
        if i % 2 == 0:
            if record[i] == "A":
                alice += int(record[i + 1])
            else:
                barbara += int(record[i + 1])
        else:
            pass
    while alice < 11 and barbara < 11:
        record = input()
        for i in range(len(record)):
            if i % 2 == 0:
                if record[i] == "A":
                    alice += int(record[i + 1])
                else:
                    barbara += int(record[i + 1])
            else:
                pass
    if alice == barbara:
        record = input()
        for i in range(len(record)):
            if i % 2 == 0:
                if record[i] == "A":
                    alice += int(record[i + 1])
                else:
                    barbara += int(record[i + 1])
            else:
                pass
        if alice > barbara:
            print("A")
        else:
            print("B")
    elif barbara == alice:
        record = input()
        for i in range(len(record)):
            if i % 2 == 0:
                if record[i] == "A":
                    alice += int(record[i + 1])
                else:
                    barbara += int(record[i + 1])
            else:
                pass
        if alice > barbara:
            print("A")
        else:
            print("B")
    elif alice - barbara >= 2:
        print("A")
    elif barbara - alice >= 2:
        print("B")

if __name__ == "__main__":
    main()
