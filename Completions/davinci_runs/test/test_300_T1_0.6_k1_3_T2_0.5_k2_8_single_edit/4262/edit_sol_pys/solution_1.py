
def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p_order = 1
    q_order = 1
    for i in range(n):
        p_order *= (i+1)
        q_order *= (i+1)
        for j in range(n):
            if p[i] > p[j]:
                p_order //= (i+1)
            if q[i] > q[j]:
                q_order //= (i+1)
    print(abs(p_order-q_order)//2)

if __name__ == '__main__':
    main()
