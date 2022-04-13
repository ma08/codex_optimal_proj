
def main():
    s = input()
    l = 1
    while l <= len(s):
        if s[:l] * (len(s) // l) == s: # s[:l] = s[0:l]
            print(l)
            break
        l += 1

if __name__ == "__main__":
    main()
