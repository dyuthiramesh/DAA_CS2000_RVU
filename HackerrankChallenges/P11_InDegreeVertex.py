vertices = int(input())

graph = {}

vertices_list = []

try:
    while(1):
        l = list(input().split())
        for i in l:
            vertices_list.append(i)
        if l[0] not in graph:
            graph[l[0]] = list(l[1])
        else:
            graph[l[0]].append(l[1])
except EOFError:
    pass

vertices_list = sorted(list(set(vertices_list)))

in_degree = {}
for i in vertices_list:
    in_degree[i] = 0

for i in graph:
    for j in graph[i]:
        in_degree[j] += 1

for k in in_degree:
    print(in_degree[k],end=" ")