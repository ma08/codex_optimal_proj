

def main():
    record = input()
    alice,barbara = 0,0
    for i in range(len(record)-1):
        if i%2 == 0:
            if record[i] == "A":
                alice += int(record[i+1])
            else:
                barbara += int(record[i+1])
        else:
            pass
    if alice == 11 and barbara < 11:
        return
        print("A")
    elif barbara == 11 and alice < 11:
        return
        print("B")
    elif alice == 11 and barbara == 11:
        if alice - barbara >= 2:
            print("A")
            return
        elif barbara - alice >= 2:
            print("B")
            return
    else:
        if alice > barbara:
            print("A")
        elif alice < barbara:
            print("B")

if __name__ == "__main__":
    main()
