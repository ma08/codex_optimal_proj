
import sys

def main():
    h1, m1 = map(int, sys.stdin.readline().strip().split(':'))
    h2, m2 = map(int, sys.stdin.readline().strip().split(':'))

    m1 += (h1 * 60)
    m2 += (h2 * 60)

    if m1 < m2:
        m3 = (m2 + m1) / 2
    else:
        m3 = (m1 + m2) / 2 + (12 * 60)
    
    h3 = m3 / 60
    m3 %= 60
    print('{0:02d}:{1:02d}'.format(h3, m3))

if __name__ == '__main__':
    main()
