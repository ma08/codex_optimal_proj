

if __name__ == "__main__":
    S = input()
    K = int(input())

    s = []
    for i in range(len(S)):
        s.append(int(S[i]))
    t = []
    for i in range(len(s)):
        for j in range(1, s[i]+1):
            t.append(s[i])

    for i in range(10):
        r = []
        for j in range(len(t)):
            for k in range(t[j]):
                r.append(t[j])
        t = r

    print(t[K-1])
