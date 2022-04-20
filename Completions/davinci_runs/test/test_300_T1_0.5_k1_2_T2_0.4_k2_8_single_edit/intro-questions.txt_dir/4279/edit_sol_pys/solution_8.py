

def main():
    n = int(input())
    for i in range(n):
        s = input()
        print(find(s))

def find(s):
    if len(s) % 2 == 0:
        return -1
    if len(s) == 1:
        return 0
    if len(s) == 3:
        if s == 'aba':
            return 0
        else:
            return -1

    for i in range(len(s)):
        if i == 0:
            continue
        if i % 2 == 0:
            if s[:i] == s[i:i*2]:
                return i
    return -1

if __name__ == '__main__':
    main()
