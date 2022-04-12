

def main():
    s = input()
    d = dict()
    for i in range(len(s)):
        if s[i] in d:
            print("ERROR")
            return
        d[s[i]] = True
    print(13-len(d), end=" ")
    print(0, end=" ")
    print(0, end=" ")
    print(0, end=" ")

if __name__ == "__main__":
    main()
