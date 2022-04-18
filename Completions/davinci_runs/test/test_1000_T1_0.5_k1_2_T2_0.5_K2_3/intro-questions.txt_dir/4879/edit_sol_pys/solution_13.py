

def main():
    a, b, c, d = input().split(" ")
    if b == "W" and c == "E" and a == "1":
        print("Yes")
    elif b == "E" and c == "W" and a == "1":
        print("Yes")
    elif b == "N" and c == "S" and a == "1":
        print("Yes")
    elif b == "S" and c == "N" and a == "1":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
