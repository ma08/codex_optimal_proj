

def main():
    s = input()
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            print(i+1, len(s)-i)
            break

if __name__ == "__main__":
    main()
