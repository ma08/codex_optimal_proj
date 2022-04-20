
import sys

def Solve(h1, h2, m1, m2):
    if h2 == h1:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 1:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 2:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 3:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 4:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 5:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 6:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 7:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 8:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 9:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 10:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 11:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 12:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 13:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 14:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)
    elif h2 == h1 + 15:
        if m2 - m1 == 30:
            return (h2, m2)
        elif m2 - m1 == 2:
            return (h2, m1 + 1)
        else:
            return (h1 + 1, m1 + (m2 - m1) / 2)


def main():
    lines = sys.stdin.readlines()
    h1, m1 = map(int, lines[0].split(':'))
    h2, m2 = map(int, lines[1].split(':'))
    h3, m3 = Solve(h1, h2, m1, m2)
    print("{0:02d}:{1:02d}".format(h3, m3))

if __name__ == "__main__":
    main()
