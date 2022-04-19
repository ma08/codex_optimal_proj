
def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    if l[0] + l[1] > l[-1] or l[0] + l[1] + l[2] > l[-1] + l[-2]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
