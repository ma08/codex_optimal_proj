

def main():
    a, b, c, d, e = input().split()
    if b == "West" and d == "East" or b == "East" and d == "West" or b == "North" and d == "South" or b == "South" and d == "North":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
