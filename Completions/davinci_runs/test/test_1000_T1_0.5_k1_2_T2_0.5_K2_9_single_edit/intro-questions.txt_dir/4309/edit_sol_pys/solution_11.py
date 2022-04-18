
import sys

def main():
    N = int(sys.stdin.readline().strip())
    for i in range(N, 1000, 111):
        if (i % 111) == 0:  # 111의 배수
            print(i)
            break

if __name__ == "__main__":
    main()
