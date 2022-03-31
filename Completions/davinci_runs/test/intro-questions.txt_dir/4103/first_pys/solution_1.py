

import numpy as np

def main():
    n, b, a = [int(x) for x in input().split()]
    s = [int(x) for x in input().split()]
    s = np.array(s)
    b_prev, a_prev = b, a
    i = 0
    while i < n:
        if s[i] == 1:
            if a_prev < a:
                a_prev += 1
            else:
                b_prev += 1
            i += 1
        elif s[i] == 0:
            if b_prev > 0:
                b_prev -= 1
                i += 1
            elif a_prev > 0:
                a_prev -= 1
                i += 1
            else:
                break
    print(i)

if __name__ == "__main__":
    main()