

def main():
    s = input()
    k = 1
    while k <= len(s):
        if s[:k] * (len(s) // k) == s: # this will check if the substring is repeated in the whole string
            print(k)
            break
        k += 1

if __name__ == "__main__":
    main()
