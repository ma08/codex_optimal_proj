

def main():
    s = list(map(int, input().split()))
    s.sort()
    if s[0] == s[1] == s[2] == s[3]:
        print(s[0]**2)
    else:
        print(max(s[0]*s[1], s[2]*s[3]))

if __name__ == "__main__":
    main()