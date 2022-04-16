

def main(s):
    if len(s) == 2:
        return s
    else:
        a = s[:2]
        for i in range(2, len(s), 2):
            a += s[i]
        return a

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        print(main(s))
