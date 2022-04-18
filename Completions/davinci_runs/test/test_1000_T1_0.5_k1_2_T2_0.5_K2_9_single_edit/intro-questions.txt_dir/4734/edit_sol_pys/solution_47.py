

def main():
    y, p = input().split()
    if y.endswith('ex'):
        print(y + p)
    elif y.endswith('e'):
        print(y[:-1] + 'x' + p)
    elif y.endswith(('a', 'i', 'o', 'u', 'A', 'I', 'O', 'U')):
        print(y[:-1] + 'ex' + p)
    else:
        print(y + 'ex' + p)

if __name__ == "__main__":
    main()
