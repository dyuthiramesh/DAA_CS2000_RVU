n_v = int(input())

if n_v <= 0:
    print(-1)
    exit()
    
n_e = int(input())

if n_e <= 0:
    print(-1)
    exit()
    
graph = [[0 for j in range(n_v)] for i in range(n_v)]    
    
for i in range(n_e):
    g_i, g_j = map(int, input().split())
    graph[g_i-1][g_j-1] = 1
    graph[g_j-1][g_i-1] = 1
    
dfs_order = [1]
stack = []
popped = []

visited = [0 for i in range(n_v)]

def dfs(v):
    visited[v-1] = 1
    for w in range(n_v):
        if graph[v-1][w] == 1 and visited[w] == 0:
            dfs_order.append(w+1)
            stack.append(w+1)
            dfs(w+1)
    if stack != []:
        popped.append(stack.pop())
            
dfs(1)
print(*dfs_order)
print(*popped)