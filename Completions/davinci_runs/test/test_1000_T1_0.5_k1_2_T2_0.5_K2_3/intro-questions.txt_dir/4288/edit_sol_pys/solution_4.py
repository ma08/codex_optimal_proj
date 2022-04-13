

def main():
    a, b, c = map(str, input().split())
    if a[-1] == b[0] and b[-1] == c[0]:
        print("Yes")
    else:
        
        print("No")

if __name__ == '__main__':
    main()
