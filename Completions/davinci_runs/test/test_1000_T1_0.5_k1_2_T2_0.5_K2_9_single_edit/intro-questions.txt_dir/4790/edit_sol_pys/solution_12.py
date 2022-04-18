

def main():
    s = input()
    N = len(s)
    if s.count('B') == s.count('W'): # BW, WB
        print(1)
        return
    if s[0] == s[-1]: # B, W
        if s.count(s[0]) == N - 1:
            print(1)
            return
    print(0)

if __name__ == "__main__":
    main()
