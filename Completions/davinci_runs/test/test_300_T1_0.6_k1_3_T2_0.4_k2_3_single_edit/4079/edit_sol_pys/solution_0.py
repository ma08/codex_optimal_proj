

def main():
    n = int(input())
    for i in range(n):
        s = input()
        s = list(s)
        s.sort()
        if len(s) == 1:
            print("Yes")
        elif len(s) > 1:
            for i in range(len(s) - 1):
                if s[i] == s[i + 1]:
                    print("No")
                    break
                elif ord(s[i]) + 1 == ord(s[i + 1]):
                    if i == len(s) - 2:
                        print("Yes")
                else:
                    print("No")
                    break


if __name__ == "__main__":
    main()
