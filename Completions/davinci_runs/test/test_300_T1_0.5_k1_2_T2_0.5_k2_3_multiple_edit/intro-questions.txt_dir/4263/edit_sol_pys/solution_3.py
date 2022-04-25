

def main():
    S = input()
    ans = 0

    for i in range(len(S)):
        for j in range(i, len(S)):
            if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
                ans += 1
            else:
                break

    print(ans)

if __name__ == '__main__':
    main()
