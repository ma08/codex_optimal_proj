

def main():
    X, Y = input().split()
    if X[-1] == "e":
        print(X + 'x' + Y)
    elif X[-1] in "aiou":
        print(X[:-1] + 'ex' + Y)
    elif X[-2:] == "ex":
        print(X + Y)
    else:
        print(X + "ex" + Y)

main()
