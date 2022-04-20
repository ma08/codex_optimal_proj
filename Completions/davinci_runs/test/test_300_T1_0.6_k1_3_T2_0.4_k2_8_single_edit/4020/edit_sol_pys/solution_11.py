
import sys

def Solve(h1, h2, m1, m2):
    if m1 < 30 and m2 < 30:
        if h2 == h1:
            if m2 - m1 == 30:
                return (h2, m2)
            elif m2 - m1 == 2:
                return (h2, m1 + 1)
            else:
                return (h1, m1 + (m2 - m1) // 2)
        else:
            return (h1, m1 + (m2 - m1) // 2)
        if m1 >= 30:
            m1 -= 30
            h1 += 1
            if h1 == 24:
                h1 = 0
        if m2 >= 30:
            m2 -= 30
            h2 += 1
            if h2 == 24:
                h2 = 0
    else:
        if h2 == h1:
            if m2 - m1 == 30:
                return (h2, m2)
            elif m2 - m1 == 2:
                return (h2, m1 + 1)
            else:
                return (h1, m1 + (m2 - m1) // 2)
        else:
            return (h1 + 1, m1 + (m2 - m1) // 2)

def main():
    lines = sys.stdin.readlines()
    h1, m1 = map(int, lines[0].split(':'))
    h2, m2 = map(int, lines[1].split(':'))
    h3, m3 = Solve(h1, h2, m1, m2)
    print("{0:02d}:{1:02d}".format(h3, m3))

if __name__ == "__main__":
    main()
