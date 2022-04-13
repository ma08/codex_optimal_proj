

def main():
    x, y, z = map(int, input().split())
    
    if x == y:
        print(z)
    elif y == z:
        print(x)
    else:
        print(y)

if __name__ == '__main__':
    main()
