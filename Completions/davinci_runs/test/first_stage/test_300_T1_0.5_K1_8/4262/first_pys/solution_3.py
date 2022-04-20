

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p_index = 0
    q_index = 0
    for i in range(1, n+1):
        if p.index(i) > p_index:
            p_index = p.index(i)
        if q.index(i) > q_index:
            q_index = q.index(i)
    print(abs(p_index - q_index))

if __name__ == '__main__':
    main()