

import sys

def main():
    N = int(sys.stdin.readline())
    edges = []
    for i in range(N-1):
        a, b = map(lambda x: int(x), sys.stdin.readline().split())
        edges.append((a, b))
        edges.append((b, a))
    #print(edges)
    max_path = 0
    node_list = list(range(1, N+1))
    for i in range(len(node_list)):
        for j in range(i+1, len(node_list)):
            for k in range(j+1, len(node_list)):
                a, b, c = node_list[i], node_list[j], node_list[k]
                #print(a, b, c)
                ab = [a, b]
                ac = [a, c]
                bc = [b, c]
                for e in edges:
                    if e[0] in ab and e[1] in ab:
                        ab.append(e[1])
                        ab.append(e[0])
                    if e[0] in ac and e[1] in ac:
                        ac.append(e[1])
                        ac.append(e[0])
                    if e[0] in bc and e[1] in bc:
                        bc.append(e[1])
                        bc.append(e[0])
                #print(ab, ac, bc)
                ab_set = set(ab)
                ac_set = set(ac)
                bc_set = set(bc)
                path_set = ab_set | ac_set | bc_set
                path = len(path_set)
                #print(path, path_set)
                if path > max_path:
                    max_path = path
                    max_path_set = path_set
                    max_a, max_b, max_c = a, b, c
    print(max_path)
    print(max_a, max_b, max_c)

if __name__ == '__main__':
    main()