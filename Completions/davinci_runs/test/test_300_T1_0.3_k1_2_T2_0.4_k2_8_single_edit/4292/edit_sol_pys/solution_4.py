

def main():
    n = int(input())
    s = input()
    k = int(input())
    res = ''
    for c in s:
        if c.islower():
            res += chr((ord(c) - ord('a') + k) % 26 + ord('a'))
        elif c.isupper():
            res += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        else:
            res += c
    print(res)

if __name__ == '__main__':
    main()
