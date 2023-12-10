vertices = int(input())
edges = int(input())

if vertices <= 0 or edges <= 0:
    print(-1)
    exit()

graph = [[9999 for j in range(vertices)] for i in range(vertices)]

for i in range(edges):
    g_i, g_j, weight = map(int, input().split())
    graph[g_i-1][g_j-1] = weight

selected = [0 for i in range(vertices)] 
selected[0] = 1
total_cost = 0

for _ in range(vertices - 1):
    min_edge = [0, 0, 9999]
    for i in range(vertices):
        if selected[i] == 1:
            for j in range(vertices):
                if selected[j] == 0 and graph[i][j] < min_edge[2]:
                    min_edge = [i, j, graph[i][j]]
    selected[min_edge[1]] = 1
    total_cost += min_edge[2]
      
print(total_cost)