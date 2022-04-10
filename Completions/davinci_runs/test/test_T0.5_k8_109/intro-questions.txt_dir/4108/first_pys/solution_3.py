

def main():
    s = input()
    t = input()

    if len(s) != len(t):
        print("No")
        exit()

    # create a dictionary of each letter in the string
    # and the number of times it occurs
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

    # compare the dictionaries
    if s_dict == t_dict:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()