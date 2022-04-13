

def main():
    n = input('Enter the number')
    if n[:3] == '555' and len(n) == 10:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
