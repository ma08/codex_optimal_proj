

def main():
    a, b, c = input().split(" ")
    if b == "West" and c == "East":
        print("Yes")
    elif b == "East" and c == "West":
        print("Yes")
    elif b == "North" and c == "South":
        print("Yes")
    elif b == "South" and c == "North":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
