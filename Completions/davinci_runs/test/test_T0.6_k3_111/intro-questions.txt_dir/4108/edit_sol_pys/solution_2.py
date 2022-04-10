
# raise if the length of S and T is different
def main():
    s, t = input().split()
    if len(s) != len(t):
        raise ValueError

    # create a dict for both S and T
    dic_s = {}
    dic_t = {}
    for i in range(len(s)):
        if s[i] in dic_s:
            dic_s[s[i]] += 1
        else:
            dic_s[s[i]] = 1

        if t[i] in dic_t:
            dic_t[t[i]] += 1
        else:
            dic_t[t[i]] = 1

    # check if they have different letter
    for key in dic_s:
        if key not in dic_t:
            print("No")
            return
        if dic_s[key] != dic_t[key]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()
