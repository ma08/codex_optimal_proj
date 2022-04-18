



def Main():
    n = int(input())
    for i in range(n):
        s = input()
        if len(s) == 1:
            print("NO")
        else:
            arr = list(s)
            arr.sort()
            for i in range(1, len(arr)):
                if arr[i] == arr[i-1]:
                    print("YES")
                    break
            else:
                print("NO")


if __name__ == "__main__":
    Main()
