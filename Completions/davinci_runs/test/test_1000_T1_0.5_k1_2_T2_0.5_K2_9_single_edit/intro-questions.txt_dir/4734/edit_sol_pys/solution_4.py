

def main():
    x, y = input().split()
    if x[-1] == 'e':
        print(x + 'x' + y)
    elif x[-1] in 'aiou':
        print(x[:-1] + 'ex' + y)
    else:
        print(x + y)

if __name__ == "__main__":
    main()
