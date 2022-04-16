

def main():
    y, p = input().split()
    if y[-1] == 'e':
        print(y + 'x' + p)
    elif y[-1] in ['a', 'i', 'o', 'u']:
        print(y[:-1] + 'ex' + p)
    else:
        print(y + p)

if __name__ == "__main__":
    main()
