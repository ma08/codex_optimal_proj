

def main():
    s = input()
    length = len(s)
    if length % 2 == 0:
        print(length - 1)
    else:
        print(length)

if __name__ == '__main__':
    main()