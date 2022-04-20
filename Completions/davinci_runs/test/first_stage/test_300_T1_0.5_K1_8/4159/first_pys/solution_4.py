

import sys

def main():
    lines = sys.stdin.readlines()
    cookies = lines[0].split()
    takahashi_cookies = int(cookies[0])
    aoki_cookies = int(cookies[1])
    k = int(cookies[2])

    for i in range(k):
        if takahashi_cookies > 0:
            takahashi_cookies -= 1
        elif aoki_cookies > 0:
            aoki_cookies -= 1

    print(takahashi_cookies, aoki_cookies)

if __name__ == "__main__":
    main()