vertices = int(input())

if vertices == 0:
    print("-1")
    exit()
    
if vertices == 1:
    v = int(input())
    print(v)
    exit()

graph = [[0 for j in range(vertices)] for i in range(vertices)]

while True:
    l = list(map(int, input().split()))
    if len(l) == 1:
        vertex = l[0]
        break
    else:
        v_i, v_j = tuple(l)
        graph[v_i-1][v_j-1] = 1

vertex_list = []
for k in range(vertices):
    if graph[vertex-1][k] == 1:
        vertex_list.append(k+1)

print(len(vertex_list))
for i in range(len(vertex_list)):
    if i == len(vertex_list)-1:
        print(vertex_list[i])
    else:
        print(vertex_list[i],end=",")