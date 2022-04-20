

import sys

def main():
    s = sys.stdin.readline().rstrip()
    if len(s) % 2 == 0:
        if s[0] == "L" or s[0] == "D":
            print("No")
            return
        for i in range(1, len(s), 2):
            if s[i] == "R":
                continue
            elif s[i] == "U" or s[i] == "D":
                if s[i-1] == "U" or s[i-1] == "D":
                    continue
                else:
                    print("No")
                    return
            else:
                print("No")
                return
        for i in range(2, len(s), 2):
            if s[i] == "L":
                continue
            elif s[i] == "U" or s[i] == "D":
                if s[i-1] == "U" or s[i-1] == "D":
                    continue
                else:
                    print("No")
                    return
            else:
                print("No")
                return
        print("Yes")
    else:
        if s[0] == "R":
            for i in range(1, len(s), 2):
                if s[i] == "R":
                    continue
                elif s[i] == "U" or s[i] == "D":
                    if s[i-1] == "U" or s[i-1] == "D":
                        continue
                    else:
                        print("No")
                        return
                else:
                    print("No")
                    return
            for i in range(2, len(s), 2):
                if s[i] == "L":
                    continue
                elif s[i] == "U" or s[i] == "D":
                    if s[i-1] == "U" or s[i-1] == "D":
                        continue
                    else:
                        print("No")
                        return
                else:
                    print("No")
                    return
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()