

def main():
    n = int(input())
    s = input()
    open_brackets = 0
    close_brackets = 0
    for i in range(n):
        if s[i] == '(':
            open_brackets += 1
        else:
            close_brackets += 1
    if open_brackets == close_brackets:
        print(0)
    else:
        print(max(open_brackets, close_brackets))

if __name__ == "__main__":
    main()