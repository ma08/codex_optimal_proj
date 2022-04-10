

def main():
    t = int(input())
    for _ in range(t):
        n,k = map(int, input().split())
        print(n//k + (1 if n%k != 0 else 0)) 

if __name__ == '__main__':
    main()
