

def main():
    y, p = input().split()
    if y[-1] == "e":
        print(y + "x" + p)
    elif y[-1] in "aiou":
        print(y[:-1] + "ex" + p)
    elif y[-2:] == "ex" and p[0] not in "aeiou":
        print(y + p)
    else:
        print(y + p)

if __name__ == "__main__":
    main()
