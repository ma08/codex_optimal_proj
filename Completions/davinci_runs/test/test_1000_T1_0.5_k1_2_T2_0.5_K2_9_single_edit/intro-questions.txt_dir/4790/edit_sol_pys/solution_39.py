
def main():
    s = input()
    if s.count('B') == s.count('W'):
        print(1)
        return
    if s[0] == s[-1] and s.count(s[0]) == len(s) - 1:
        print(1)
        return
    print(0)

if __name__ == "__main__":
    main()
