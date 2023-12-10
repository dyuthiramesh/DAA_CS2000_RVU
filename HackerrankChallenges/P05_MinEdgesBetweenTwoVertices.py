vertices = int(input())
graph = [[0 for j in range(vertices)] for i in range(vertices)]

edges = int(input())
if edges == 0:
    print(-1)
    exit()

for _ in range(edges):
    v_i, v_j = map(int, input().split(","))
    if v_i>edges:
        v_i = edges
    elif v_j>edges:
        v_j = edges
    graph[v_i - 1][v_j - 1] = graph[v_j - 1][v_i - 1] = 1

vertex_i, vertex_j = map(int, input().split(","))

queue = [(vertex_i - 1, 0)]
visited = [False] * vertices

min_distance = float('inf')

while queue:
    current_vertex, distance = queue.pop(0)
    visited[current_vertex] = True

    if current_vertex + 1 == vertex_j:
        min_distance = distance
        break

    for neighbor in range(vertices):
        if graph[current_vertex][neighbor] == 1 and not visited[neighbor]:
            queue.append((neighbor, distance + 1))
            visited[neighbor] = True

if min_distance == float('inf'):
    print(-1)
else:
    print(min_distance)