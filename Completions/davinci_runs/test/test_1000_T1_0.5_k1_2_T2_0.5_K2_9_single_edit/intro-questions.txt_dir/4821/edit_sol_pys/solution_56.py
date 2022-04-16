

def main():
    s = input()
    d = dict()
    for i in range(len(s)):
        if s[i] in d:
            print("GRESKA")
            return
        d[s[i]] = True
    for i in range(5):
        if chr(ord("A")+i) not in d:
            print(13, end=" ")
        else:
            print(0, end=" ")

if __name__ == "__main__":
    main()
