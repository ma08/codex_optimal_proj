

import sys

def main():
    line1 = sys.stdin.readline().strip().split()
    line2 = sys.stdin.readline().strip().split()
    h1 = int(line1[0][:2])
    m1 = int(line1[0][3:5])
    h2 = int(line2[0][:2])
    m2 = int(line2[0][3:5])

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
