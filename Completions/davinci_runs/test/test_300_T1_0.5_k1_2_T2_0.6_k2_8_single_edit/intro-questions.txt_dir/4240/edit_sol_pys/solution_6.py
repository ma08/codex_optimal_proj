

def solve(s,t):
    if s == t:
        print("Yes")
    else:
        if len(s) == len(t):
            for i in range(len(s)):
                if s == t:
                    print("Yes")
                    break
                else:
                    s = s[-1] + s[:-1]
            else:
                print("No")
        else:
            print("No")

if __name__ == "__main__":
    s = input()
    t = input()
    solve(s,t)
