

def main():
    n = int(input())
    ll = list(map(int, input().split()))
    ll.sort()
    if ll[0] + ll[1] > ll[-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
