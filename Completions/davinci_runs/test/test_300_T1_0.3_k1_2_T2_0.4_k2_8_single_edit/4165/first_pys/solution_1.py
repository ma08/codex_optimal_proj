

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if l[0] + l[1] > l[-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()