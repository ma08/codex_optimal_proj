
import fractions

def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    print(fractions.reduce(T))

if __name__ == '__main__':
    main()
