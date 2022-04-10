
def check_diverse(s):
    if len(s) == 1:
        return "Yes"
    else:
        s = sorted(s)
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) != 1:
                return "No"
        return "Yes"

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        print(check_diverse(s))