

def main():
    a = int(input())
    b = str(a)
    if (int(b[0]) + int(b[1])) == (int(b[1]) + int(b[2])):
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()