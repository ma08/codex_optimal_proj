

def main():
    a, b, c, d = input().split()
    if b == "W" and c == "E" and d == "W":
        print("Yes")
    elif b == "E" and c == "W" and d == "E":
        print("Yes")
    elif b == "N" and c == "S" and d == "N":
        print("Yes")
    elif b == "S" and c == "N" and d == "S":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
