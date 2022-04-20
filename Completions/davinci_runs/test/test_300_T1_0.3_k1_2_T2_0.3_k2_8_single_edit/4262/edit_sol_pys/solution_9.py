
import sys

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p_index = p.index(1)
    q_index = q.index(1)
    print(abs(p_index - q_index) + 1)

if __name__ == '__main__':
    main()
