

def main():
    s = input()
    print(s[:2] + s[2:].replace("e", "ee") + s[-1])

if __name__ == "__main__":
    main()
