

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p_order = 0
    q_order = 0
    for i in range(len(p)):
        p_order += p[i] - 1
        q_order += q[i] - 1
        for j in range(i+1, len(p)):
            if p[i] > p[j]:
                p_order += 1
            if q[i] > q[j]:
                q_order += 1
    print(abs(p_order - q_order))

if __name__ == '__main__':
    main()
