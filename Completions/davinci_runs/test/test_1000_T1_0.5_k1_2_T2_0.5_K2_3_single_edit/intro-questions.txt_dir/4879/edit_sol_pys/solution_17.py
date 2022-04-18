

def main():
    a, b = input().split()
    if a == "H":
        if b == "H":
            print("H")
        else:
            print("D")
    elif a == "D":
        if b == "H":
            print("D")
        else:
            print("H")

if __name__ == '__main__':
    main()
