

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        print("YES") if len(set(a)) < 3 else print("NO")

if __name__ == '__main__':
    main()
