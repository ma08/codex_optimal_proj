
import sys
def main():
    n = int(sys.stdin.readline())
    if n == 1:
        print(0)
        return
    elif n == 2:
        print(0)
        return
    else:
        arr = list(map(int,sys.stdin.readline().split()))
        arr.sort()
        if arr[0] == arr[1] and arr[1] == arr[2]:
            print(0)
            return
        elif arr[0] == arr[1]:
            print(1)
            return
        elif arr[1] == arr[2]:
            print(1)
            return
        else:
            print(2)
            return

if __name__ == '__main__':
    main()
