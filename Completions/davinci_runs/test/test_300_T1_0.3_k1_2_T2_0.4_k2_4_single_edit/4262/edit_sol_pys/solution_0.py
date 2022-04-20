import sys

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p_index = 0
    q_index = 0
    for i in range(n-1):
        if p[i] > p[i+1]:
            p_index = i
        if q[i] > q[i+1]:
            q_index = i
    print(abs(p_index - q_index))

if __name__ == '__main__':
    main()
