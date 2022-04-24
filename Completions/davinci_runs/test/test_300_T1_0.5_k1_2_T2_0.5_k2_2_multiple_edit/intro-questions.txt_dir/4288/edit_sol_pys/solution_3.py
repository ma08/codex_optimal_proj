

def main():
    a, b, c = map(int, input().split())
    if a == b or b == c or a == c:
        print("YES")
    else:
        print("NO") 

if __name__ == '__main__':
    main()
