

# %%

#%%

import math


def main():
    n = int(input())
    ans = 0
    while n > 0:
        if n % 6 == 0:
            n = n // 6
            ans += 1
        elif n % 9 == 0:
            n = n // 9
            ans += 1
        else:
            n = n - 1
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
