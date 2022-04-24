
import math

def main():
    N, D = map(int, input().split())
    print(math.ceil(N/(2*D+1))) 

if __name__ == "__main__":
    main()
