

def main():
    record = input().split()
    alice, barbara = 0, 0
    for i in range(len(record)//2):
        if record[i * 2] == "A":
            alice += int(record[i * 2 + 1])
        elif record[i * 2] == "B":
            barbara += int(record[i * 2 + 1])
        elif record[i * 2] == "C":
            alice += int(record[i * 2 + 1])
            barbara += int(record[i * 2 + 1])
    if alice == 11 and barbara < 11:
        print("A")
    elif barbara == 11 and alice < 11:
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
