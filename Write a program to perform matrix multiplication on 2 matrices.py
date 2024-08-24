

# Write a program to perform matrix multiplication on 2 matrices

matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
    [7, 8],
    [9, 10],
    [11, 12]
]
result_rows = len(matrix_a)
result_columns = len(matrix_b[0])
result_matrix = [[0] * result_columns for _ in range(result_rows)]
for i in range(result_rows):  
    for j in range(result_columns):  
        for k in range(len(matrix_b)):  
            result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
print("Result of matrix multiplication:")
for row in result_matrix:
    print(row)
