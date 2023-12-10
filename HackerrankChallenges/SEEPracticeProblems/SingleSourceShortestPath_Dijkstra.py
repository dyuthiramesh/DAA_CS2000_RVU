vertices = int(input())
edges = int(input())

if vertices <= 0 or edges <= 0:
    print(-1)
    exit()

graph = [[9999 if i != j else 0 for j in range(vertices)] for i in range(vertices)]

for i in range(edges):
    g_i, g_j, weight = map(int, input().split())
    graph[g_i-1][g_j-1] = weight

visited = [0 for i in range(vertices)] 
visited[0] = 1
distance = [9999 for i in range(vertices)] 
distance[0] = 0


for v in range(vertices):
    if visited[v] == 0 and graph[0][v] != 9999:
        distance[v] = graph[0][v]

for _ in range(vertices):
    min_distance = 9999
    next_vertex = -1
    for v in range(vertices):
        if visited[v] == 0 and distance[v] < min_distance:
            next_vertex = v

    visited[next_vertex] = 1
    for v in range(vertices):
        if visited[v] == 0 and graph[next_vertex][v] != 9999:
            if distance[next_vertex] + graph[next_vertex][v] < distance[v]:
                distance[v] = distance[next_vertex] + graph[next_vertex][v]

for i in range(vertices):
    if i != 0:
        print(1,i+1,distance[i])