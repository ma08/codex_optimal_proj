

def main():
    p, q, r = map(int, input().split())  # input
    print(min(p+q, p+r, q+r))

if __name__ == '__main__':
    main()
