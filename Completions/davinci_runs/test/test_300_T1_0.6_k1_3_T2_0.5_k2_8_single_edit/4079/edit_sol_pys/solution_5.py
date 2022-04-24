

def main():
    string = ""
    string_list = []
    n = int(input())
    for i in range(n):
        string = input().lower()
        string_list = list(string)
        string_list.sort()
        if len(string_list) == 1:
            print("Yes")
        elif len(string_list) > 1:
            for i in range(len(string_list) - 1):
                if string_list[i] == string_list[i + 1]:
                    print("No")
                    break
                    if i == len(string_list) - 2:
                        print("Yes")
                else:
                    print("No")
                    break


if __name__ == "__main__":
    main()
