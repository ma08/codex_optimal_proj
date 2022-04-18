

def main():
    y, p = input().split()  # y = y, p = p
    if y[-1] == "e":  # if y ends with "e"
        print(y + "x" + p)  # print y + "x" + p
    elif y[-1] in "aiou":  # if y ends with "aiou"
        print(y[:-1] + "ex" + p)  # print y without last letter + "ex" + p
    elif y[-2:] == "ex":  # if y ends with "ex"
        print(y + p)  # print y + p

if __name__ == "__main__":
    main()
