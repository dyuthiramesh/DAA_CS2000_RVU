n_v = int(input())
if n_v <= 0:
    print(-1)
    exit()
    
n_e = int(input())
if n_e <= 0:
    print(-1)
    exit()

graph = [[9999 if i != j else 0 for j in range(n_v)] for i in range(n_v)]
            
for i in range(n_e):
    l_i, l_j, w = map(int, input().split())
    graph[l_i-1][l_j-1] = w
    
for k in range(n_v):
    for j in range(n_v):
        for i in range(n_v):
            graph[j][i] = min(graph[j][i], graph[j][k]+graph[k][i])
            
for i in range(n_v):
    for j in range(n_v):
        if i!=j:
            print(i+1, j+1, graph[i][j])