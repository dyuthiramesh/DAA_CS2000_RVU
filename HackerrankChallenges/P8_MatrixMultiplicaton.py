matrix_1_i, matrix_1_j = map(int, input().split())

matrix_1 = []

for i in range(matrix_1_i):
    matrix_1.append(list(map(int, input().split())))

matrix_2_i, matrix_2_j = map(int, input().split())

if matrix_1_j != matrix_2_i:
    print(-1)
    exit()

matrix_2 = []

for i in range(matrix_2_i):
    matrix_2.append(list(map(int, input().split())))

m, n, p = matrix_1_i, matrix_1_j, matrix_2_j
mul_matrix = []
multiplications = 0
additions = 0

for i in range(m):
    l = []
    for j in range(p):
        temp_sum = []
        for k in range(n):
            temp_sum.append(matrix_1[i][k] * matrix_2[k][j])
            multiplications += 1
        total = sum(temp_sum)
        additions += len(temp_sum)-1
        l.append(total)
    mul_matrix.append(l)

for i in mul_matrix:
    for j in i:
        print(j, end=" ")
    print()

print(multiplications, additions)