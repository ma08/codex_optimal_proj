

def main():
    s = input()
    print(s[:2] + "e"*(2*s.count("e")-1) + s[-2:], end="")

if __name__ == "__main__":
    main()
