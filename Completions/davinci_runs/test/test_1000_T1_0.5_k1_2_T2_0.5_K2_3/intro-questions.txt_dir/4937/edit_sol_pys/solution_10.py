

def main():
    s = input()
    t = input()
    for i in range(len(s)):
        if s[i] != t[-i-1]:
            print('No')
            return
    print('Yes')

main()
