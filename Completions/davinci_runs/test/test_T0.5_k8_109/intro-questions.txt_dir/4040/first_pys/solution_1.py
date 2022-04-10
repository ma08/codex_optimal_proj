

import sys

def main():
    n,m,d = map(int, sys.stdin.readline().strip().split(' '))
    c = map(int, sys.stdin.readline().strip().split(' '))
    print n,m,d
    print c
    if len(c) != m:
        print "Invalid input"
        return
    # Construct the river
    river = [0] * n
    left = 0
    right = 0
    for i in xrange(m):
        if left + c[i] > n:
            print "Invalid input"
            return
        river[left:left+c[i]] = [i+1] * c[i]
        left += c[i]
    print river
    # Construct the graph
    graph = {}
    for i in xrange(n):
        if river[i] == 0:
            continue
        for j in xrange(1, d+1):
            if i+j >= n:
                break
            if river[i+j] == 0:
                continue
            if river[i] not in graph:
                graph[river[i]] = {}
            if river[i+j] not in graph[river[i]]:
                graph[river[i]][river[i+j]] = 0
            graph[river[i]][river[i+j]] += 1
    print graph
    # Find the path
    path = []
    while m > 0:
        if 1 not in graph:
            print "NO"
            return
        path.append(1)
        m -= 1
        while path[-1] in graph and len(graph[path[-1]]) > 0:
            path.append(graph[path[-1]].keys()[0])
            graph[path[-2]][path[-1]] -= 1
            if graph[path[-2]][path[-1]] == 0:
                del graph[path[-2]][path[-1]]
        if len(path) > 1:
            if path[-2] in graph and path[-1] in graph[path[-2]]:
                graph[path[-2]][path[-1]] += 1
            else:
                graph[path[-2]] = {path[-1]:1}
        path = path[:-1]
    print "YES"
    print ' '.join(map(str, path))

if __name__ == '__main__':
    main()