

def main():
    s = input()
    print(1 if s.count('b') == s.count('w') or s[0] == s[-1] and s.count(s[0]) == len(s) - 1 else 0)

if __name__ == "__main__":
    main()
