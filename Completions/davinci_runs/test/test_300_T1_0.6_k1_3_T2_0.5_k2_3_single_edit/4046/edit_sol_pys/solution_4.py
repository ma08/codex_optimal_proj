
with open('input.txt', 'r') as fin:
    with open('output.txt', 'w') as fout:
        n = int(fin.readline())
        q = [int(x) for x in fin.readline().split()]
        if not all([-n < x < n for x in q]):
            fout.write('-1')
        else:
            p = [1]
            for i in range(1, n):
                p.append(p[-1] + q[i-1])
            if not all([1 <= x <= n for x in p]):
                fout.write('-1')
            else:
                fout.write(' '.join([str(x) for x in p]))
