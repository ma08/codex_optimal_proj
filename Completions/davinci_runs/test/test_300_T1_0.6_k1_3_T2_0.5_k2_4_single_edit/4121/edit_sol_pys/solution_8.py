

def main():
    s = input()
    # print(s)
    cnt = 1
    for i in range(len(s)):
        if s[i] == '+':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            print(i + 2)
            return


if __name__ == "__main__":
    main()
