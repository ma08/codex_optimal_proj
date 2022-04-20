

def main():
    h1, m1 = map(int, input().split(':'))
    h2, m2 = map(int, input().split(':'))
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2
    t = (t1 + t2) // 2
    h = t // 60
    m = t % 60
    print('{:02d}:{:02d}'.format(h, m))

if __name__ == '__main__':
    main()