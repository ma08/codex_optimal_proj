

def main():
    a, b, c, d = map(int, input().split()) 
    print(max(a * d, a * c, b * d, b * c)) 

if __name__ == '__main__':
    main()
