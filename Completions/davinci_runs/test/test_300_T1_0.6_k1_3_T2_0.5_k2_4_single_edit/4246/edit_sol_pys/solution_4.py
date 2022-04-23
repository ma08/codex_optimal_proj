def main():
    s = input()  # input() -> str
    t = input()  # input() -> str
    result = 0
    for i in range(3):
        if s[i] == t[i]:
            result += 1
    print(result)  # print(int)

if __name__ == '__main__':
    main()
