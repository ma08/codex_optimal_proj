import numpy as np

def main():
    n, b, a = [int(x) for x in raw_input().split()]
    s = [int(x) for x in raw_input().split()]
    s = np.array(s)
    b_curr, a_curr = b, a
    i = 0
    while i < n:
        if s[i] == 1:
            if a_curr < a:
                a_curr += 1
            else:
                b_curr += 1
            i += 1
        elif s[i] == 0:
            if b_curr > 0:
                b_curr -= 1
                i += 1
            elif a_curr > 0:
                a_curr -= 1
                i += 1
            else:
                break
    print i

if __name__ == "__main__":
    main()
