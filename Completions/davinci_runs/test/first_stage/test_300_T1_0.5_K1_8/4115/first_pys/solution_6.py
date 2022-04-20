

def isPalindrome(s):
    return s == s[::-1]

def main():
    S = input()
    if isPalindrome(S):
        print(0)
    else:
        if S[0] == S[-1]:
            print(1)
        else:
            print(2)

if __name__ == '__main__':
    main()