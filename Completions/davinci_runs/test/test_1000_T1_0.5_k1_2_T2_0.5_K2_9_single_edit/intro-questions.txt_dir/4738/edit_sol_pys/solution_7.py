

def main():
    s = input()
    for i in range(len(s)):
        if s[:i] * (len(s) // i) == s:
            print(i)
            exit()

if __name__ == "__main__":
    main()
