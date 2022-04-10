

def main():
    n = int(input())
    s = input()
    result = "YES\n"
    for i in range(n):
        if s[i] < s[i-1]:
            result += "1"
        else:
            result += "0"
    print(result)

if __name__ == "__main__":
    main()