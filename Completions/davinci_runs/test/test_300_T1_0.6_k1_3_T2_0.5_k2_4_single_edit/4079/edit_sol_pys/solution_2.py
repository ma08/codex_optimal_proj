

def main():
    n = int(input())
    for i in range(n):
        string_ = input()
        string_ = list(string_)
        string_.sort()
        if len(string_) == 1:
            print("Yes")
        elif len(string_) > 1:
            for i in range(len(string_) - 1):
                if string_[i] == string_[i + 1]:
                    print("No")
                    break
                elif ord(string_[i]) + 1 == ord(string_[i + 1]):
                    if i == len(string_) - 2:
                        print("Yes")
                else:
                    print("No")
                    break


if __name__ == "__main__":
    main()
