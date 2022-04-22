

N, M = map(int, input().split()) 
edges = [[] for _ in range(N)] 
for _ in range(M): 
    a, b, c = map(int, input().split()) 
    a -= 1 
    b -= 1 
    edges[a].append((b, -c)) 

dist = [1 << 60] * N 
dist[0] = 0 

# 負の閉路を探す 
for _ in range(N): 
    for i in range(N): 
        for e in edges[i]: 
            j, c = e 
            if dist[j] > dist[i] + c: 
                dist[j] = dist[i] + c 
                if i == N - 1: 
                    print(-1) 
                    exit() 

# 閉路がなければ最短距離を更新 
for i in range(N): 
    for e in edges[i]: 
        j, c = e 
        if dist[j] > dist[i] + c: 
            dist[j] = dist[i] + c 
print(-dist[N - 1]) 
