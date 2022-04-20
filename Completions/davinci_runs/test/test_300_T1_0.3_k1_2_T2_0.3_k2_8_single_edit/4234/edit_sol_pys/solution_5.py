

def main():
    n = int(input())
    s = list(input())
    k = 0
    for i in range(0, n, 2):
        if i+1 < n and s[i] == s[i+1]:  # if two consecutive elements are same
            k += 1
    print(k)
    for i in range(0, n, 2):
        if i+1 < n and s[i] == s[i+1]:  # if two consecutive elements are same
            continue
        print(s[i], end="")
    print()

if __name__ == "__main__":
    main()
