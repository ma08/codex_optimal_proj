

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    l.sort(key=len)
    for i in range(n):
        for j in range(i+1,n):
            if l[j].find(l[i]) == -1:
                print("NO")
                return
    print("YES")
    for i in l:
        print(i)

if __name__ == "__main__":
    main()