
def main():
    s = input()
    if s[0] == "A":
        i = 2
        while s[i] != "C":
            i += 1
        if s[1].islower() and s[i-1].islower() and s[i+1:].islower():
            print("AC")
        else:
            print("WA")
    else:
        print("WA")

if __name__ == '__main__':
    main()
