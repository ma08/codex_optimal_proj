

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
    if alice == 11 and barbara < 10:
        print("A")
    elif barbara == 11 and alice < 10:
        print("B")
    elif alice == 11 and barbara == 11:
        if alice - barbara >= 2:
            print("A")
        elif barbara - alice >= 2:
            print("B")
    else:
        pass

if __name__ == "__main__":
    main()
