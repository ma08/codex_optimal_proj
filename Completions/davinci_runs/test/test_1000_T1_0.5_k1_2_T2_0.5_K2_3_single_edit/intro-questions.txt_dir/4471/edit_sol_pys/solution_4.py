

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if n == 1:
            if a[0] == 1:
                print("NO")
            else:
                print("YES")
            continue
        a.sort()
        if a[0] == 1:  # first element is 1
            if a[1] == 1:  # second element is 1
                print("NO")  # can't be
            else:  # second element is not 1
                if a[1] == 2:  # second element is 2
                    print("NO")  # can't be
                else:  # second element is 3
                    print("YES")  # can be
        else:  # first element is not 1
            if a[0] == 2:  # first element is 2
                if a[1] == 2:  # second element is 2
                    print("NO")  # can't be
                else:  # second element is 3
                    print("YES")  # can be
            else:  # first element is 3
                if a[1] == 3:  # second element is 3
                    print("NO")  # can't be
                else:  # second element is 4
                    print("YES")  # can be

if __name__ == "__main__":
    main()
