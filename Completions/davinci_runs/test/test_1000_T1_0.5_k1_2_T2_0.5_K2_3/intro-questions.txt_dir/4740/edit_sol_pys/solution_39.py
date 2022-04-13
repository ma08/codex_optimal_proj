

def main():
    n = input()
    if n[:3] == '555' and len(n) == 10: # if the first 3 digits are 555 and the length of the number is 10
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
