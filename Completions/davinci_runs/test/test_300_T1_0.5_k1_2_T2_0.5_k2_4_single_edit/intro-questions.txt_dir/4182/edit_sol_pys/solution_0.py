
import sys

def main():
    n, m, a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    for z in range(a + 1, b):
        if all(z > a_i for a_i in a_list) and all(z <= b_i for b_i in b_list):
            print("No War")
            sys.exit()

    print("War")

if __name__ == '__main__':
    main()
