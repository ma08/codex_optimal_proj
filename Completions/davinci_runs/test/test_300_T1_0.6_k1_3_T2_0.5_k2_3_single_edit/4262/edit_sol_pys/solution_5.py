
def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    p_order = [0 for _ in range(len(p))]
    q_order = [0 for _ in range(len(q))]
    for i in range(1, len(p)):
        j = i - 1
        while j >= 0 and p[j] > p[j+1]:
            p[j], p[j+1] = p[j+1], p[j]
            j -= 1
    for i in range(1, len(q)):
        j = i - 1
        while j >= 0 and q[j] > q[j+1]:
            q[j], q[j+1] = q[j+1], q[j]
            j -= 1
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            if p[i] < p[j]:
                p_order[i] += 1
    for i in range(len(q)):
        for j in range(i+1, len(q)):
            if q[i] < q[j]:
                q_order[i] += 1
    print(sum(p_order) - sum(q_order))

if __name__ == '__main__':
    main()
