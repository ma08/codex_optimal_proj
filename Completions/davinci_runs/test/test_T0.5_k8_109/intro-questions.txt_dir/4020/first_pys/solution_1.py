

import sys

def main():
    inp = sys.stdin.read().splitlines()
    h1, m1 = inp[0].split(":")
    h2, m2 = inp[1].split(":")
    h1 = int(h1)
    m1 = int(m1)
    h2 = int(h2)
    m2 = int(m2)
    if m1 % 2 == 0:
        if m2 % 2 == 0:
            m3 = (m1+m2)//2
            if m3 == 60:
                h3 = (h1+h2+1)//2
                m3 = 0
            else:
                h3 = (h1+h2)//2
        else:
            m3 = (m1+m2+1)//2
            if m3 == 60:
                h3 = (h1+h2+1)//2
                m3 = 0
            else:
                h3 = (h1+h2)//2
    else:
        if m2 % 2 == 0:
            m3 = (m1+m2-1)//2
            if m3 == 60:
                h3 = (h1+h2+1)//2
                m3 = 0
            else:
                h3 = (h1+h2)//2
        else:
            m3 = (m1+m2)//2
            if m3 == 60:
                h3 = (h1+h2+1)//2
                m3 = 0
            else:
                h3 = (h1+h2)//2
    if h3 < 10:
        h3 = "0" + str(h3)
    else:
        h3 = str(h3)
    if m3 < 10:
        m3 = "0" + str(m3)
    else:
        m3 = str(m3)
    print(h3 + ":" + m3)

main()