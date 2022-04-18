

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
    while alice < 11 or barbara < 11:
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
            break
        else:
            pass
    if alice == barbara and alice < 11 and barbara < 11:
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
        elif barbara - alice >= 2:
            print("B")
    else:
        pass

if __name__ == "__main__":
    main()
