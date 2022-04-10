
import numpy as np

def main():
    n, b, a = map(int, input().split())
    s = map(int, input().split())
    s = np.array(s)
    b_now, a_now = b, a
    i = 0
    while i < n:
        if s[i] == 1:
            if a_now < a:
                a_now += 1
            else:
                b_now += 1
            i += 1
        elif s[i] == 0:
            if b_now > 0:
                b_now -= 1
                i += 1
            elif a_now > 0:
                a_now -= 1
                i += 1
            else:
                break
    print(i)

if __name__ == "__main__":
    main()
