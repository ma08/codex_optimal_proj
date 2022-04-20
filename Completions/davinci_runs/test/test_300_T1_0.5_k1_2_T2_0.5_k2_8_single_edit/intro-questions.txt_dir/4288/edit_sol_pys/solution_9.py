

def main():
    s = input()
    res = ""
    for i in range(len(s)):
        if s[i] == "B":
            res = res[:-1]
        else:
            res += s[i]
    print(res)


if __name__ == '__main__':
    main()
