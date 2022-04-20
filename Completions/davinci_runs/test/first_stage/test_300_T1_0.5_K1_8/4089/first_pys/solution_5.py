

import math

def main():
    n = int(input())
    num = n - 1
    arr = []
    while True:
        if num < 26:
            arr.append(num)
            break
        else:
            arr.append(num % 26)
            num //= 26
    ans = ""
    for i in range(len(arr)):
        ans += chr(arr[i] + 97)
    print(ans[::-1])

if __name__ == '__main__':
    main()