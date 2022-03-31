

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=len)
    for i in range(n):
        for j in range(i + 1, n):
            if s[j].find(s[i]) == -1:
                print("NO")
                return
    print("YES")
    for i in s:
        print(i)

if __name__ == "__main__":
    main()
