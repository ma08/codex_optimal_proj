

import sys

def main():
    q = int(sys.stdin.readline().strip())
    for i in range(q):
        s = sys.stdin.readline().strip()
        m = int(sys.stdin.readline().strip())
        b = sys.stdin.readline().strip()
        b = b.split(" ")
        b = [int(x) for x in b]
        #print(s)
        #print(m)
        #print(b)
        ans = ""
        for j in range(len(s)):
            if j < len(b):
                for k in range(b[j]):
                    ans += "a"
            ans += s[j]
        print(ans)

if __name__ == "__main__":
    main()