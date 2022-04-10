

def main():
    q = int(input())
    for i in range(q):
        s = input()
        m = int(input())
        b = list(map(int,input().split()))
        #print(s,m,b)
        t = ""
        for i in range(m):
            if b[i] == 0:
                t += s[i]
            elif b[i] == 1:
                if s[i] == 'z':
                    t += 'a'
                else:
                    t += chr(ord(s[i])+1)
            else:
                t += 'b'
        print(t)

if __name__ == "__main__":
    main()