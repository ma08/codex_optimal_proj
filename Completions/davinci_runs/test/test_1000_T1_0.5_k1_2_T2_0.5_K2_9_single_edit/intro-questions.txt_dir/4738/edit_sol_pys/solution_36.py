

def main():
    s = input()
    k = 1

    while k <= len(s):
        if len(s) % k == 0:
            i = k
            while i < len(s):  # i = 1, 2, 3, 4, 5
                if s[i] != s[i-k]:  # s[1] != s[0]
                    break
                i += 1
            if i == len(s):  # i = 6
                break
        k += 1
    print(k)

if __name__ == "__main__":
    main()
