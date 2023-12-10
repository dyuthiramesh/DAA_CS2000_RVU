matrix_1_i, matrix_1_j = map(int, input().split())

matrix_1 = []

for i in range(matrix_1_i):
    matrix_1.append(list(map(int, input().split())))

matrix_2_i, matrix_2_j = map(int, input().split())

if matrix_1_i != matrix_2_i or matrix_1_j != matrix_2_j:
    print(-1)
    exit()

matrix_2 = []

for i in range(matrix_2_i):
    matrix_2.append(list(map(int, input().split())))
        
sum_matrix = []
additions = 0

for i in range(matrix_1_i):
    l = []
    for j in range(matrix_1_j):
        l.append(matrix_1[i][j]+matrix_2[i][j])
        additions += 1
    sum_matrix.append(l)
    
for i in sum_matrix:
    for j in i:
        print(j, end=" ")
    print()

print(additions)