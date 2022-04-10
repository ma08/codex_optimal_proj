

import sys

def main():
    S = sys.stdin.readline().rstrip()
    T = sys.stdin.readline().rstrip()

    if len(S) != len(T):
        print("No")
        return

    s_dict = {}
    t_dict = {}

    for i in range(len(S)):
        if S[i] in s_dict:
            s_dict[S[i]] += 1
        else:
            s_dict[S[i]] = 1

        if T[i] in t_dict:
            t_dict[T[i]] += 1
        else:
            t_dict[T[i]] = 1

    for k in s_dict.keys():
        if k not in t_dict or s_dict[k] != t_dict[k]:
            print("No")
            return

    print("Yes")

if __name__ == "__main__":
    main()