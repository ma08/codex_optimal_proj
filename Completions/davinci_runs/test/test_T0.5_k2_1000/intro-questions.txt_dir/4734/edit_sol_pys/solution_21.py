

def main():
    y, p = input().split()
    if y[-1] == "e":
        print(y + "x" + p)
    elif y[-1] in "aiouy":
        print(y[:-1] + "ex" + p)
    elif y[-2:] == "ex" and y[-3] not in "aiouy":
        print(y + p)

if __name__ == "__main__":
    main()
