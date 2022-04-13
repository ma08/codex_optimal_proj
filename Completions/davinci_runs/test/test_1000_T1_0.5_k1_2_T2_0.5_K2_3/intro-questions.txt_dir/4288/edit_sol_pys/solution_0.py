

def main():
    a, b, c, x, y = map(int, input().split())
    print(min(a+b, 2*c)*min(x,y)+max(0, x-y)*min(a, 2*c)+max(0, y-x)*min(b, 2*c))

if __name__ == '__main__':
    main()
