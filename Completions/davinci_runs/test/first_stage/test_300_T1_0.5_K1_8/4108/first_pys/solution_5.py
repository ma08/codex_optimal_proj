

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print("No")
        return
    s_dict = {}
    t_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict:
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 1
        if t[i] in t_dict:
            t_dict[t[i]] += 1
        else:
            t_dict[t[i]] = 1
    for key in s_dict:
        if key not in t_dict:
            print("No")
            return
        if s_dict[key] != t_dict[key]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()