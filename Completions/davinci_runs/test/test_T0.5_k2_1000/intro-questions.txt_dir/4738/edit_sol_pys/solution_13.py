

def main():
    s = input()  # input string
    k = 1

    while k <= len(s):
        if len(s) % k == 0:
            i = k
            while i < len(s):
                if s[i] != s[i - k]:
                    break
                i += 1
            if i == len(s):
                break

        k += 1
    print(k)

if __name__ == "__main__":
    main()
