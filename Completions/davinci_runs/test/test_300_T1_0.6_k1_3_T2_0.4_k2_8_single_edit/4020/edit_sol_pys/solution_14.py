
import sys

def Solve(h1, h2, m1, m2):
    if m1 < 30 and m2 > 30:
        if h2 == h1:
            if m2 - m1 == 30:
                return (h2, m2, True)
            elif m2 - m1 == 2:
                return (h2, m1 + 1, True)
            else:
                return (h1, m1 + (m2 - m1) / 2, True)
        elif h2 == h1 + 1:
            return (h1, m1 + (m2 - m1) / 2, True)
        else:
            return (h1, m1 + (m2 - m1) / 2, False)
    else:
        if h2 == h1:
            if m2 - m1 == 30:
                return (h2, m2, True)
            elif m2 - m1 == 2:
                return (h2, m1 + 1, True)
            else:
                return (h1, m1 + (m2 - m1) / 2, True)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2, False)

def main():
    lines = sys.stdin.readlines()
    h1, m1 = map(int, lines[0].split(':'))
    h2, m2 = map(int, lines[1].split(':'))
    h3, m3, is_same_day = Solve(h1, h2, m1, m2)
    if is_same_day:
        print("{0:02d}:{1:02d}".format(h3, m3))
    else:
        print("{0:02d}:{1:02d}+1".format(h3, m3))

if __name__ == "__main__":
    main()
