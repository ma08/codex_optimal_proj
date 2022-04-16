

def main():
    a, b, c = input().split()
    if b == "West" and c == "East" \
            or b == "East" and c == "West" \
            or b == "North" and c == "South" \
            or b == "South" and c == "North":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
