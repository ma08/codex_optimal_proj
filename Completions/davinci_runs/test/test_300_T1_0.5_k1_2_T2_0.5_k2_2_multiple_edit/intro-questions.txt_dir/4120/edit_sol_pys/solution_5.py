

#!/usr/bin/python3
# https://www.hackerrank.com/challenges/beautiful-path/problem

import sys

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Complete this function
    if c_road > c_lib:
        return n*c_lib
    else:
        return n*c_road

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m, c_lib, c_road = input().strip().split(' ')
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        cities = []
        for cities_i in range(m):
           cities_t = [int(cities_temp) for cities_temp in input().strip().split(' ')]
           cities.append(cities_t)
        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)


def is_connected(g):
    used = [0 for i in range(n)]
    dfs(0, g, used)
    for i in range(n):
        if (not used[i]):
            return False
    return True

def get_dist(g):
    dist = [0 for i in range(n)]
    used = [0 for i in range(n)]
    q = [0]
    used[0] = 1
    while (len(q) > 0):
        cur = q[0]
        q = q[1:]
        for i in range(len(g[cur])):
            if (not used[g[cur][i]]):
                used[g[cur][i]] = 1
                q.append(g[cur][i])
                dist[g[cur][i]] = dist[cur] + 1
    return sum(dist)

def get_answer(g, m, k):
    dist = get_dist(g)
    best = dist
    ans = []
    for i in range(1 << m):
        if (bin(i).count('1') == n - 1):
            cur = deepcopy(g)
            for j in range(m):
                if ((i >> j) % 2 == 1):
                    cur[g[j][0]].remove(g[j][1])
                    cur[g[j][1]].remove(g[j][0])
            if (is_connected(cur)):
                cur_dist = get_dist(cur)
                if (cur_dist < best):
                    best = cur_dist
                    ans = []
                    ans.append(i)
                elif (cur_dist == best):
                    ans.append(i)
    return ans

ans = get_answer(g, m, k)
print(len(ans))
for i in range(len(ans)):
    print(bin(ans[i])[2:].zfill(m))

# Reference: https://github.com/jaehyunp/stanfordacm/blob/master/code/RoadsNotOnlyInBerland.cpp 
